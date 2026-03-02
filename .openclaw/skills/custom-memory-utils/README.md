# Compact Framework Skill

Autonomous conversation distillation system for long Telegram threads. Transforms verbose conversations into structured, searchable Tier 2 (Warm Memory) while preserving 100% of critical decisions, tasks, and metadata.

## Overview

**Problem**: Long Telegram conversations consume excessive tokens (10K-20K per thread) and make it hard to find important decisions.

**Solution**: The Compact Framework distills conversations using an intelligent 4-phase workflow:
1. **Search First** - Find existing memories with ripgrep (95% token savings)
2. **Resource Awareness** - Choose cloud/local AI based on RAM
3. **Distillation Logic** - Apply 80/20 rule intelligently
4. **Multi-layered Storage** - Update Hot/Warm/Cold memory tiers

**Result**: 70-90% compression while preserving 100% of #IMPORTANT/#URGENT items.

---

## Features

✅ **Autonomous Operation** - No manual intervention required
✅ **Token Efficient** - 87-89% token reduction
✅ **RAM Aware** - Adapts to VPS constraints (< 200MB → cloud, > 500MB → local)
✅ **Ripgrep-First** - Searches before reading (50% token savings)
✅ **Structured Output** - Consistent format for easy searching
✅ **Critical Data Preservation** - 100% retention of decisions, tasks, preferences
✅ **Multi-tier Integration** - Works with memory-librarian skill

---

## Installation

### Prerequisites

```bash
# 1. Install ripgrep (required)
apt-get update && apt-get install -y ripgrep

# 2. Verify Python 3.8+
python3 --version

# 3. (Optional) Set up Gemini API for low-RAM mode
export GEMINI_API_KEY="your_api_key_here"
```

### Setup

```bash
# 1. Create directory structure
mkdir -p /root/.openclaw/memory/topics
mkdir -p /root/.openclaw/.signals

# 2. Make scripts executable
chmod +x compact-framework/scripts/*.sh
chmod +x compact-framework/scripts/*.py

# 3. (Optional) Add to PATH
echo 'export PATH=$PATH:/root/.openclaw/skills/compact-framework/scripts' >> ~/.bashrc
source ~/.bashrc
```

---

## Usage

### Automatic Triggering

The skill triggers automatically when:
- Telegram thread exceeds 50+ messages
- User says: "summarize this thread", "compact conversation"
- Context window > 15K tokens
- Thread age > 2 hours without distillation

### Manual Triggering

```bash
# Basic usage
python3 scripts/distill_conversation.py <thread_id> <conversation.json>

# Example
python3 scripts/distill_conversation.py 12345 /tmp/telegram_thread.json
```

### Conversation JSON Format

```json
[
  {
    "sender": "Nolan",
    "content": "Let's fix the database error #IMPORTANT",
    "timestamp": "2024-03-15T14:30:00"
  },
  {
    "sender": "David",
    "content": "I'll investigate the connection pool",
    "timestamp": "2024-03-15T14:31:00"
  }
]
```

---

## How It Works

### Phase 1: Search First (Token Saver)

Before reading anything, use ripgrep to search for existing memories:

```bash
# Search by thread_id
rg "thread_id: 12345" /root/.openclaw/memory/topics/ -l

# Search by topic
rg "topic: database-error" /root/.openclaw/memory/topics/ -l
```

**Benefit**: If memory exists, read only metadata (200 tokens) instead of full conversation (15K tokens).

**Savings**: 95% token reduction

---

### Phase 2: Resource Awareness (VPS Safety)

Check available RAM and select appropriate AI:

| Available RAM | AI Mode | Description |
|---------------|---------|-------------|
| < 200MB | Cloud (Gemini) | Zero local RAM usage |
| 200-500MB | Local Streaming | Process in chunks (~150MB peak) |
| > 500MB | Local Full | Single-pass (~300MB peak) |

```bash
# Check RAM and get AI mode recommendation
bash scripts/ram_check_ai_mode.sh
```

**Benefit**: Never exceeds VPS RAM limits, gracefully falls back to cloud when needed.

---

