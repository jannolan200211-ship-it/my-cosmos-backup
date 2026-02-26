# Ko Sai's Daily Operations Checklist (DevOps)

ကိုစိုင်း (Ko Sai) အနေဖြင့် နေ့စဉ် ပုံမှန်စစ်ဆေးရမည့် အလုပ်များ ဖြစ်သည်။

## ၁။ စနစ်ကျန်းမာရေး စစ်ဆေးခြင်း (Morning Check - 09:00 AM)
- [ ] **Disk Usage:** `/` partition သည် ၈၀% ထက် မကျော်လွန်ကြောင်း စစ်ဆေးရန်။ (`df -h`)
- [ ] **RAM Status:** Free RAM သည် ၂၀၀ MB အထက်တွင် ရှိနေကြောင်း အတည်ပြုရန်။ (`free -m`)
- [ ] **Service Health:** OpenClaw Gateway နှင့် Ollama Server များ ပုံမှန်လည်ပတ်နေကြောင်း စစ်ဆေးရန်။

## ၂။ လုံခြုံရေးနှင့် Backup စစ်ဆေးခြင်း (Mid-day Check - 01:00 PM)
- [ ] **GitHub Sync:** နောက်ဆုံး Backup သည် GitHub ပေါ်သို့ အောင်မြင်စွာ ရောက်ရှိခြင်း ရှိ/မရှိ စစ်ဆေးရန်။
- [ ] **Log Rotation:** `99 Archive/logs/` ထဲရှိ log ဖိုင်များ အလွန်အမင်း ကြီးမားမလာစေရန် စစ်ဆေးရန်။

## ၃။ အစီရင်ခံစာ တင်ပြခြင်း (Nightly Review - 11:55 PM)
- [ ] **System Status Report:** တစ်နေ့တာအတွင်း စနစ်၏ ကျန်းမာရေး အခြေအနေ (Healthy/Warning) ကို David မှတစ်ဆင့် Nolan ထံ အနှစ်ချုပ် တင်ပြရန်။
- [ ] **Maintenance:** အပတ်စဉ် OS Updates များ ရှိပါက Nolan ထံ ခွင့်ပြုချက်တောင်းခံရန်။

---
*Created by David for Ko Sai*
