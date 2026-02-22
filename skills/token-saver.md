---
name: token-saver
description: Implements the "Early Compact Pattern" to maintain operational awareness and reduce token costs. Use when session sizes approach thresholds, token usage is high, or periodically to summarize long-term memory.
---

# Token Saver (Early Compact Pattern)

This skill ensures the system remains "cost-aware" and sustainable by proactively managing memory size.

## Core Pattern: Early Compact

1. **Monitor**: Check session file sizes and memory line counts using `scripts/monitor_usage.sh`.
2. **Threshold**: 
   - **Green (< 2MB)**: No action needed.
   - **Yellow (2MB - 5MB)**: **Early Compact Triggered**. Summarize older parts of the session or merge daily logs.
   - **Red (> 5MB)**: **Emergency Compact**. Aggressive summarization to prevent token exhaustion.
3. **Action**: 
   - Read the target file.
   - Extract core insights, decisions, and outcomes.
   - Replace the verbose original with the distilled summary.
   - Archive the original if necessary.

## Model Strategy (Tiered Reasoning)

- **Summarization**: Use `gemini-3-flash` (Cheap & Fast).
- **Final Validation**: Use `gemini-3-flash` or `claude-sonnet-4-5` depending on complexity.

## Myanmar Summary Guidelines

အမြဲတမ်း ကုန်ကျစရိတ် (Token) ကို ချွေတာရန် အောက်ပါတို့ကို လုပ်ဆောင်ပါ:
- မလိုအပ်သော နှုတ်ဆက်စကားများကို ဖယ်ထုတ်ပါ။
- ပြီးသွားသော အလုပ်များကို အနှစ်ချုပ်ပါ။
- ရေရှည်မှတ်သားရန် မလိုသော စာသားများကို ဖျက်ပစ်ပါ။
