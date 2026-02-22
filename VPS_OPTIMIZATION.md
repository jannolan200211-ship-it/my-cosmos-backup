# VPS_OPTIMIZATION.md - VPS Performance Logs

## Optimization History

### 2026-02-22: Tier 4 Local Worker Configuration (Option C)
- **Strategy:** On-Demand (Option C).
- **Parameters:**
  - `keep_alive: 0` (Unload immediately after task).
  - `num_ctx: 2048` (Context limit for RAM efficiency).
  - `num_thread: 2` (Match CPU cores).
- **Setup:** Linked `qwen-opt` as Tier 4 worker in `openclaw.json`.
- **Automation:** Updated `/root/.openclaw/workspace/scripts/tier4.py` with `keep_alive: 0`.
- **Error Note:** `openclaw.json` config does not support custom keys like `priority` or `tags` in model definitions. Adding them causes "Config Invalid" errors. Stick to standard OpenClaw schema.
- **Result:** Successfully running local AI without persistent RAM usage.
