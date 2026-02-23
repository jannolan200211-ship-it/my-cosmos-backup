# Detailed Plan: 24/7 Resilient Multi-Agent AI System (David)
Date: 2026-02-23
Version: 1.1

## 1. Multi-Account Rotation (The Failover Shield)
To ensure continuous operation, David uses a tiered access system.

- **Tier 1 (Primary):** `skyhtetaunglin2002@gmail.com` (Gemini CLI)
  - Purpose: Default engine for all high-level reasoning and chat.
  - Threshold: Switch to Tier 2 when 80% of the daily/minute quota is reached.
- **Tier 2 (Secondary):** `htetaungl451@gmail.com` (Gemini CLI)
  - Purpose: Backup engine. Takes over seamlessly if Tier 1 hits a hard limit or 80% threshold.
- **Tier 3 (Final Fallback):** `Local AI (Qwen-opt on VPS)`
  - Purpose: Emergency responsiveness. If all Cloud APIs are exhausted, David switches to "Low-Power Mode".
  - Behavior: Provides basic chat and local task execution until Cloud quotas reset.

## 2. Resource Management (Token Saving Protocol)
Saving tokens is as important as having more accounts.

- **Hybrid Delegation:** 
  - Thinking-heavy tasks (Decision making, complex coding) -> Cloud Gemini.
  - Thinking-light tasks (Summary, text formatting, cleanup) -> Local Qwen-opt (Tier 4 Worker).
- **Aggressive Summarization:** 
  - Every 25,000 tokens, the session history is summarized using `Local AI`.
  - Only the summary and the most recent 5-10 messages are kept in active context.
  - Full logs are flushed to `/root/.openclaw/workspace/memory/`.

## 3. Self-Healing & Health Checks (The Guardrail)
David monitors his own status to prevent silent failures.

- **Cron Health Check:** 
  - Runs every 6 hours (`daily_health.py`).
  - Checks if tokens for all registered accounts are valid.
  - Verifies Gateway connectivity.
- **Auto-Repair:** 
  - If a `token_mismatch` is detected in logs, David runs `openclaw doctor --fix` and restarts the gateway automatically.

## 4. Communication Protocol (User Transparency)
Nolan is kept informed without being overwhelmed.

- **Failover Alert:** "Account A hit limit. Switching to Account B to continue our work."
- **Daily Reset Notification:** "Quotas reset. Resuming with Primary account."
- **Emergency Alert:** "Cloud APIs exhausted. Running in Local Mode for basic assistance."

---
*Developed by David (Manager)*
*Approved by: Nolan (Confirmed: 2026-02-23)*
*Status: ACTIVATED (Updated: v1.1 - Removed AntiGravity)*
