---
name: memory-librarian
description: Automatic memory organization and distillation system for VPS environments. Use this skill whenever the user wants to organize workspace knowledge, create topic summaries, maintain knowledge index, archive old files, or says "organize library/memory/knowledge". Also trigger when workspace files exceed 100+ files or when user mentions memory management, knowledge distillation, or cleanup tasks.
compatibility: Requires ripgrep-search skill, bash_tool, view, str_replace, create_file tools
---

# Hybrid Memory Distillation & Librarian Skill

Intelligent knowledge organization system that maintains a tiered memory architecture without overwhelming limited RAM resources.

## Core Philosophy

**"Search first, index smart, archive cold."**

Instead of keeping everything in RAM, this skill:
1. Maintains a lightweight INDEX.md as the single source of truth (Tier 1)
2. Creates topic-specific files on demand (Tier 2)
3. Uses ripgrep to search cold storage when needed (Tier 3)

## Memory Architecture

### Tier 1: Hot Memory (Always in Context)
- **Location**: `/root/.openclaw/memory/INDEX.md`
- **Purpose**: Global knowledge index, active projects, topic map
- **Size**: Target < 5KB to stay context-friendly
- **Update**: Every distillation cycle

### Tier 2: Warm Memory (Load on Demand)
- **Location**: `/root/.openclaw/memory/topics/*.md`
- **Purpose**: Deep dives into specific topics
- **Size**: Each file < 50KB
- **Access**: Read with `view` tool when topic is discussed

### Tier 3: Cold Memory (Search on Demand)
- **Location**: `/root/.openclaw/workspace/**/*`
- **Purpose**: Historical logs, old documents, archived data
- **Size**: Unlimited
- **Access**: Search with ripgrep-search skill

## Pre-flight Checklist

Before running distillation, verify these requirements:

```bash
# 1. Check RAM availability
free -m | awk 'NR==2 {printf "RAM: %.1f%% used
", $3/$2*100}'

# 2. Verify ripgrep is available
rg --version || apt-get install -y ripgrep

# 3. Ensure directory structure exists
mkdir -p /root/.openclaw/memory/topics
mkdir -p /root/.openclaw/memory/archive
mkdir -p /root/.openclaw/logs

# 4. Check if INDEX.md exists, create if not
if [ ! -f /root/.openclaw/memory/INDEX.md ]; then
  cat > /root/.openclaw/memory/INDEX.md << 'EOF'
# 📌 GLOBAL_KNOWLEDGE_INDEX

Last Updated: $(date '+%Y-%m-%d %H:%M:%S')

## 🔥 ACTIVE_PROJECTS
<!-- Current tasks and ongoing work -->

## 📂 TOPIC_MAP
<!-- Topic Name -> File Path mappings -->

## ⏱️ LAST_DISTILLATION
<!-- Timestamp of last librarian run -->

EOF
fi
```

## INDEX.md Structure

The INDEX.md follows a strict format for consistency:

```markdown
# 📌 GLOBAL_KNOWLEDGE_INDEX

Last Updated: 2024-03-15 14:30:00

## 🔥 ACTIVE_PROJECTS

### Project: Visa Application System Upgrade
- **Status**: In Progress
- **Priority**: #IMPORTANT
- **Files**: 
  - `/root/.openclaw/workspace/visa-upgrade/requirements.md`
  - `/root/.openclaw/workspace/visa-upgrade/implementation.md`
- **Last Modified**: 2024-03-14
- **Summary**: Upgrading online visa application portal with new biometric features

### Project: Monthly Immigration Report
- **Status**: Pending
- **Priority**: Medium
- **Due**: 2024-03-20
- **Summary**: Compile statistics for Q1 2024

## 📂 TOPIC_MAP

- **Immigration Policies** → `/root/.openclaw/memory/topics/immigration-policies.md` (Last: 2024-03-10)
- **Visa Processing** → `/root/.openclaw/memory/topics/visa-processing.md` (Last: 2024-03-12)
- **Office Procedures** → `/root/.openclaw/memory/topics/office-procedures.md` (Last: 2024-03-05)
- **Technical Documentation** → `/root/.openclaw/memory/topics/technical-docs.md` (Last: 2024-03-15)

## ⏱️ LAST_DISTILLATION

- **Date**: 2024-03-15 03:00:00
- **Duration**: 45 seconds
- **Topics Updated**: 2
- **Files Archived**: 5
- **RAM Usage**: 1.2GB / 2.0GB (60%)
```

## Distillation Workflows

### Workflow 1: Full Distillation (Scheduled)

