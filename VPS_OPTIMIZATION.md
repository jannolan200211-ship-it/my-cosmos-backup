# VPS AI Optimization & Memory Management

Nolan ၏ ၂ဂျီဘီ VPS တွင် Local AI မော်ဒယ်များကို အထိရောက်ဆုံး run နိုင်ရန်အတွက် နည်းပညာဆိုင်ရာ မှတ်တမ်းဖြစ်သည်။

## ၁။ KV Cache နှင့် Memory Math
AI Model တစ်ခု Inference ပြုလုပ်စဉ်တွင် မော်ဒယ် Weights များအပြင် **Key-Value (KV) Cache** သည် RAM ကို အဓိက စားသုံးသည်။

**Math Formula (Qwen 2.5 0.5B/1.5B):**
`KV Cache Size ≈ 2 × Context Length × Layers × KV-Heads × Head-Dimension × Bytes-per-Token`

**Optimization Strategy:**
- **Context Length Scaling:** Context Window ကို ၃၂,၇၆၈ မှ ၂,၀၄၈ သို့ လျှော့ချခြင်းဖြင့် RAM သုံးစွဲမှုကို Gigabytes မှ Megabytes သို့ သိသိသာသာ လျှော့ချနိုင်သည်။
- **Quantization:** Memory ထပ်မံချွေတာရန် llama.cpp (သို့မဟုတ်) Ollama backend တွင် အောက်ပါတို့ကို သုံးသင့်သည် -
    - `-ctk q8_0` သို့မဟုတ် `q4_0` (K-cache quantization)
    - `-ctv q8_0` (V-cache quantization)
    - `-fa` (Flash Attention - `-ctv` အတွက် မဖြစ်မနေ လိုအပ်သည်)

## ၂။ ZRAM ပေါင်းစပ်အသုံးပြုခြင်း
- **ZRAM (1GB):** RAM ထဲတွင် ဒေတာများကို ချုံ့၍ သိမ်းဆည်းပေးခြင်းဖြင့် Virtual Capacity ကို တိုးမြှင့်ပေးသည်။
- **ရလဒ်:** အထက်ပါ KV Cache Optimization များနှင့် ပေါင်းစပ်လိုက်လျှင် ၂ဂျီဘီ VPS ပေါ်၌ပင် ၄,၀၉၆ tokens context အထိ စိတ်ချစွာ အသုံးပြုနိုင်သည်။

---
*Added: ၂၀၂၆-၀၂-၂၀ (Technical Knowledge from Nolan)*
