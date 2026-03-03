# librarian-usage.md
# Source: /root/.openclaw/workspace/.openclaw/skills/custom-memory-utils/SKILL.md

---
name: librarian-usage
description: Use the Compact Framework and Memory Librarian system for autonomous conversation distillation and workspace organization. Trigger when conversations are long, when Nolan asks for a summary/compaction, or when needing to organize memories into Tier 2 (Warm Memory).
---

# Librarian Skills (Compact Framework)

This system is designed to efficiently distill long Telegram conversations and organize them into structured memory.

## 核心 (Core)
- **Primary Path:** `/root/.openclaw/workspace/.openclaw/skills/custom-memory-utils/`
- **Main Tool:** `compact-framework`
- **Script:** `distill_conversation.py`

## Usage Rules
1. **Search First:** Use `ripgrep` to check if a memory topic already exists before creating a new one.
2. **Resource Aware:** Check VPS RAM before running local AI (qwen-opt). Fallback to Gemini if RAM < 200MB.
3. **80/20 Distillation:** Keep critical decisions, tasks, and #IMPORTANT/#URGENT tags. Discard small talk and noise.
4. **Tiered Storage:**
   - **Tier 1 (Hot):** Update `INDEX.md`
   - **Tier 2 (Warm):** Save to `memory/topics/<topic>.md`

## Trigger Keywords
- "summarize this thread"
- "compact the conversation"
- "save this discussion to memory"
- "librarian skills"

---
*Note: This is a reference guide for Ko Tun to use the system-wide librarian tools.*
