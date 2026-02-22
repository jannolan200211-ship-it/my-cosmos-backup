# VPN Business Blueprint: "The Autonomous VPN Agency"

## 1. Branding & Avatar Advice (Branding Concept)
Nolan အတွက် Professional ဆန်ပြီး ယုံကြည်မှုရှိစေမည့် Branding အကြံပြုချက်များ -
- **Name Ideas:** "Nolan VPN", "Cyber Shield VPN", "Ruby Speed VPN", "Aegis Outline".
- **Color Palette:** Deep Blue (#001F3F) နှင့် Gold (#FFD700) - (Trust & Premium) သို့မဟုတ် Teal နှင့် White - (Modern & Fast)။
- **Avatar Concept:** Shield (ဒိုင်း) တစ်ခု သို့မဟုတ် Key (သော့) တစ်ခုကို ကမ္ဘာလုံးပုံစံနှင့် ပေါင်းစပ်ထားသော Minimalist Logo။ မျက်စိအေးပြီး ယုံကြည်ရသော ပုံစံမျိုး ဖြစ်သင့်ပါသည်။

## 2. Infrastructure (VPN Servers)
- **Singapore:** [172.236.147.182] (100GB / 3000 Ks)
- **Japan:** [172.238.20.132] (100GB / 4000 Ks) - *Pending: certSha256*
- **Protocol:** Outline (Shadowsocks)

## 3. Bot Architecture (Triple-Bot System)
1. **Customer Bot (The Salesman):**
   - **Menu:** ဝယ်ယူရန် | သက်တမ်းစစ်ရန် | အသုံးပြုပုံ (Video) | Support ဆက်သွယ်ရန်။
   - **Flow:** Region ရွေး -> ငွေလွှဲ Screenshot ပို့ -> ခဏစောင့် -> Key ရယူ။
2. **Admin Bot (The Controller):**
   - Nolan အတွက်သီးသန့်။ ငွေလွှဲ Notification တက်လာမည်။ [Approve] | [Reject] ခလုတ်များ ပါရှိမည်။
3. **Proxy Support Bot (The Bridge):**
   - Customer က Support နှိပ်လျှင် Nolan ဆီ စာရောက်မည်။ Nolan ပြန်ပို့သောစာသည် Bot အမည်ဖြင့် Customer ဆီ ရောက်မည်။ (Nolan Account အစစ်ကို ဖုံးကွယ်ထားမည်)။

## 4. Automation & Database Logic
- **Key Generation:** Outline API မှတစ်ဆင့် On-the-fly ထုတ်ပေးမည်။
- **Data Cap:** 100GB Limit သတ်မှတ်မည်။
- **Expiration:** ၃ ရက်အလိုတွင် Reminder ပို့မည်။ ရက်ပြည့်လျှင် Server မှ Key ကို အလိုအလျောက် ဖျက်မည်။
- **Daily Report:** ညစဉ် ဝင်ငွေနှင့် User အသစ်စာရင်းကို Nolan ဆီ ပို့မည်။
- **Database (SQLite/PostgreSQL):** User ID, Key, Region, Start/End Date, Payment Status တို့ကို သိမ်းဆည်းမည်။

## 5. Security & Sovereignty
- **Self-Hosted:** ဤစနစ်တစ်ခုလုံးကို Nolan ၏ VPS ပေါ်တွင်သာ Run မည်ဖြစ်သောကြောင့် ဒေတာများ လုံခြုံမှုရှိမည်။
- **Human-in-the-loop:** ငွေဝင်မဝင်ကို Nolan ကိုယ်တိုင် အတည်ပြုမှသာ Key ထုတ်ပေးမည် (လုံခြုံမှုအတွက်)။

---
*Created by David on 2026-02-21*
