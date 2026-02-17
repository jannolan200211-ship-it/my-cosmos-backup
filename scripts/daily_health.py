import os
import json
import subprocess
import requests
import time
import glob

# Configuration
LOG_DIR = "/tmp/openclaw"
SESSION_DIR = os.path.expanduser("~/.openclaw/agents/main/sessions")
CONFIG_FILE = os.path.expanduser("~/.openclaw/openclaw.json")
HEARTBEAT_FILE = "memory/heartbeat-state.json"

results = {
    "status": "OK",
    "timestamp": time.time(),
    "checks": []
}

def fail(tool, code, msg, recovery):
    return {
        "status": "FAIL",
        "tool": tool,
        "error_code": code,
        "message": msg,
        "recovery_path": recovery
    }

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip(), 0
    except subprocess.CalledProcessError as e:
        return "", e.returncode

# 1. Gateway Process
out, code = run_cmd("pgrep -f 'openclaw gateway'")
if code == 0:
    results["checks"].append({"id": 1, "name": "Gateway Process", "status": "OK"})
else:
    results["status"] = "FAIL"
    results["checks"].append(fail("pgrep", 1, "Gateway process not found", "systemctl --user start openclaw-gateway"))

# 3. Systemd Service
out, code = run_cmd("systemctl --user is-active openclaw-gateway")
if out == "active":
    results["checks"].append({"id": 3, "name": "Systemd Service", "status": "OK"})
else:
    results["status"] = "FAIL"
    results["checks"].append(fail("systemctl", 3, f"Service state: {out}", "systemctl --user restart openclaw-gateway"))

# 4. AI Connectivity (Google)
try:
    r = requests.get("https://generativelanguage.googleapis.com", timeout=5)
    results["checks"].append({"id": 4, "name": "AI Connectivity", "status": "OK"})
except Exception as e:
    results["status"] = "WARN"
    results["checks"].append(fail("requests", 4, str(e), "Check internet connection"))

# 7. Disk Write/Space
try:
    with open("test_write.tmp", "w") as f:
        f.write("test")
    os.remove("test_write.tmp")
    results["checks"].append({"id": 7, "name": "Disk Write", "status": "OK"})
except Exception as e:
    results["status"] = "FAIL"
    results["checks"].append(fail("fs", 7, str(e), "Free up disk space"))

# 8. Config Sanity
try:
    with open(CONFIG_FILE) as f:
        json.load(f)
    results["checks"].append({"id": 8, "name": "Config JSON", "status": "OK"})
except Exception as e:
    results["status"] = "FAIL"
    results["checks"].append(fail("json", 8, "Invalid Config JSON", "openclaw config edit"))

# 9. Network Latency
out, code = run_cmd("ping -c 1 google.com")
if code == 0:
    results["checks"].append({"id": 9, "name": "Network", "status": "OK"})
else:
    results["status"] = "FAIL"
    results["checks"].append(fail("ping", 9, "Network unreachable", "Check VPN/Connection"))

print(json.dumps(results, indent=2))
