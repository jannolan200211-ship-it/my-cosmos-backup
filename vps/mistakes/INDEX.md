# MISTAKES & ERRORS INDEX

ဒီနေရာကတော့ ကျွန်တော်တို့ ကြုံတွေ့ခဲ့ရတဲ့ အမှားတွေနဲ့ သင်ခန်းစာတွေကို စနစ်တကျ စုစည်းထားတဲ့ နေရာဖြစ်ပါတယ်။

## Error Logs & RCA (Root Cause Analysis)

- **[2026-02-22] - Config Invalid Error (Unknown Keys)**
  - **Symptom:** OpenClaw status ပြရင် `Config invalid` ပြပြီး `priority`, `tags`, `keepAlive` keys တွေကို နားမလည်ကြောင်း ပြောခြင်း။
  - **Root Cause:** `openclaw.json` ထဲမှာ system schema က ခွင့်မပြုတဲ့ custom keys တွေကို manual ထည့်သွင်းမိခြင်း။
  - **Fix:** `openclaw doctor --fix` ကို သုံး၍သော်လည်းကောင်း၊ manual ဖြစ်စေ အဆိုပါ keys များကို ဖယ်ရှားခြင်း။
  - **Lesson:** Config ပြင်ရင် standard schema ကိုပဲ လိုက်နာရန်။
  - **Details:** `/root/.openclaw/workspace/vps/mistakes/2026-02-22-config-invalid.md`

---
*မှတ်ချက်: အမှားအသစ်တွေ ရှိလာတိုင်း ဒီနေရာမှာ အစဉ်လိုက် ထည့်သွင်းသွားပါမည်။*
