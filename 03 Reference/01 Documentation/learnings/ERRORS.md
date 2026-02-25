# ERRORS.md - Learning Logs (Error Repository)

### [ERR-20260225-001] Ineffective Deny Commands (Invalid Tool Names)
- **Issue:** OpenClaw config (`openclaw.json`) တွင် `gateway.nodes.denyCommands` အောက်၌ `camera.snap`, `camera.clip` ကဲ့သို့ နာမည်အမှားများ သုံးထားသဖြင့် command ပိတ်ဆို့မှု အလုပ်မလုပ်ခြင်း။
- **Root Cause:** OpenClaw ၏ native tool naming convention ဖြစ်သော `nodes.camera_snap`, `nodes.camera_clip` အစား `camera.snap` ဟု မှားယွင်းစွာ ခေါ်ဆိုခဲ့ခြင်း။
- **Remedy:** `openclaw.json` ရှိ `denyCommands` စာရင်းကို တိကျသော tool names (ဥပမာ: `nodes.camera_snap`, `nodes.camera_clip`) များဖြင့် ပြင်ဆင်ရန်။
- **Prevention:** `openclaw help` သို့မဟုတ် tool documentation တွင် ပါရှိသော တိကျသည့် tool names များကိုသာ config တွင် အသုံးပြုရန်။

### [ERR-20260223-001] Gateway Token Mismatch (Unresponsive Agent)
- **Symptom:** Gateway logs showed constant `unauthorized: gateway token mismatch` errors. Agent was unresponsive via Telegram until `openclaw doctor` was run manually by the user.
- **Root Cause:** Stale `openclaw-tui` (Terminal UI) processes were running in the background. These processes were using an old, invalid Gateway token from a previous session/configuration, causing a continuous loop of unauthorized connection attempts and cluttering logs.
- **Resolution:**
    1. Identified the background processes using `ps aux | grep openclaw-tui`.
    2. Terminated all conflicting processes using `pkill -9 -f openclaw-tui`.
    3. Ran `openclaw doctor --fix` to sync the current Gateway token with the system configuration.
    4. Restarted the Gateway service (`openclaw gateway restart`) to apply the correct token environment.
- **Prevention:** Always ensure Terminal UI (TUI) sessions are properly closed (Ctrl+C) before performing major configuration changes or Gateway restarts. Added a health check step to `daily_health.py` to monitor for stale TUI processes.