Run this during low-traffic hours (3 AM recommended):

```bash
# Step 1: RAM Safety Check
RAM_PERCENT=$(free -m | awk 'NR==2 {printf "%.0f", $3/$2*100}')
if [ $RAM_PERCENT -gt 90 ]; then
  echo "⚠️ RAM usage at ${RAM_PERCENT}% - switching to LOW_MEMORY_MODE"
  LOW_MEMORY_MODE=true
else
  LOW_MEMORY_MODE=false
fi

# Step 2: Scan workspace for recent activity
echo "🔍 Scanning workspace for recent changes..."
rg --files /root/.openclaw/workspace/ --mtime -7 > /tmp/recent_files.txt

# Step 3: Extract important keywords and topics
# Use ripgrep to find #IMPORTANT tags
rg -l "#IMPORTANT" /root/.openclaw/workspace/ > /tmp/priority_files.txt

# Step 4: Identify topics for extraction
# This is where Claude steps in to:
# - Read priority files
# - Extract key facts
# - Categorize by topic
# - Update or create topic files

# Step 5: Update INDEX.md
# - Refresh ACTIVE_PROJECTS
# - Update TOPIC_MAP
# - Record LAST_DISTILLATION timestamp

# Step 6: Archive old files
find /root/.openclaw/workspace/ -type f -mtime +30 -exec mv {} /root/.openclaw/memory/archive/ \;

# Step 7: Log results
echo "[$(date)] Distillation completed" >> /root/.openclaw/logs/librarian.log
```

### Workflow 2: Quick Index Update (Manual)

When user says "organize library" or "update index":

```bash
# Step 1: Read current INDEX.md
# Step 2: Scan for new files in workspace
# Step 3: Add new entries to TOPIC_MAP
# Step 4: Don't do full summarization (save RAM)
# Step 5: Report what was added
```

### Workflow 3: Topic Extraction (On-demand)

When discussing a new topic extensively:

```bash
# Step 1: Detect topic from conversation context
# Step 2: Search workspace for related files
rg -i "topic_keyword" /root/.openclaw/workspace/ -l

# Step 3: Create new topic file
cat > /root/.openclaw/memory/topics/new-topic.md << EOF
# Topic: [Topic Name]

Created: $(date)
Related Files: [file list]

## Key Points
- [Extracted fact 1]
- [Extracted fact 2]

## References
- [Source file paths]
EOF

# Step 4: Add to INDEX.md TOPIC_MAP
```

## Importance Scoring Algorithm

Prioritize items based on:

1. **User Explicit Tags** (Highest priority)
   - `#IMPORTANT` tag in file → Score: 100
   - `#URGENT` tag → Score: 90
   - `#TODO` tag → Score: 70

2. **Recency** (Time-based)
   - Modified within 1 day → Score: 50
   - Modified within 7 days → Score: 30
   - Modified within 30 days → Score: 10

3. **Access Frequency** (Usage-based)
   - Accessed 10+ times → Score: 40
   - Accessed 5-9 times → Score: 20
   - Accessed 1-4 times → Score: 5

**Total Score = Tag Score + Recency Score + Frequency Score**

Files with scores > 80 go into ACTIVE_PROJECTS.
Files with scores 40-80 get indexed in TOPIC_MAP.
Files with scores < 40 can be archived after 30 days.

## RAM Safety Mechanisms

### Low-Memory Mode Triggers

Activate when RAM usage > 90% (1.8GB of 2GB):

```bash
if [ $RAM_USAGE -gt 1800 ]; then
  echo "🚨 LOW MEMORY MODE ACTIVATED"
  # Skip summarization
  # Only update index with file paths
  # Defer distillation to next cycle
  # Archive aggressively
fi
```

### Safe Operations in Low Memory:
- ✅ Update INDEX.md (small file)
- ✅ Add topic map entries (metadata only)
- ✅ Move files to archive (no reading)
- ❌ Read and summarize long files
- ❌ Create new topic files with content
- ❌ Extract facts from multiple files

## Trigger Mechanisms

### Automatic Trigger (Cron Job)

Add to crontab:
```cron
# Run librarian at 3 AM daily
0 3 * * * /usr/bin/python3 /root/.openclaw/memory-librarian/scripts/distill.py >> /root/.openclaw/logs/librarian.log 2>&1
```

### Manual Trigger (User Command)

Phrases that should trigger this skill:
- "organize library"
- "organize memory"
- "update knowledge index"
- "distill workspace"
- "clean up old files"
- "what do I have in my memory?"
- "show me the topic map"

### Auto-Trigger Conditions

