# MODEL_ROUTING.md - Smart Hybrid Routing Strategy

## ၁။ ရည်ရွယ်ချက် (Objective)
Free User ဖြစ်သော Nolan အတွက် API Token အသုံးပြုမှုကို အထိရောက်ဆုံး လျှော့ချရန်နှင့် VPS ပေါ်ရှိ Local AI (Tier 4) အား အကျိုးရှိရှိ အသုံးပြုရန်။

## ၂။ Routing Logic (Dynamic Hybrid Model)

အလုပ်တစ်ခု ရောက်လာပါက အောက်ပါ ဦးစားပေး အစဉ်အတိုင်း ခွဲဝေမည်-

| အလုပ်အမျိုးအစား (Task Category) | အသုံးပြုမည့် Model | မှတ်ချက် |
| :--- | :--- | :--- |
| **Daily Chat (Casual)** | Gemini 3 Flash | မြန်မာစာ ပီပြင်စေရန်။ |
| **Large File Summarization** | Local AI (Qwen-opt) | Context ကြီးမားမှုကို အရင်းအနှီးမကုန်ဘဲ ဖြေရှင်းရန်။ |
| **Basic Text Cleanup/Format** | Local AI (Qwen-opt) | JSON/Markdown Formatting များအတွက်။ |
| **Complex Coding/Logic** | Gemini 3 Pro / Flash | တိကျမှုရှိစေရန်။ |
| **Final Review/Refinement** | Gemini 3 Flash | Local AI မှ ထွက်လာသော ရလဒ်များကို အချောသတ်ရန်။ |

## ၃။ အမှားကိုင်တွယ်ပုံ (Fail-safe Protocol)
1. Local AI မှ Error တက်ပါက သို့မဟုတ် Nolan ၏ လိုအပ်ချက်နှင့် မကိုက်ညီပါက ချက်ချင်းရပ်နားပါ။
2. Nolan ထံသို့ "Gemini ဖြင့် အစားထိုးသုံးမလား" ဟု Button ဖြင့် မေးမြန်းပါ။
3. ခွင့်ပြုချက် ရမှသာ Gemini ကို ပြောင်းသုံးပါ။

## ၄။ ပွင့်လင်းမြင်သာမှု (Transparency)
Telegram တွင် စာပြန်တိုင်း အပေါ်ဆုံးတွင် အသုံးပြုထားသော Model Tag ကို ပြသမည်-
- `🤖 [Local AI အသုံးပြုထားသည်]`
- `✨ [Gemini AI အသုံးပြုထားသည်]`
- `🔄 [Hybrid: Local + Gemini]`

## ၅။ အစီရင်ခံစာနှင့် မှတ်တမ်း (Reporting & Logs)
- **မှတ်တမ်း:** `/root/.openclaw/workspace/vps/logs/routing/YYYY-MM-DD.jsonl` တွင် အသေးစိတ် သိမ်းဆည်းမည်။
- **အစီရင်ခံစာ:** အပတ်စဉ် တနင်္ဂနွေနေ့ ညနေ ၆ နာရီတွင် Token ချွေတာမှု အကျိုးကျေးဇူးကို Nolan ထံ တင်ပြမည်။
- **Metric:** API Token Quota သက်သာမှုနှင့် ခန့်မှန်းခြေ USD တန်ဖိုး နှစ်ခုလုံးကို ပြသမည်။

## ၆။ ကန့်သတ်ချက်များ (Restrictions)
- အရေးကြီးသော ရုံးစာနှင့် မြန်မာစာ ဘာသာပြန်များကို Local AI အား မခိုင်းရ။
- ငွေကြေးနှင့် ကိုယ်ရေးကိုယ်တာ လျှို့ဝှက်ချက်များကို Local AI အား မခိုင်းရ။
