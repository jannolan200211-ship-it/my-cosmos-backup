# Context Engineering & Budgeting

## Core Strategy
To maintain VPS stability (2GB RAM) and reduce Cloud AI costs, we follow the "High-Signal, Low-Token" principle.

## Key Rules (from context-fundamentals)
- **Attention Favored Positions:** Place critical instructions at the beginning and end of prompts.
- **Progressive Disclosure:** Load detailed documents only when specifically needed for a task.
- **Context Budgeting:** Trigger compaction/reset when utilization reaches 70-80% (approx 25,000 tokens for our current setup).
- **Informativity over Exhaustiveness:** Prefer smaller high-signal context over large low-signal context.

## Maintenance
- Ko Sai monitors token usage trends during nightly reviews.
- David enforces XML/Markdown sectioning for structural clarity.

## Context Degradation Prevention (from context-degradation)
- **Attention Decay:** Long sessions can lead to "forgetfulness." Trigger manual reset or compaction when the agent starts repeating itself or ignoring instructions.
- **Middle-Loss:** Information in the middle of long prompts is often ignored. Move critical safety rules (Anti-Loop, RAM checks) to the very beginning or end of the context.
- **Noise Cleanup:** Regularly remove redundant tool outputs and error logs to maintain high-signal context.

## Context Compression Strategy (from context-compression)
- **Aggressive Summarization:** Replace long reasoning blocks and tool outputs with single-sentence summaries.
- **Entity Replacement:** Use shorthand or stable identifiers for recurring long names or paths.
- **Instruction Condensing:** Combine similar instructions into a single, high-density rule.
- **History Pruning:** Remove conversational filler and off-topic exchanges during memory flushes.
