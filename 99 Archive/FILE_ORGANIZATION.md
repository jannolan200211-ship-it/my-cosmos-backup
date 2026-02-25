# FILE_ORGANIZATION.md - Universal File Management System (5-99 Hierarchy)

ဤလမ်းညွှန်ချက်သည် OpenClaw Workspace အတွင်း ဖိုင်များကို စနစ်တကျ သိမ်းဆည်းရန်နှင့် Agent များ အလွယ်တကူ ရှာဖွေနိုင်ရန် ရည်ရွယ်သည်။

## ၁။ မူဝါဒအနှစ်ချုပ် (Core Philosophy)
- **Functional Categorization:** အချက်အလက်များကို "ရင်းမြစ်" (Source) အလိုက် မဟုတ်ဘဲ "အသုံးပြုမည့် ပုံစံ" (Usage Context) အလိုက် သိမ်းဆည်းပါ။
- **5-99 Rule:** Folder အဆင့် ၅ ဆင့်ထက် မနက်ရ။ အဆင့်တစ်ခုစီတွင် Folder ၉၉ ခုထက် မပိုရ။ (01-99 Numbering စနစ်သုံးပါ)။
- **Naming Convention:** `YYYY-MM-DD [Project] [Type]` သို့မဟုတ် `[Prefix]_[Name]` ပုံစံကို အသုံးပြုပါ။

## ၂။ Root Directory Structure (ပင်မ တည်ဆောက်ပုံ)

### 📂 01 Personal
- **ရည်ရွယ်ချက်:** Nolan ၏ ကိုယ်ရေးကိုယ်တာ မှတ်စုများ၊ စာရွက်စာတမ်းများနှင့် Preferences များ။
- **ပါဝင်ပစ္စည်းများ:** `PREFERENCES.md`, Personal Notes.

### 📂 02 Work
- **ရည်ရွယ်ချက်:** Professional လုပ်ငန်းခွင်နှင့် သက်ဆိုင်သော အရာအားလုံး။
- **Sub-folders:**
  - `01 Business Strategy`: စီးပွားရေး စီမံကိန်းများ (Business Plans, Strategy Docs).
  - `02 Projects`: လက်ရှိ Run နေသော Bot များ၊ Blueprint များ (Brain5000, Cerebro, VPN Bot).
  - `03 Operations`: နေ့စဉ် လုပ်ငန်းလည်ပတ်မှုများ (Jobs, Team Management).

### 📂 03 Reference
- **ရည်ရွယ်ချက်:** ကိုးကားစရာများ၊ စနစ်ပိုင်းဆိုင်ရာ ဖိုင်များနှင့် အသိပညာ ဗဟုသုတများ။
- **Sub-folders:**
  - `01 Documentation`: OpenClaw Docs, Learning Tracker, Context Files.
  - `02 System Configs`: Skills, Scripts, Secrets, Config Files.
  - `03 Tech Specs`: Technical Optimization, Token Usage, Root Cause Analysis.

### 📂 04 Quick Share
- **ရည်ရွယ်ချက်:** ယာယီ မျှဝေရန် ဖိုင်များ။ (Security Layer - မူရင်းကို မပို့ဘဲ Copy ကူးပြီးမှ ပို့ရန်)။
- **စည်းကမ်း:** ပို့ပြီးလျှင် ချက်ချင်း (သို့) ပုံမှန် ရှင်းလင်းပါ။

### 📂 00 Backups
- **ရည်ရွယ်ချက်:** အရေးကြီးဖိုင်များကို Drag-and-drop ဖြင့် အလွယ်တကူ သိမ်းဆည်းရန်။

### 📂 99 Archive
- **ရည်ရွယ်ချက်:** လက်ရှိ မသုံးတော့သော ဖိုင်ဟောင်းများ၊ Log များ။
- **ပါဝင်ပစ္စည်းများ:** `logs/`, `old_scripts/`, `README`, `LICENSE`, `CHANGELOG`.

## ၃။ System Files (Do Not Move)
အောက်ပါ ဖိုင်များသည် OpenClaw ၏ အသက်သွေးကြောများ ဖြစ်သောကြောင့် **Root** တွင်သာ အမြဲရှိနေရမည် -
- `AGENTS.md` (Agent Manifest)
- `SOUL.md` (Persona)
- `MEMORY.md` (Long-term Memory)
- `TOOLS.md` (Local Tool Configs)
- `USER.md` (User Profile)
- `HEARTBEAT.md` (Periodic Tasks)
- `IDENTITY.md` (Agent Identity)
- `GOVERNANCE.md` (Policies)
- `MESSAGING.md` (Communication Rules)
- `INDEX.md` (File Map)

## ၄။ Agent များ လိုက်နာရန် (Agent Guidelines)
- **File Creation:** ဖိုင်အသစ် ဖန်တီးတိုင်း အထက်ပါ Category တစ်ခုခုအောက်တွင်သာ သိမ်းဆည်းပါ။ Root တွင် ဖိုင်အသစ် မဆောက်ရ (System File မှလွဲ၍)။
- **Search:** ဖိုင်ရှာလျှင် သက်ဆိုင်ရာ Category အောက်ကို အရင်သွားရှာပါ။
- **Consistency:** Folder နာမည်ပေးလျှင် `01`, `02` စသဖြင့် Numbering တပ်ပါ။

---
*Last Updated: 2026-02-22 by David*