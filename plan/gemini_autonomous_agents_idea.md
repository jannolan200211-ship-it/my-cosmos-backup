# Task EPIC: Gemini Autonomous Agents (n8n + here.now)

## Vision Alignment
Nolan ၏ လက်ရှိ VPS hardware (2GB RAM) အတွင်း Gemini API ကို အကျိုးရှိရှိ အသုံးပြု၍ ကိုယ်ပိုင် Autonomous Agents များ တည်ဆောက်ရန်။

## Strategy (Method 1)
1. **n8n as the Brain**: Gemini API ကို n8n ၏ "AI Agent" node များတွင် ထည့်သွင်းအသုံးပြုမည်။
2. **Tools Integration**: 
   - Google Search (via Serper/Custom Search API)
   - File Operations (via OpenClaw scripts)
   - Web Scraping (via n8n nodes)
3. **Deployment**: `here.now` ကို အသုံးပြု၍ အေးဂျင့်များ၏ output များကို public dashboard အဖြစ် ချက်ချင်း တင်ဆက်မည်။

## Implementation Plan (Future)
- [ ] Step 1: n8n တွင် Gemini API credentials များ သတ်မှတ်ရန်။
- [ ] Step 2: Google Search tool ကို n8n နှင့် ချိတ်ဆက်ရန်။
- [ ] Step 3: "Memory Distiller" workflow ကို ပထမဆုံး အလိုအလျောက် အေးဂျင့်အဖြစ် စမ်းသပ်ရန်။
- [ ] Step 4: `here.now` သို့ report များ အလိုအလျောက် ပေးပို့ရန်။

## Why Method 1?
- **Low RAM Usage**: အလုပ်များကို API မှတစ်ဆင့်သာ လုပ်ဆောင်သောကြောင့် VPS RAM ကို အနည်းဆုံးသာ အသုံးပြုသည်။
- **Cost Effective**: Gemini API ၏ free tier ကို အသုံးပြုနိုင်သည်။
- **Scalable**: n8n တွင် nodes များ ထပ်တိုးရုံဖြင့် အေးဂျင့်၏ စွမ်းဆောင်ရည်ကို မြှင့်တင်နိုင်သည်။
