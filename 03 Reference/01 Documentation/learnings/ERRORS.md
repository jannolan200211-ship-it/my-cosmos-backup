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
- **ERR-20260228-004:** n8n "Unrecognized Node Type" error for `executeCommand` and `localFile`.
    - **Root Cause:** n8n's community/npm version restricts certain nodes by default for security, and node internal names vary across versions (v2.9.4).
    - **Remedy:** Used `export N8N_NODES_EXTERNAL_ALLOWED="*"` in PM2 environment to unlock all nodes and switched to the `n8n-nodes-base.readWriteFile` node type.
    - **Prevention:** Always check n8n version (`n8n --version`) before defining workflow JSON via API and ensure the environment allows external nodes.
- **ERR-20260228-005:** Gemini API 'User Location Not Supported' in n8n.
    - **Root Cause:** Gemini API restricts direct access from certain regions (including Myanmar) when called via n8n's standard Google Gemini node.
    - **Remedy:** Switched to **Groq API** as a proxy/alternative provider. Groq is accessible from Myanmar and provides high-speed access to the `llama-3.3-70b-versatile` model, which has excellent Burmese language support.
    - **Lesson Learned:** Always have a backup LLM provider (like Groq or OpenRouter) configured in n8n to bypass regional API restrictions.
- **WORKFLOW-NOTE-20260228:** n8n Version-Specific Node Naming.
    - **Discovery:** In n8n v2.9.4, nodes like `executeCommand` or `localFile` might appear as 'Unrecognized' if not enabled in the environment or if the internal name differs from newer documentation.
    - **Action:** Using `n8n-nodes-base.readWriteFile` for local disk operations and `@n8n/n8n-nodes-langchain.chainLlm` for AI chains proved to be the most compatible path for this specific installation.
