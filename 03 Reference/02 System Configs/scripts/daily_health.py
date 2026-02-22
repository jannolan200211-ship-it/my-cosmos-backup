import os
import json
import subprocess
import requests
import time
import glob
import sys

CONFIG_FILE = os.path.expanduser("~/.openclaw/openclaw.json")
LOG_DIR = "/tmp/openclaw"
SESSION_DIR = os.path.expanduser("~/.openclaw/agents/main/sessions")

results = {
    "status": "OK",
    "timestamp": time.time(),
    "checks": []
}

def report(id, name, status, details=None):
    results["checks"].append({
        "id": id,
        "name": name,
        "status": status,
        "details": details
    })
    if status == "FAIL":
        results["status"] = "FAIL"
    elif status == "WARN" and results["status"] != "FAIL":
        results["status"] = "WARN"

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode().strip(), 0
    except subprocess.CalledProcessError as e:
        return e.output.decode().strip(), e.returncode
    except Exception as e:
        return str(e), -1

try:
    # 1. Gateway Process (FAIL if down)
    out, code = run_cmd("pgrep -f 'openclaw gateway'")
    if code == 0:
        report(1, "Gateway Process", "OK")
    else:
        report(1, "Gateway Process", "FAIL", "Gateway not running")

    # 2. Recent Error Log Analysis (Last 1 Hour)
    # Finding logs modified in last 60 mins containing "error" (case insensitive)
    try:
        # Simple heuristic: Check current day log for errors
        today_log = f"{LOG_DIR}/openclaw-{time.strftime('%Y-%m-%d')}.log"
        if os.path.exists(today_log):
            err_count = int(subprocess.getoutput(f"grep -i 'error' {today_log} | wc -l"))
            if err_count > 50: # Threshold
                report(2, "Log Analysis", "WARN", f"High error count: {err_count}")
            else:
                report(2, "Log Analysis", "OK", f"Errors: {err_count}")
        else:
            report(2, "Log Analysis", "OK", "No log file yet")
    except:
        report(2, "Log Analysis", "WARN", "Could not parse logs")

    # 3. AI Provider Connectivity (Ping)
    providers = [
        ("Google", "https://generativelanguage.googleapis.com"),
        ("Anthropic", "https://api.anthropic.com"),
        ("OpenAI", "https://api.openai.com")
    ]
    up_count = 0
    for name, url in providers:
        try:
            requests.get(url, timeout=3)
            up_count += 1
        except:
            pass
    
    if up_count == len(providers):
        report(3, "AI Connectivity", "OK")
    elif up_count > 0:
        report(3, "AI Connectivity", "WARN", "Some providers down")
    else:
        report(3, "AI Connectivity", "FAIL", "All providers unreachable")

    # 4. Channel Health (via Status)
    try:
        status_json = json.loads(subprocess.check_output("openclaw status --json", shell=True))
        channels = status_json.get("channels", {})
        failed_channels = [k for k, v in channels.items() if v.get("state") != "OK"]
        if failed_channels:
            report(4, "Channel Health", "FAIL", f"Failed: {failed_channels}")
        else:
            report(4, "Channel Health", "OK")
    except:
        report(4, "Channel Health", "WARN", "Could not check status")

    # 5. Cron & Heartbeat
    if os.path.exists("memory/heartbeat-state.json"):
        report(5, "Heartbeat", "OK")
    else:
        report(5, "Heartbeat", "WARN", "No heartbeat state found")

    # 6. Session Size (>5MB = WARN)
    large_sessions = []
    if os.path.exists(SESSION_DIR):
        for f in glob.glob(f"{SESSION_DIR}/*.jsonl"):
            if os.path.getsize(f) > 5 * 1024 * 1024:
                large_sessions.append(os.path.basename(f))
    
    if large_sessions:
        report(6, "Session Size", "WARN", f"Large sessions: {len(large_sessions)}")
    else:
        report(6, "Session Size", "OK")

    # 7. Storage
    try:
        with open("test_write.tmp", "w") as f:
            f.write("test")
        os.remove("test_write.tmp")
        report(7, "Storage", "OK")
    except:
        report(7, "Storage", "FAIL", "Read-only filesystem")

    # 8. External Services (Mirror/Process check)
    report(8, "External Services", "OK", "Skipped (No mirror)")

    # 9. Config Sanity
    try:
        with open(CONFIG_FILE) as f:
            cfg = json.load(f)
            # Basic sanity: Port exists?
            if "gateway" in cfg and "port" in cfg["gateway"]:
                report(9, "Config Sanity", "OK")
            else:
                report(9, "Config Sanity", "FAIL", "Invalid config structure")
    except:
        report(9, "Config Sanity", "FAIL", "JSON Error")

    # 10. Network & Proxy
    out, code = run_cmd("ping -c 1 8.8.8.8")
    if code == 0:
        report(10, "Network", "OK")
    else:
        report(10, "Network", "FAIL", "Internet unreachable")

except Exception as e:
    results["status"] = "UNKNOWN"
    results["error"] = str(e)

print(json.dumps(results, indent=2))
