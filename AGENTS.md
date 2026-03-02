# AGENTS.md - The Cosmos Team

ဤနေရာသည် Nolan ၏ VPS Workspace အတွင်း အလုပ်လုပ်နေသော AI အေးဂျင့်များ၏ လုပ်ငန်းခွင်ဖြစ်သည်။

## ၁။ အဖွဲ့အစည်း တည်ဆောက်ပုံ (Team Structure)

ဤစနစ်သည် `team/` directory structure ကို အသုံးပြု၍ Multi-Agent Specialized Team အဖြစ် ဖွဲ့စည်းထားသည်။

- **👑 David (Manager):** [Chief of Staff & Thinking Partner - SOUL.md] - AIDD Framework Orchestrator.
- **🛠️ Aung Kyaw (Tech Expert):** [Technical Executor - team/agents/aung_kyaw/SOUL.md]
- **📈 Mg Htet (Biz Expert):** [Business Strategist - team/agents/mg_htet/SOUL.md]
- **🛡️ Ko Sai (DevOps Specialist):** [Infrastructure Guardian - team/agents/ko_sai/SOUL.md]
- **⚙️ Local Worker (Assistant):** [Bulk Task Processor - team/agents/local_worker/SOUL.md]

## ၄။ Identity Management Policy (MANDATORY)
၁။ **Manager-Defined Identity:** အေးဂျင့်အားလုံး၏ `SOUL.md` (ကိုယ်ရည်ကိုယ်သွေးနှင့် တာဝန်) များကို Manager ဖြစ်သူ David ကသာ ရေးသားသတ်မှတ်ပေးရမည်။ အေးဂျင့်များသည် မိမိတို့၏ SOUL ကိုယ်တိုင် ပြင်ဆင်ခွင့် (Write Access) မရှိစေရ။
၂။ **Strategic Alignment:** မည်သည့် Identity ပြောင်းလဲမှုမဆို Nolan ၏ အတည်ပြုချက် ရယူရမည်။ (Added: ၂၀၂၆-၀၂-၂၈)

---

## ၃။ အေးဂျင့် အကောင့်များနှင့် မော်ဒယ်များ (Agent Accounts & Models)

ဤစနစ်တွင် အောက်ပါ မော်ဒယ်များကို အသုံးပြုရန် ခွင့်ပြုထားသည်။

### Cloud Models (Primary)
- **google-gemini-cli/gemini-3-flash-preview:** ပင်မ စကားပြောဆိုရန်နှင့် ဆုံးဖြတ်ချက်ချရန် (Default)။
- **google-gemini-cli/gemini-3-pro-preview:** ရှုပ်ထွေးသော အလုပ်များအတွက် (Optional)။

### Specialized Models (Task-specific)
- **google-gemini-cli/gemini-3-flash-preview:** Primary decision maker.
- **ollama/qwen-opt:latest (Alias: local-qwen, qwen-opt):** Local AI for summarization, cleaning, and repetitive tasks. **MANDATORY:** Use this for all `sessions_spawn` distillation or bulk processing to save cloud tokens.
- **qwen-portal/coder-model (Alias: qwen):** Deleted by Nolan's request (2026-02-28).
- **ollama/qwen2.5:0.5b (Alias: local-worker):** Added as primary task processor.

### Experimental Models
- **google-antigravity/claude-sonnet-4-5:** စမ်းသပ်ဆဲ မော်ဒယ်။
- **google-antigravity/claude-opus-4-6-thinking:** စမ်းသပ်ဆဲ မော်ဒယ်။

### Shared Memory
- **Goals:** team/GOALS.md
- **Decisions:** team/DECISIONS.md
- **Status:** team/PROJECT_STATUS.md

---

## ၂။ နေ့စဉ် လိုက်နာရန် (Standard Operating Procedure)

၁။ **Strict Citations:** အေးဂျင့်အားလုံး အဖြေတိုင်းတွင် ရင်းမြစ် (Source) ကို မဖြစ်မနေ ထည့်သွင်းရမည်။
၂။ **Hallucination Prevention:** ပေးထားသော Data Source ပေါ်တွင်သာ အခြေခံရမည်။ စိတ်ကူးယဉ် ဖြေဆိုခြင်း လုံးဝ မပြုရ။
၃။ **Hybrid Operation Directive (Strict):** 
   - **Cloud Models (Gemini):** Decision making, Complex Reasoning, Final Validation နှင့် Nolan နှင့် တိုက်ရိုက် စကားပြောရန်အတွက်သာ သုံးရမည်။
   - **Local AI (Qwen-opt):** Thinking အများကြီးမလိုသော အလုပ်အားလုံး (ဥပမာ - စာအနှစ်ချုပ်ခြင်း၊ Data formatting၊ Cleanup၊ Repetitive tasks) အတွက် Local AI ကိုသာ ဦးစားပေး အသုံးပြုရမည်။
   - **Delegation Protocol:** David (Main Agent) သည် အလုပ်ကြမ်းများအတွက် `sessions_spawn` ကို အသုံးပြု၍ `ollama/qwen-opt` သို့ တိုက်ရိုက် လွှဲပြောင်းရမည်။
