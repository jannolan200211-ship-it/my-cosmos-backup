# Status Classification Protocol

## Overview

Simplified health monitoring protocol for VPS deployments. Focuses on 5 critical subsystems that directly impact reliability.

---

## Status Levels

| Status | Definition | Action Strategy |
|--------|-----------|-----------------|
| **OK** | System stable, all checks pass | Normal heartbeat monitoring |
| **WARN** | Non-critical issues detected | Investigation + proactive remediation |
| **FAIL** | Critical subsystem failure | Immediate remediation protocol + alert |
| **UNKNOWN** | Monitoring system cannot assess | Investigate monitoring system, check connectivity |

---

## 5 Core Health Checks

### 1. Gateway Process Discovery
**What:** Verify OpenClaw Gateway is running  
**Command:** `systemctl is-active openclaw || pgrep -f openclaw`  
**Classification:**
- Running → OK
- Stopped → **FAIL**

**So What:** Gateway down = entire system down (all agent communication stops)

---

### 2. Recent Error Log Parsing
**What:** Check for recent errors in gateway logs  
**Command:** `tail -100 /root/.openclaw/logs/gateway.log | grep -ic error`  
**Classification:**
- 0-2 errors → OK
- 3-10 errors → **WARN**
- >10 errors → **FAIL**

**So What:** Detects silent failures (system appears running but internal errors accumulating)

---

### 3. Disk Space Health
**What:** Monitor available disk space  
**Command:** `df -h / | awk 'NR==2 {print $5}' | sed 's/%//'`  
**Classification:**
- <85% → OK
- 85-94% → **WARN**
- ≥95% → **FAIL**

**So What:** Full disk = agents cannot save memory, cascading failures

---

### 4. Session Integrity and Size
**What:** Detect oversized session files  
**Command:** `find /root/.openclaw/agents/main/sessions -name "*.jsonl" -size +5M`  
**Classification:**
- No large files → OK
- 1-2 large files → **WARN**
- >2 large files → **FAIL**

**So What:** Large sessions burn massive tokens, degrade performance

---

### 5. OpenClaw System Status
**What:** Run built-in status check  
**Command:** `openclaw status --json`  
**Classification:**
- All services OK → OK
- Channel issues / warnings → **WARN**
- Gateway errors / critical → **FAIL**

**So What:** Comprehensive system health snapshot (channels, sessions, config)

---

## Check Execution Order

1. **Gateway Process** (fastest, most critical)
2. **Disk Space** (fast, critical)
3. **OpenClaw Status** (medium, comprehensive)
4. **Error Logs** (medium, diagnostic)
5. **Session Size** (slowest, optimization)

Stop on **FAIL** and report immediately.

---

## Output Format

### OK Status
```
Status: OK
All systems operational.
```

### WARN Status
```
Status: WARN
Issues detected:
- Disk space: 87% (threshold: 85%)
- Large session: agent:main:main (6.2MB)

Recommended actions:
1. Clean old logs
2. Compact large session
```

### FAIL Status
```
Status: FAIL
Critical failure detected:
- Gateway: NOT RUNNING

Immediate action required:
1. Restart gateway: systemctl restart openclaw
2. Check logs: tail -50 /root/.openclaw/logs/gateway.log
```

---

## Automation

**Schedule:** Every 12 hours (00:00, 12:00 Asia/Yangon)  
**Model:** `gemini-3-flash` (cost-efficient)  
**Delivery:** Telegram announcement  
**Session:** Isolated (no context pollution)

---

## Token Budget

**Estimated per check:**
- Input: ~2k tokens (protocol + commands)
- Output: ~1k tokens (status report)
- **Total: ~3k tokens/check**

**Daily (2 checks):** ~6k tokens  
**Monthly:** ~180k tokens (within free tier)

---

## Maintenance

**Review quarterly:**
- Adjust thresholds based on actual usage
- Add/remove checks as system evolves
- Monitor token costs

**Last updated:** 2026-02-16
