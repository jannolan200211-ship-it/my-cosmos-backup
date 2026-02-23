# Probability & Failover Analysis (Mental Models)
Date: 2026-02-23

## 🧠 Mental Model Analysis

### 1. Inversion (Thinking Backwards)
**Scenario:** "What causes the failover to fail?"
- **Risk:** Both accounts hit rate limits simultaneously.
- **Risk:** Gmail tokens expire without auto-renewal.
- **Risk:** David (Main Agent) loses access to the config files.

### 2. First Principles (Root Cause Analysis)
**Truth:** API access is a finite resource.
- **Fact:** Gemini Free/Flash has tight per-minute and per-day limits.
- **Fact:** Context window size directly impacts token consumption.

### 3. Redundancy & Margin of Safety
**Strategy:** Having two accounts is good, but having a "Safety Net" is better.
- **Gap:** If both Gmails fail, the system stops.
- **Solution:** Always keep the Local AI (Tier 4) as the "Infinite Fallback".

## 🛡️ Actionable Solutions (Proposed)

### A. The "Smart Rotation" Logic
Instead of waiting for an error, David will track token usage:
- If Account A reaches 80% of its daily quota, switch to Account B proactively.
- This prevents "Hard Stops" during critical tasks.

### B. Context Pruning (Token Saving)
- Aggressive summarization before sending long histories to Gemini.
- Use Local AI for "Cleaning" tasks to save Cloud tokens.

### C. The "Last Resort" Protocol
- If all Cloud APIs fail, David automatically shifts to a "Low-Power Mode" using Local Qwen-opt to stay responsive to Nolan.

---
*Analyzed by David (Manager)*
