# Task EPIC: Telegram Forum Deployment (AI HQ)

## Vision Alignment
Nolan ၏ VPS အေးဂျင့်များကို Telegram Forum Topic များအဖြစ် စနစ်တကျ နေရာချပြီး Gateway တည်ငြိမ်မှုရှိစေရန်။

## Micro-Task Breakdown

### Phase 1: Security & Stability Audit (David's Internal Check)
- [ ] 1.1: Verify `openclaw.json` settings for Telegram Group context.
- [ ] 1.2: Check `ackReactionScope` and `dmScope` to prevent infinite loops in groups.
- [ ] 1.3: Audit Allowed Users list (Confirm only Nolan's ID: 1839077362).

### Phase 2: Forum Structure Creation (Autonomous Deployment)
- [ ] 2.1: Create Forum Topics for the 5 agents:
    - 💼 **Business Expert (Mg Htet)**
    - 🎨 **Creative Lead (Zayar)**
    - 🛠 **Tech Executor (Aung Kyaw)**
    - 🛡 **Infrastructure Guardian (Ko Sai)**
    - ⚙ **Bulk Worker (Local Worker)**
- [ ] 2.2: Set up a **General/Strategy** topic for David.

### Phase 3: Smart Routing Implementation
- [ ] 3.1: Configure Agent-to-Topic mapping (ဘယ် Topic မှာ စာပို့ရင် ဘယ်အေးဂျင့်က ဖြေရမလဲဆိုတာ သတ်မှတ်ခြင်း)။
- [ ] 3.2: Perform a "Low-load Heartbeat Test" to ensure no gateway restarts.

### Phase 4: Final Handover
- [ ] 4.1: Send a welcome message to each topic from the respective agents.
- [ ] 4.2: Deliver a "Stable HQ" report to Nolan.
