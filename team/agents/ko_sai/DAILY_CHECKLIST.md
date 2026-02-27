# Ko Sai's "Reef Model" Operations Checklist

ကိုစိုင်း (Ko Sai) အနေဖြင့် နေ့စဉ် ပုံမှန်စစ်ဆေးရမည့် Infrastructure Guardian အလုပ်များ ဖြစ်သည်။

## ၁။ နံနက်ခင်း တင်ပြမှု (Morning Briefing - 08:00 AM)
- [ ] **Weather:** ရန်ကုန်မြို့၏ ရာသီဥတု အခြေအနေကို စစ်ဆေးရန်။
- [ ] **Schedules:** Nolan ၏ Calendar နှင့် Google Tasks အနှစ်ချုပ်ကို ယူရန်။
- [ ] **System Status:** CPU/RAM/Disk ကျန်းမာရေးနှင့် Service များ UP/DOWN Status စစ်ရန်။
- [ ] **Daily Briefing:** အထက်ပါ အချက်များကို Nolan ထံ စနစ်တကျ Report ပို့ရန်။

## ၂။ ပုံမှန် စောင့်ကြည့်မှု (Heartbeat Checks - Every 15-60 Mins)
- [ ] **Resource Limit:** RAM 80% ကျော်ပါက Nolan ထံ ချက်ချင်း Alert ပို့ရန်။
- [ ] **Service Watchdog:** OpenClaw နှင့် Ollama ပုံမှန် လည်ပတ်နေကြောင်း စစ်ရန်။
- [ ] **Self-Healing:** Service တစ်ခုခု Down ပါက အကြောင်းရင်းရှာပြီး Nolan ထံ ပြုပြင်ရန် ခွင့်ပြုချက်တောင်းရန်။

## ၃။ လုံခြုံရေးနှင့် Backup (Every 6 Hours)
- [ ] **Secret Scanning:** Workspace ထဲတွင် Plain text secrets များ မရှိကြောင်း စစ်ဆေးရန်။
- [ ] **GitHub Sync:** Auto-backup အောင်မြင်ကြောင်းနှင့် Repo ကျန်းမာကြောင်း စစ်ရန်။

## ၄။ ညဉ့်နက်ပိုင်း ပြုပြင်ထိန်းသိမ်းမှု (Nightly Review - 11:55 PM)
- [ ] **Error Log Review:** တစ်နေ့တာအတွင်း ဖြစ်ခဲ့သော Error များအား Root Cause ရှာဖွေပြီး `ERRORS.md` တွင် မှတ်တမ်းတင်ရန်။
- [ ] **Improvement:** နောက်တစ်ကြိမ် အမှားမထပ်စေရန် စနစ်အား Hardening လုပ်ရန် အဆိုပြုချက် တင်ပြရန်။

---
*Created by David for Ko Sai (Infrastructure Specialist)*
