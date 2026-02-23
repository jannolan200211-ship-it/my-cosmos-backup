# ERRORS.md - Learning Logs (Error Repository)

### [ERR-20260223-001] Gateway Token Mismatch (Unresponsive Agent)
- **Symptom:** Gateway logs showed constant `unauthorized: gateway token mismatch` errors. Agent was unresponsive via Telegram until `openclaw doctor` was run manually by the user.
- **Root Cause:** Stale `openclaw-tui` (Terminal UI) processes were running in the background. These processes were using an old, invalid Gateway token from a previous session/configuration, causing a continuous loop of unauthorized connection attempts and cluttering logs.
- **Resolution:**
    1. Identified the background processes using `ps aux | grep openclaw-tui`.
    2. Terminated all conflicting processes using `pkill -9 -f openclaw-tui`.
    3. Ran `openclaw doctor --fix` to sync the current Gateway token with the system configuration.
    4. Restarted the Gateway service (`openclaw gateway restart`) to apply the correct token environment.
- **Prevention:** Always ensure Terminal UI (TUI) sessions are properly closed (Ctrl+C) before performing major configuration changes or Gateway restarts. Added a health check step to `daily_health.py` to monitor for stale TUI processes.