### Phase 3: Distillation Logic (80/20 Rule)

Extract the 20% of content that contains 80% of value:

**TIER 1: MUST RETAIN** (20% of messages)
- #IMPORTANT, #URGENT, #TODO tags
- Explicit decisions ("We decided...", "Agreed:")
- Task assignments ("You need to...", "[ ] Task")
- User preferences ("I prefer...", "Always...")
- Error resolutions ("Fix was...", "Root cause:")

**TIER 2: CONDITIONAL** (30% of messages)
- Context-setting explanations
- Problem descriptions
- Questions that led to decisions

**TIER 3: DISCARD** (50% of messages)
- Greetings ("Hi", "Thanks", "Sure")
- Repeated questions without progress
- Dead-end discussions
- Acknowledgments ("Ok", "Got it", "👍")

**Example**:
- Input: 150 messages, 15K tokens
- Output: 35 key points, 2K tokens
- **Compression: 87%**, **Preserved: 100% of critical info**

---

### Phase 4: Multi-layered Storage

Update all three memory tiers:

**Tier 1 (Hot): INDEX.md**
- Add link to distilled memory
- Update ACTIVE_PROJECTS or TOPIC_MAP
- ~100 bytes per entry

**Tier 2 (Warm): memory/topics/\*.md**
- Store distilled conversation
- Structured format for easy searching
- ~2-5KB per distillation

**Tier 3 (Cold): openclaw.db**
- Create signal for archiving original
- Can compress/remove original (70-90% space savings)
- Signal file in `.signals/` directory

---

## Output Format

The distilled output follows this structure:

```markdown
# Database Connection Error #IMPORTANT

**Metadata:**
- Topic: database-error
- Thread ID: 12345
- Date: 2024-03-15
- Original Messages: 150 → Distilled: 35
- Compression: 77%

---

## [Core Logic/Decision]

### Key Decisions
- **DECISION #IMPORTANT**: Implement SQLAlchemy connection pooling
  - Context: Connection pool exhausted during peak load
  - Rationale: Prevent connection leaks
  - Timestamp: 2024-03-15 14:45

### Preferences (Nolan)
- Always use connection pooling for database access
- Monitor connection count with Prometheus

---

## [Active Tasks]

- [ ] **Implement SQLAlchemy pool** #URGENT
  - Status: In Progress
  - Assigned: David
  - Deadline: 2024-03-17

- [x] **Identify root cause**
  - Status: Completed
  - Result: Found missing connection.close()

---

## [Next Goals]

### Immediate
1. Deploy connection pool fix to staging
2. Test under load

### Short-term
1. Implement monitoring dashboard
2. Document best practices

---

## [Reference Links]

- Original Thread: `openclaw.db/threads/12345`
- Related: [Database Configuration](database-config.md)
```

---

## Performance

### Token Efficiency

| Operation | Without Compact | With Compact | Savings |
|-----------|----------------|--------------|---------|
| Read thread | 15K tokens | 2K tokens | 87% |
| Search memory | 5K tokens | 200 tokens | 96% |
| **Total** | **20K tokens** | **2.2K tokens** | **89%** |

### RAM Management

| Mode | RAM Usage | Speed | Cost |
|------|-----------|-------|------|
| Cloud (Gemini) | 0MB | Fast | ~$0.001 |
| Local Streaming | 150MB | Medium | Free |
| Local Full | 300MB | Fastest | Free |

### Storage Impact

- Hot (INDEX.md): +100 bytes per entry
- Warm (topics/): +2-5KB per distillation
- Cold (openclaw.db): 70-90% space savings possible

---

## Integration with Memory Librarian

Compact Framework works seamlessly with the memory-librarian skill:

| Aspect | Memory Librarian | Compact Framework |
|--------|-----------------|-------------------|
| **Source** | Workspace files | Telegram conversations |
| **Storage** | Tier 2 (topics/) | Tier 2 (topics/) |
| **Index** | INDEX.md | INDEX.md |
| **Trigger** | "organize library" | "compact conversation" |
| **Scoring** | 7-signal algorithm | Priority classification |

**Complementary**: Use both skills together for complete knowledge management.