Activate automatically when:
- Workspace contains 100+ files
- No distillation in past 48 hours
- User mentions "I can't find" or "where did I put"

## Distillation Operations

### Operation 1: Summarization

For long documents (> 10KB):
```python
# Read file
content = read_file(path)

# Extract key points
summary = """
Title: [Document title]
Date: [Creation date]
Key Facts:
- [Fact 1]
- [Fact 2]
- [Fact 3]

Decisions Made:
- [Decision 1]

Action Items:
- [Action 1]
"""

# Save to topic file or INDEX.md
```

### Operation 2: Fact Extraction

Extract structured data:
```python
# Search patterns
patterns = [
    r'phone:\s*(\d{3}-\d{3}-\d{4})',
    r'email:\s*(\S+@\S+)',
    r'deadline:\s*(\d{4}-\d{2}-\d{2})',
    r'decision:\s*(.+)',
]

facts = extract_facts(content, patterns)
add_to_index(facts)
```

### Operation 3: Merging Duplicates

When multiple files discuss same topic:
```bash
# Find related files
rg -l "visa processing" /root/.openclaw/workspace/

# Read and merge key points
# Create unified topic file
# Archive original files with reference
```

### Operation 4: Archiving

Move old, low-priority files:
```bash
# Archive files older than 30 days with score < 40
find /root/.openclaw/workspace/ -type f -mtime +30 -exec \
  python3 -c "import sys; score=calculate_score(sys.argv[1]); sys.exit(0 if score < 40 else 1)" {} \; \
  -exec mv {} /root/.openclaw/memory/archive/ \;
```

## Integration with Ripgrep Skill

The librarian relies heavily on ripgrep for cold storage access:

```bash
# Before distillation: search for candidates
rg --files /root/.openclaw/workspace/ | \
  xargs -I {} stat -c '%Y %n' {} | \
  sort -rn | head -20

# During topic creation: find related content
rg "immigration policy" /root/.openclaw/workspace/ -C 2

# For retrieval: search across all tiers
# Tier 1: grep INDEX.md
# Tier 2: grep memory/topics/*.md
# Tier 3: rg workspace/
```

## Output & Notifications

### Log File Format

`/root/.openclaw/logs/librarian.log`:
```
[2024-03-15 03:00:00] Distillation started
[2024-03-15 03:00:05] RAM check: 1.2GB / 2.0GB (60%) - OK
[2024-03-15 03:00:10] Scanned 145 files in workspace
[2024-03-15 03:00:20] Found 3 files with #IMPORTANT tag
[2024-03-15 03:00:30] Created topic: technical-documentation.md
[2024-03-15 03:00:35] Updated topic: visa-processing.md
[2024-03-15 03:00:40] Archived 5 files (older than 30 days)
[2024-03-15 03:00:45] Updated INDEX.md
[2024-03-15 03:00:45] Distillation completed (45s)
[2024-03-15 03:00:46] Notification sent to Telegram
```

### User Notification (Telegram)

Send concise summary:
```
📚 Library Organized (3:00 AM)
✅ 2 Topics Updated
📁 5 Files Archived
🔥 3 Active Projects
💾 RAM: 60% (Safe)
⏱️ Time: 45s
```

Telegram notification script location: `/root/.openclaw/memory-librarian/scripts/notify.sh`

## Example Workflow: Complete Distillation Cycle

```bash
# 1. Pre-flight checks
bash /root/.openclaw/memory-librarian/scripts/check_ram.sh

# 2. Start distillation
python3 /root/.openclaw/memory-librarian/scripts/distill.py

# This script will:
# - Read INDEX.md
# - Scan workspace with ripgrep
# - Calculate importance scores
# - Update/create topic files
# - Archive old files
# - Update INDEX.md
# - Log results
# - Send notification

# 3. Verify
cat /root/.openclaw/memory/INDEX.md
ls -lh /root/.openclaw/memory/topics/
tail /root/.openclaw/logs/librarian.log
```

## Retrieval Strategies

### Strategy 1: Quick Lookup
User asks: "What were the visa policy changes?"

1. Search INDEX.md first for active projects
2. If not found, check TOPIC_MAP for relevant topic file
3. Read that topic file from Tier 2
4. If still not found, use ripgrep on cold storage (Tier 3)

### Strategy 2: Deep Dive
User asks: "Show me everything about immigration procedures"

1. Read `/root/.openclaw/memory/topics/immigration-procedures.md`
2. Use ripgrep to find related workspace files
3. Synthesize from both sources
4. Optionally update topic file with new findings

### Strategy 3: Temporal Query
User asks: "What did I work on last week?"

