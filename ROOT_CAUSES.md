# ROOT_CAUSES.md - ပြဿနာနှင့် အရင်းအမြစ် မှတ်တမ်း

ဤဖိုင်သည် ဖြစ်ပွားခဲ့သော ပြဿနာများ၏ အရင်းအမြစ် (Root Causes) များကို စနစ်တကျ မှတ်တမ်းတင်ထားရန် ဖြစ်သည်။ ဤသို့ဖြင့် ထပ်ခါတလဲလဲ ဖြစ်တတ်သော Pattern များကို ရှာဖွေနိုင်မည် ဖြစ်သည်။

| နေ့စွဲ | ပြဿနာ (Symptom) | အရင်းအမြစ် (Root Cause) | အဖြေ (Action Taken) |
| :--- | :--- | :--- | :--- |
| ၂၀၂၆-၀၂-၂၁ | GitHub Backup Failed & Brain Bot Sync Failed | Backup Script မှ `*.json` (secrets) များကို GitHub သို့ တင်ရန် ကြိုးစားခြင်းကြောင့် GitHub Push Protection မှ Block လုပ်ခဲ့သည်။ ထိုမှတစ်ဆင့် သမိုင်းကြောင်း (History) ကို ရှင်းလင်းစဉ် Bot Secrets များပါ ပျောက်ဆုံးသွားခဲ့သည်။ | `.gitignore` တွင် `client_secret.json` နှင့် `wrangler.json` ကို ထည့်သွင်းခဲ့သည်။ ပျောက်ဆုံးသွားသော Secrets များကို Git Reflog မှ ပြန်ယူ၍ Cloudflare Worker အား Re-deploy လုပ်ခဲ့သည်။ |
