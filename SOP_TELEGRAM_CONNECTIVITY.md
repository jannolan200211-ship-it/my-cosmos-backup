# SOP_TELEGRAM_CONNECTIVITY.md - Self-Healing SOP

ဤဖိုင်သည် Nolan ၏ Telegram Bot ဆက်သွယ်မှု ပြဿနာများကို Autonomous အနေဖြင့် စစ်ဆေးပြီး ပြင်ဆင်နိုင်ရန် David (Manager) အတွက် လမ်းညွှန်ချက် ဖြစ်သည်။

## ၁။ `requireMention` Setting ကို စစ်ဆေးခြင်း
- **Issue:** Bot က စာမပြန်ခြင်း (Silence)။
- **Diagnostic:** `openclaw.json` ရှိ `channels.telegram.groups` အောက်ရှိ group ID တွင် `requireMention` ကို စစ်ပါ။
- **Action:** `true` ဖြစ်နေပါက Nolan ၏ ညွှန်ကြားချက်အရ `false` သို့ ချက်ချင်း ပြောင်းပါ။
- **Tool:** `edit` သို့မဟုတ် `openclaw config set channels.telegram.groups.-1003843376924.requireMention false`

## ၂။ Security Allowlist ပြဿနာ (Security Audit Warning)
- **Issue:** Audit တွင် "group commands have no sender allowlist" ပြနေခြင်း။
- **Diagnostic:** `openclaw security audit --deep` ကို run ၍ allowlist အခြေအနေကို ကြည့်ပါ။
- **Action:** 
  1. `openclaw pairing list` ဖြင့် pending request ရှိမရှိ စစ်ပါ။
  2. ရှိပါက `openclaw pairing approve <code>` ဖြင့် အတည်ပြုပါ။
  3. Pending မရှိပါက Nolan အား `/pair` command run ရန် အသိပေးပါ။

## ၃။ Connection & Proxy Status
- **Issue:** Gateway reachable မဖြစ်ခြင်း။
- **Diagnostic:** `openclaw status --deep` ကို run ၍ `Gateway` နှင့် `Telegram` OK ဖြစ်မဖြစ် စစ်ပါ။
- **Action:** 
  - Connection မကောင်းပါက `openclaw gateway restart --force` ကို သုံးပါ။
  - VPS firewall သို့မဟုတ် Tailscale status (`tailscale status`) ကို စစ်ပါ။

## ၄။ Smart Lazy Logic
- အလုပ်မစမီ `openclaw doctor` ကို အမြဲအရင် run ပါ။ ၎င်းသည် ၉၀% သော ပြဿနာများကို အလိုအလျောက် fix ပေးနိုင်သည်။
- ပြင်ဆင်ပြီးတိုင်း `openclaw gateway restart` ချရန် မမေ့ပါနှင့်။

---
*Status: Active (Last Updated: 2026-03-02)*
