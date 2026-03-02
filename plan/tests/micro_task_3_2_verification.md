# Verification Plan: Micro-Task 3.2 (Context Window Management)

## Objective
`ai/custom/n8n/log_chunker.js` ရှိ JavaScript logic သည် n8n Code Node အတွင်း၌ ပေးထားသော logs များထဲမှ Priority logs များကို ခွဲထုတ်နိုင်စွမ်းရှိမရှိနှင့် Token limit အတွင်း ချိန်ညှိနိုင်စွမ်းရှိမရှိကို AIDD (TDD) စံနှုန်းဖြင့် စစ်ဆေးရန်။

## Test Cases
1. **Test Case 1 (Priority Extraction)**: 
   - Input: logs တွင် "ERROR", "DECISION", "GOAL" ပါဝင်သော စာသားများ။
   - Expected Output: အဆိုပါ စာသားများ အားလုံး Output တွင် ပါဝင်ရမည်။
2. **Test Case 2 (Recency Balance)**:
   - Input: General logs အများအပြား (Limit ကျော်လွန်သည်အထိ)။
   - Expected Output: နောက်ဆုံးကျသော General logs များကိုသာ ဦးစားပေး ချန်လှပ်ထားရမည်။
3. **Test Case 3 (Empty/Small Input)**:
   - Input: Logs နည်းပါးခြင်း သို့မဟုတ် မရှိခြင်း။
   - Expected Output: Error မတက်ဘဲ ပုံမှန်အတိုင်း output ထွက်ရမည်။

## Execution (Verification via n8n_tester)
`python3 /usr/lib/node_modules/openclaw/skills/n8n/scripts/n8n_tester.py` ကို အသုံးပြု၍ n8n ပေါ်ရှိ workflow ကို validate လုပ်မည်။