1. Use INDEX.md LAST_DISTILLATION timestamp as reference
2. Search workspace for files modified in that range
3. Check ACTIVE_PROJECTS for ongoing work
4. Synthesize timeline

## Edge Cases & Error Handling

### Case 1: INDEX.md Corrupted
```bash
# Detect: Can't parse INDEX.md
# Action: Create backup, regenerate from topics/
mv INDEX.md INDEX.md.backup
python3 /root/.openclaw/memory-librarian/scripts/rebuild_index.py
```

### Case 2: RAM Exhaustion During Distillation
```bash
# Detect: RAM > 95%
# Action: Abort distillation, log warning, notify user
echo "CRITICAL: RAM exhausted during distillation" >> /root/.openclaw/logs/librarian.log
bash /root/.openclaw/memory-librarian/scripts/notify.sh "⚠️ Distillation aborted - RAM critical"
```

### Case 3: Topic File Conflict
```bash
# Detect: Two processes trying to write same topic file
# Action: Use file locking
flock /tmp/librarian.lock -c "python3 update_topic.py"
```

### Case 4: Workspace Overwhelmed (500+ files)
```bash
# Detect: File count exceeds threshold
# Action: Aggressive archiving + warning
if [ $(find /root/.openclaw/workspace -type f | wc -l) -gt 500 ]; then
  echo "WARNING: 500+ files detected, aggressive archiving triggered"
  # Archive anything older than 14 days (instead of 30)
  find /root/.openclaw/workspace/ -type f -mtime +14 -exec mv {} /root/.openclaw/memory/archive/ \;
fi
```

## Performance Benchmarks

Target performance on 2GB RAM VPS:

- **INDEX.md read/write**: < 10ms
- **Topic file creation**: < 100ms
- **Workspace scan (100 files)**: < 2s
- **Full distillation (100 files)**: < 60s
- **RAM overhead**: < 200MB during operation
- **Archive operation**: < 5s for 20 files

## Best Practices

1. **Keep INDEX.md Lean**: Never exceed 10KB. Move details to topic files.
2. **One Topic per File**: Don't mix concepts in topic files.
3. **Archive Aggressively**: Better to archive and retrieve than to clutter.
4. **Use Tags**: Encourage user to add `#IMPORTANT` tags to critical files.
5. **Regular Distillation**: Daily runs keep the system healthy.
6. **Monitor RAM**: Always check before intensive operations.
7. **Incremental Updates**: Don't rewrite everything, update incrementally.

## Maintenance Commands

```bash
# Check librarian health
python3 /root/.openclaw/memory-librarian/scripts/health_check.py

# Manual distillation
python3 /root/.openclaw/memory-librarian/scripts/distill.py --force

# Rebuild index from scratch
python3 /root/.openclaw/memory-librarian/scripts/rebuild_index.py

# Show statistics
python3 /root/.openclaw/memory-librarian/scripts/stats.py

# Clear old archives (older than 90 days)
find /root/.openclaw/memory/archive/ -type f -mtime +90 -delete
```

## မြန်မာဘာသာ မှတ်ချက်

ဒီ skill က VPS ရဲ့ သတ်မှတ်ချက်ကို လေးစားပြီး ဒီဇိုင်းထားတာပါ။ RAM 2GB ပဲရှိတဲ့ စက်မှာ memory ကို ထိထိရောက်ရောက် စီမံခန့်ခွဲဖို့ အောက်ပါ နည်းလမ်းတွေကို သုံးထားပါတယ်-

1. **Tiered Architecture**: အရာတိုင်းကို RAM မှာ မထားဘု၊ လိုအပ်မှ ဖတ်တာပါ။
2. **Ripgrep Integration**: File system တစ်ခုလုံးကို မဖတ်ဘဲ လိုတာကိုပဲ ရှာတာပါ။
3. **Smart Archiving**: ဟောင်းသွားတဲ့ ဖိုင်တွေကို အလိုအလျောက် သိမ်းထားတာပါ။
4. **Low-Memory Mode**: RAM တင်းတဲ့အခါ လုပ်ငန်းစဉ်ကို လျှော့ချတာပါ။

ဒီ system က "စာကြည့်တိုက်မှူး" လိုမျိုး အလုပ်လုပ်ပါတယ်။ သင့်ရဲ့ ဖိုင်တွေ၊ မှတ်တမ်းတွေကို အလိုအလျောက် စုစည်းပြီး ရှာချင်တဲ့အခါ ချက်ချင်း ရနိုင်အောင် စီစဉ်ပေးပါတယ်။