---

## Examples

### Example 1: Bug Fix Discussion

**Input**: 150-message thread about PostgreSQL timeout

**Process**:
1. Search First: No existing memory found
2. Resource Check: 380MB available → Local streaming
3. Distillation: Extracted 15 critical messages + 8 decisions + 12 tasks
4. Storage: Created `database-error.md` in topics/

**Output**: 35 key points, 77% compression

---

### Example 2: Feature Planning

**Input**: 80-message thread about new visa processing feature

**Process**:
1. Search First: Found existing `visa-processing.md`
2. Resource Check: 550MB available → Local full
3. Distillation: Extracted 12 decisions + 6 tasks + 4 preferences
4. Storage: Appended to existing `visa-processing.md`

**Output**: 22 key points, 72% compression

---

## Maintenance

### Check Health

```python
# Run health check
python3 scripts/health_check.py

# Output:
# ✅ ripgrep available
# ✅ Memory directories exist
# ✅ INDEX.md valid
# ✅ 15 topic files
# ✅ 3 cleanup signals pending
```

### View Statistics

```bash
# Show distillation stats
python3 scripts/show_stats.py

# Output:
# Total distillations: 47
# Avg compression: 78%
# Total tokens saved: 623K
# Total space saved: 145MB
```

### Cleanup Signals

```bash
# List pending cleanup signals
ls -lh /root/.openclaw/.signals/

# Process signals (compress/archive original conversations)
python3 scripts/process_signals.py
```

---

## Troubleshooting

### Issue: "ripgrep not found"

```bash
apt-get install -y ripgrep
```

### Issue: "Low RAM and no API key"

**Problem**: RAM < 200MB but GEMINI_API_KEY not set

**Solution**:
```bash
# Option 1: Set API key
export GEMINI_API_KEY="your_key"

# Option 2: Free up RAM
# Kill unnecessary processes
# Or wait for RAM to free up
```

### Issue: "Distillation validation failed"

**Problem**: Output missing required sections

**Solution**: Check that conversation has actual content (decisions, tasks). If conversation is just small talk, distillation might not be meaningful.

### Issue: "Emergency distillation used"

**Problem**: Both cloud and local AI failed

**Action**: This is acceptable! Emergency mode uses rule-based extraction and preserves critical messages. Review output to ensure nothing important was missed.

---

## Best Practices

1. **Run distillation regularly**: Don't wait until 500+ messages
2. **Use tags**: Encourage Nolan to tag important items with #IMPORTANT
3. **Monitor RAM**: Keep RAM > 200MB for local processing
4. **Process signals**: Run cleanup periodically to reclaim space
5. **Verify output**: Spot-check distilled content occasionally

---

## မြန်မာဘာသာ အကျဉ်းချုပ်

**Compact Framework** က Telegram thread conversations တွေကို အလွန်ထိရောက်စွာ ချုံ့ပေးတဲ့ autonomous skill ပါ။

**အဓိက အင်္ဂါရပ်များ:**
- 4-phase workflow (Search → Resource → Distill → Store)
- 87-89% token reduction
- RAM-aware (cloud သို့မဟုတ် local ကို အလိုအလျောက် ရွေးချယ်တယ်)
- 100% critical data preservation
- Multi-tier storage integration

**သုံးရတာ လွယ်ကူတယ်:**
1. User: "summarize this thread"
2. Skill က အလိုအလျောက် 4 phases လုပ်တယ်
3. ရလဒ်: 150 messages → 35 key points (77% compression)

**အကျိုးကျေးဇူးများ:**
- Token အများကြီး သက်သာတယ်
- RAM ကို လုံခြုံစွာ စီမံတယ်
- အရေးကြီးတဲ့ အချက်အလက် 100% သိမ်းဆည်းတယ်
- ရှာဖွေရတာ လွယ်ကူတယ် (structured format)

---

## License

MIT License - Free to use and modify

## Support

For issues or questions:
1. Check SKILL.md for detailed documentation
2. Run health check: `python3 scripts/health_check.py`
3. View logs: `tail -f /root/.openclaw/logs/compact-framework.log`
