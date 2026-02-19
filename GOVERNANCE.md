# GOVERNANCE.md - System Policies & Guidelines

## 1. System Hierarchy (Tier Structure)

### 🧠 Tier 1: The Brain (Architect & Decision Maker)
- **Agent Name:** David
- **Primary Model:** `gemini-3-pro`
- **Account:** `jannolan200211@gmail.com` (Root/Admin)
- **Role:** 
  - High-level reasoning, strategy, and complex problem solving.
  - Final decision authority on task delegation.
  - API Key & Policy management.
  - Handling sensitive data and "Human-in-the-Loop" interactions.
- **Access Level:** Full System Access (Read/Write/Exec).

### 🛠 Tier 2: Specialists (Skill Executors)
- **Role:** Targeted execution (Coding, Deep Research, Data Analysis).
- **Primary Model:** `gemini-2.0-flash`
- **Fallback Model:** `gemini-1.5-pro`
- **Scope:** 
  - Executing specific sub-tasks defined by Tier 1.
  - Generating code, drafting content, parsing complex documents.
- **Access Level:** Scoped to specific tools/directories required for the task.

### 🤖 Tier 3: Workers (Operations & Monitoring)
- **Role:** Routine tasks, background monitoring, cron jobs, simple formatting.
- **Primary Model:** `gemini-1.5-flash` (Cost-Efficiency Optimized)
- **Fallback Model:** `gemini-1.5-flash-8b` (if available/applicable)
- **Scope:** 
  - Heartbeat checks, log rotation, simple summaries.
  - High-volume, low-complexity data processing.
- **Access Level:** Read-Only or heavily restricted Write access.

---

## 2. AI Model Routing & Fallback Policy

### Routing Logic
1. **Complexity Assessment:** Tier 1 analyzes the request.
   - *High Complexity/Reasoning?* -> Route to Tier 1 (`gemini-3-pro`).
   - *Specific Skill?* -> Route to Tier 2 (`gemini-2.0-flash`).
   - *Repetitive/Simple?* -> Route to Tier 3 (`gemini-1.5-flash`).

### Backup Plan (Resilience)
If the primary model for a tier fails (API Error 5xx, Rate Limit 429):
1. **Immediate Retry:** Wait 2s, retry once.
2. **Fallback Strategy:**
   - **Tier 1 Failure:** Downgrade to `gemini-1.5-pro` (Reasoning capability loss, but functional). Notify User.
   - **Tier 2 Failure:** Downgrade to `gemini-1.5-flash` or `gemini-1.0-pro`.
   - **Tier 3 Failure:** Pause task, log error, retry in 15 mins.
3. **Cross-Provider Redundancy:** (Future) If Google API is down globally, switch to backup provider (e.g., Anthropic/OpenAI) if keys are available.

---

## 3. Self-Healing & Recovery Protocols

### Circuit Breakers
- **Tool Failures:** If a tool fails **3 consecutive times** with the same error, stop calling it.
  - *Action:* Log error -> Search for alternative tool -> If none, escalate to User.
- **Infinite Loops:** If the Agent repeats the same thought/action loop **3 times**, force a "Stop & Re-assess" interrupt.

### State Recovery
- **Session Crash:** Upon restart, always read `memory/heartbeat-state.json` and recent `memory/YYYY-MM-DD.md` to restore context.
- **Orphaned Processes:** Tier 3 agents periodically check for "zombie" sub-agents and terminate them if their parent task is complete.

### Auto-Correction
- **Code Errors:** If generated code fails to run:
  1. Read the error log.
  2. Attempt to fix (max 2 attempts).
  3. If still failing, mark as "Needs Human Review".

---

## 4. API Key & Security Governance

- **Storage:** API Keys must exist **ONLY** in Environment Variables (`.env` or system env). Never write keys to Markdown files, logs, or chat history.
- **Rotation:** 
  - Triggers: Suspected leak, every 90 days (preventative).
  - Authority: Only Tier 1 (David) or Nolan can authorize key rotation.
- **Least Privilege:** Sub-agents (Tier 2/3) inherit only the permissions strictly necessary for their task.

---

## 5. Subscription Quota Management

- **Philosophy:** Since we are on a flat-rate subscription, the scarcity metric is **Message Cap/Rate Limit**, not Dollar Cost.
- **Quota Preservation:**
  - **Tier 1 (Pro):** High Value resource. Use strictly for complex reasoning, planning, and final outputs. Avoid using for simple echoes, formatting, or basic info retrieval.
  - **Tier 2/3 (Flash):** High Volume resource. Use proactively for drafting, summarization, and intermediate steps to preserve Tier 1 quota.
  - **Threshold Management:** Context size is strictly limited to **25,000 tokens** before automatic compaction to prevent API Rate Limit (429) triggers.
  - **Daily Brain-Dump:** Every day at 03:00 AM, all session logs must be summarized, flushed to `MEMORY.md`, and permanently cleared.

## 6. The Nolan Protocol (Resource Guard)
- **Philosophy:** Protect the 2GB VPS from resource depletion by strictly managing agent concurrency.
- **Concurrency Cap:** Primary agents are limited to **maxConcurrent: 1**. Sub-agents are capped at **2**.
- **The Queue System:** Heavy tasks (backups, bulk edits, long-range research) must be queued and run one at a time.
- **Always-on Router:** David (Tier 1) acts as the traffic controller, deciding when to spawn workers based on current system load.
- **Rate Limit Handling:**
  - If Tier 1 hits a rate limit (429 Too Many Requests), **automatically downgrade** to Tier 2/3 for the remainder of the hour/window to keep operations running.
  - Notify User only if the task *requires* Pro intelligence and cannot be completed by Flash.
