# RCA: Config Invalid Error (2026-02-22)

## ဖြစ်စဉ် (Symptom)
`openclaw.json` ပြင်ဆင်ပြီးနောက် `openclaw status` စစ်ဆေးရာတွင် `Config invalid` error တက်လာပြီး စနစ်က ပုံမှန် အလုပ်မလုပ်တော့ခြင်း။

## အကြောင်းအရင်း (Root Cause)
Local AI setup လုပ်စဉ်တွင် Gemini ရဲ့ priority သတ်မှတ်ရန်နှင့် Ollama tags များ ထည့်သွင်းရန်အတွက် `openclaw.json` ထဲသို့ အောက်ပါ keys များ ထည့်သွင်းမိခြင်း-
- `priority`
- `tags`
- `keepAlive`

ဤ keys များသည် OpenClaw စနစ်၏ တရားဝင် Configuration Schema ထဲတွင် မပါဝင်သောကြောင့် စနစ်က နားမလည်ဘဲ ငြင်းပယ်ခြင်း ဖြစ်သည်။

## ဖြေရှင်းချက် (Resolution)
၁။ `openclaw.json` ထဲမှ အဆိုပါ Unknown Keys များကို ဖယ်ရှားခဲ့သည်။
၂။ `openclaw status` ပြန်လည်စစ်ဆေးပြီး စနစ် ပုံမှန်ဖြစ်သွားကြောင်း အတည်ပြုခဲ့သည်။
၃။ Local AI setup အတွက် config ထဲမှာ မဟုတ်ဘဲ သီးသန့် Tier 4 Script ထဲတွင်သာ parameter များ ချိန်ညှိခဲ့သည်။

## သင်ခန်းစာ (Learning/Prevention)
- `openclaw.json` ကို ပြင်ဆင်သည့်အခါ တရားဝင် support ပေးထားသော keys များကိုသာ အသုံးပြုရန်။
- မသေချာသော keys များ ထည့်သွင်းမည့်အစား သီးသန့် script များ သို့မဟုတ် environment variables များကို အသုံးပြုရန်။