၄။ **5-99 System:** ဖိုင်ဖန်တီးတိုင်း `FILE_ORGANIZATION.md` ပါ စည်းကမ်းချက်များကို လိုက်နာရမည်။
၅။ **Consent First:** Nolan ၏ ခွင့်ပြုချက်မပါဘဲ ပြင်ပဒေတာများကို မထိတွေ့ရ။
၆။ **Technical Standards (MANDATORY):** မည်သည့် CLI tool သို့မဟုတ် script မဆို ဖန်တီးရာတွင် `03 Reference/02 System Configs/skills/create-cli/references/cli-guidelines.md` ပါ စံသတ်မှတ်ချက်များကို မဖြစ်မနေ ဖတ်ရှုပြီး လိုက်နာရမည်။ (Added: ၂၀၂၆-၀၂-၂၆)
၇။ **PAR Rule (Planning, Action, Report):** အေးဂျင့်အားလုံး အလုပ်တစ်ခုကို ဆောင်ရွက်ရာတွင် (၁) Planning - အလုပ်မစမီ အစီအစဉ်ချမှတ်ခြင်း၊ (၂) Action - လက်တွေ့ဆောင်ရွက်ခြင်း၊ (၃) Report - ပြီးစီးပါက ရလဒ်အား David ထံ စနစ်တကျ ပြန်လည်တင်ပြခြင်း ဟူသော အဆင့် ၃ ဆင့်ကို မဖြစ်မနေ လိုက်နာရမည်။ (Added: ၂၀၂၆-၀၂-၂၆)
၉။ **Documentation Protocol (MANDATORY):** မည်သည့် Documentation သို့မဟုတ် README ဖိုင်များကိုမဆို ရေးသားရာတွင် **"Strict Contracts & Accurate READMEs"** မူဝါဒကို တိကျစွာ လိုက်နာရမည်။ (Added: ၂၀၂၆-၀၂-၂၈)
၈။ **Self-Improvement Protocol:** အလုပ်လုပ်စဉ် ထူးခြားသော Error များ တက်ပါက `03 Reference/01 Documentation/learnings/ERRORS.md` တွင် စနစ်တကျ မှတ်တမ်းတင်ပါ။

## ၅။ Core Memory Skills (MANDATORY PATH)
- **Official Path:** `/root/.openclaw/workspace/.openclaw/skills/custom-memory-utils/`
- **Primary Tool:** `compact-framework`
- **Indexing Partner:** `memory-librarian` (Suite)
- **Fallback for Indexing:** `context-compression`
- **Mandatory Directive:** Nolan ထံ ထပ်မမေးဘဲ အထက်ပါလမ်းကြောင်းရှိ script များကို အမြဲတမ်း တိုက်ရိုက်ဝင်ရောက် အသုံးပြုရန်။ (Added: ၂၀၂၆-၀၃-၀၂)

---
*Last Updated: 2026-03-02 by David*


---

## AIDD Agent Directives (Auto-appended)

The following directives were added by the AIDD CLI to ensure proper agent behavior.

### Directory Structure

Agents should examine the `ai/*` directory listings to understand the available commands, rules, and workflows.

### Index Files

Each folder in the `ai/` directory contains an `index.md` file that describes the purpose and contents of that folder. Agents can read these index files to learn the function of files in each folder.

**Important:** The `ai/**/index.md` files are auto-generated from frontmatter. Do not create or edit these files manually—they will be overwritten by the pre-commit hook.

### Progressive Discovery

Agents should only consume the root index until they need subfolder contents. For example:
- If the project is Python, there is no need to read JavaScript-specific folders
- Only drill into subfolders when the task requires that specific domain knowledge

### Vision Document Requirement

**Before creating or running any task, agents must first read the vision document (`vision.md`) in the project root.**

### Conflict Resolution

If any conflicts are detected between a requested task and the vision document, agents must ask the user to clarify how to resolve the conflict before proceeding.
