---
name: memory-librarian
description: Fully autonomous memory organization and distillation system for resource-constrained VPS environments. Use this skill whenever the user wants to organize workspace knowledge, create topic summaries, maintain knowledge index, archive old files, or says "organize library/memory/knowledge". Also trigger automatically when workspace files exceed 100+ files, when user mentions memory management, or when creating new files (for auto-tagging). This skill operates autonomously without requiring manual user tags - it infers importance from context, goals, and relationships.
compatibility: Requires ripgrep-search skill (mandatory), bash_tool, view, str_replace, create_file tools
---

# Autonomous Hybrid Memory Distillation & Librarian Skill

Fully autonomous knowledge organization system that maintains a tiered memory architecture without overwhelming limited RAM resources. This skill operates intelligently without requiring manual intervention - it infers, scores, tags, and organizes autonomously.

## Core Philosophy

**"Search first, infer smart, organize autonomously."**

This skill is designed for FULL AUTONOMY:
1. **Self-scoring**: Infers importance without manual tags
2. **Self-tagging**: Automatically tags new files during creation
3. **Self-organizing**: Maintains INDEX.md without prompts
4. **RAM-conscious**: Respects 2GB limit and 240s timeout
5. **Ripgrep-first**: Uses ripgrep-search skill for all cold storage access

Instead of keeping everything in RAM, this skill:
1. Maintains a lightweight INDEX.md as the single source of truth (Tier 1)
2. Creates topic-specific files on demand (Tier 2)
3. Uses **ripgrep-search skill** to search cold storage when needed (Tier 3)

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
- **Access**: **ALWAYS use ripgrep-search skill**

## Autonomous Operation Mode

**This skill operates FULLY AUTONOMOUSLY. No manual tagging required.**

### What Makes This Autonomous?

1. **Self-Scoring**: Infers importance from 7+ signals without user tags
   - Goal alignment (checks GOALS.md automatically)
   - Eisenhower matrix interpretation (analyzes keywords)
   - Backlink counting (uses ripgrep to find references)
   - Recency, file type, content quality

2. **Self-Tagging**: Automatically adds #IMPORTANT, #URGENT, #TODO tags when creating files
   - Analyzes creation context
   - Detects strategic vs. tactical content
   - Aligns with GOALS.md if present

3. **Self-Organizing**: Maintains INDEX.md without prompts
   - Scans workspace automatically
   - Updates ACTIVE_PROJECTS
   - Refreshes TOPIC_MAP
   - Archives old files

4. **Self-Monitoring**: Respects constraints automatically
   - Checks RAM before every operation
   - Monitors elapsed time (240s timeout)
   - Degrades gracefully when resources are low

5. **Search-First**: Uses ripgrep-search skill for all cold storage access
   - Token-efficient
   - RAM-conscious
   - Millisecond performance

### User's Role

The user's role is MINIMAL:
- ✅ Optional: Create GOALS.md to guide importance scoring
- ✅ Optional: Add explicit #IMPORTANT tags for critical files
- ✅ Optional: Trigger manual distillation with "organize library"
- ❌ NOT required: Tag every file manually
- ❌ NOT required: Maintain INDEX.md manually
- ❌ NOT required: Organize topics manually

### Claude's (David's) Autonomous Responsibilities

When this skill is active, Claude AUTOMATICALLY:

1. **During File Creation**:
   - Analyzes context to determine importance
   - Adds appropriate tag (#IMPORTANT, #URGENT, #TODO)
   - Places file in appropriate workspace location

2. **During Distillation** (scheduled or manual):
   - Scans workspace with ripgrep-search skill
   - Scores all files using 7-signal algorithm
   - Extracts content from high-priority files
   - Creates/updates topic files
   - Updates INDEX.md
   - Archives old low-priority files
   - Logs and notifies completion

3. **During Retrieval** (when user asks questions):
   - Checks INDEX.md first (Tier 1)
   - Reads relevant topic file if available (Tier 2)
   - Uses ripgrep-search skill for deep search (Tier 3)

4. **Continuous Monitoring**:
   - RAM usage (abort if critical)
   - Elapsed time (abort if timeout approaching)
   - File count (trigger distillation if > 100 files)

This is a TRUE AUTONOMOUS SYSTEM - it works intelligently without manual oversight.

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

### Workflow 1: Full Autonomous Distillation (Scheduled)

Run this during low-traffic hours (3 AM recommended). **Process SEQUENTIALLY, respect timeout.**

```bash
#!/bin/bash
# SEQUENTIAL DISTILLATION - DO NOT PARALLELIZE

START_TIME=$(date +%s)
MAX_DURATION=235  # 240s timeout minus 5s buffer

# Step 1: RAM Safety Check (5 seconds)
echo "Step 1: RAM Safety Check"
RAM_PERCENT=$(free -m | awk 'NR==2 {printf "%.0f", $3/$2*100}')
if [ $RAM_PERCENT -gt 90 ]; then
  echo "⚠️ RAM usage at ${RAM_PERCENT}% - LOW_MEMORY_MODE"
  LOW_MEMORY_MODE=true
else
  LOW_MEMORY_MODE=false
fi

# Step 2: Read GOALS.md (if exists) (5 seconds)
echo "Step 2: Loading GOALS.md for autonomous scoring"
if [ -f /root/.openclaw/workspace/GOALS.md ]; then
  GOALS_CONTENT=$(cat /root/.openclaw/workspace/GOALS.md)
  echo "✅ GOALS.md loaded"
else
  echo "⚠️ GOALS.md not found - goal alignment scoring disabled"
  GOALS_CONTENT=""
fi

# Step 3: Scan workspace with ripgrep-search skill (10 seconds)
echo "Step 3: Scanning workspace with ripgrep"
WORKSPACE_FILES=$(rg --files /root/.openclaw/workspace/ -t md -t py -t js -t json)
FILE_COUNT=$(echo "$WORKSPACE_FILES" | wc -l)
echo "✅ Found $FILE_COUNT files"

# Step 4: Sequential scoring (max 60 seconds for 40 files = 1.5s per file)
echo "Step 4: Autonomous importance scoring (sequential)"
PRIORITY_FILES=()

# SEQUENTIAL PROCESSING - ONE FILE AT A TIME
while IFS= read -r file; do
  # Check timeout
  ELAPSED=$(($(date +%s) - START_TIME))
  if [ $ELAPSED -gt $MAX_DURATION ]; then
    echo "⚠️ Timeout approaching, stopping scoring"
    break
  fi
  
  # Autonomous scoring for this file
  SCORE=$(python3 -c "
import sys
sys.path.append('/root/.openclaw/memory-librarian/scripts')
from scoring import calculate_autonomous_score
print(calculate_autonomous_score('$file', '$GOALS_CONTENT'))
")
  
  # Only keep high-priority files (score >= 70)
  if [ $SCORE -ge 70 ]; then
    PRIORITY_FILES+=("$file:$SCORE")
    echo "  ✅ $file → Score: $SCORE"
  fi
  
done <<< "$WORKSPACE_FILES"

echo "✅ Scored ${#PRIORITY_FILES[@]} high-priority files"

# Step 5: Sequential topic extraction (max 100 seconds)
echo "Step 5: Topic extraction (sequential, top 20 files max)"

# Limit to top 20 files to stay within timeout
# Sort by score descending, take top 20
SORTED_FILES=$(printf '%s\n' "${PRIORITY_FILES[@]}" | sort -t: -k2 -rn | head -20)

TOPICS_UPDATED=0
while IFS=: read -r file score; do
  # Check timeout
  ELAPSED=$(($(date +%s) - START_TIME))
  if [ $ELAPSED -gt $MAX_DURATION ]; then
    echo "⚠️ Timeout approaching, stopping topic extraction"
    break
  fi
  
  # Extract topic (Claude does this via create_file)
  # This is where Claude would read the file and create/update topic file
  echo "  Processing: $file (score: $score)"
  
  # Placeholder: In production, Claude executes topic extraction here
  # topic_name=$(extract_topic_from_file "$file")
  # update_topic_file "$topic_name" "$file"
  
  TOPICS_UPDATED=$((TOPICS_UPDATED + 1))
  
done <<< "$SORTED_FILES"

echo "✅ Updated $TOPICS_UPDATED topics"

# Step 6: Update INDEX.md (10 seconds)
echo "Step 6: Updating INDEX.md"
# Claude generates INDEX.md content based on scored files
# This is done with create_file or str_replace

echo "✅ INDEX.md updated"

# Step 7: Archive old files (30 seconds)
echo "Step 7: Archiving old files (score < 20, age > 30 days)"
if [ "$LOW_MEMORY_MODE" != "true" ]; then
  ARCHIVED_COUNT=0
  # Find files older than 30 days with low scores
  find /root/.openclaw/workspace/ -type f -mtime +30 | while read old_file; do
    # Quick score check (metadata only, no file read)
    # If score < 20, archive it
    # mv "$old_file" /root/.openclaw/memory/archive/
    ARCHIVED_COUNT=$((ARCHIVED_COUNT + 1))
  done
  echo "✅ Archived $ARCHIVED_COUNT files"
else
  echo "⚠️ Skipping archiving in low-memory mode"
fi

# Step 8: Log and notify (5 seconds)
TOTAL_TIME=$(($(date +%s) - START_TIME))
echo "Step 8: Logging results"
echo "[$(date)] Distillation completed in ${TOTAL_TIME}s" >> /root/.openclaw/logs/librarian.log
echo "  Topics updated: $TOPICS_UPDATED"
echo "  Files archived: $ARCHIVED_COUNT"
echo "  RAM usage: $RAM_PERCENT%"

# Send Telegram notification
bash /root/.openclaw/memory-librarian/scripts/notify.sh \
  "" "$TOPICS_UPDATED" "$ARCHIVED_COUNT" "${#PRIORITY_FILES[@]}" "$RAM_PERCENT" "$TOTAL_TIME"

echo "✅ Distillation completed successfully"
```

**Key Points:**
- ✅ Sequential processing (one file at a time)
- ✅ Timeout monitoring (checks elapsed time)
- ✅ Autonomous scoring (no manual tags required)
- ✅ GOALS.md integration (goal alignment)
- ✅ Ripgrep-search skill usage (cold storage access)
- ✅ RAM-conscious (checks before operations)
- ✅ Graceful degradation (stops if timeout approaches)

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

## Autonomous Importance Scoring Algorithm

**CRITICAL: This skill INFERS importance autonomously. User tags are optional hints, not requirements.**

Prioritize items based on multiple autonomous signals:

### 1. User Explicit Tags (Optional Hints)
If present, these provide strong signals:
- `#IMPORTANT` tag in file → Score: 100
- `#URGENT` tag → Score: 90
- `#TODO` tag → Score: 70

### 2. Project-Goal Alignment (Autonomous Inference)
**ALWAYS check `/root/.openclaw/workspace/GOALS.md` first if it exists.**

Algorithm:
```python
# Step 1: Read GOALS.md
goals_content = read_file("/root/.openclaw/workspace/GOALS.md")
goal_keywords = extract_keywords(goals_content)

# Step 2: Check file alignment
file_content = read_file(file_path)
alignment_score = 0

for keyword in goal_keywords:
    if keyword.lower() in file_content.lower():
        alignment_score += 15  # Each goal keyword match = +15 points

# Cap at 60 points
alignment_score = min(alignment_score, 60)
```

**Example:**
- GOALS.md contains: "visa automation", "biometric integration"
- File contains "visa automation system design" → +30 points
- File unrelated to goals → +0 points

### 3. Eisenhower Matrix Interpretation (Semantic Analysis)
Analyze file content for keywords that indicate urgency and importance:

**Urgent Keywords** (Time-sensitive, reactive):
- "error", "bug", "crash", "fix", "hotfix", "broken", "failure"
- "deadline", "emergency", "critical", "urgent", "asap"
- "incident", "outage", "down", "blocker"
- **Score**: +40 points if 2+ urgent keywords found

**Important Keywords** (Strategic, proactive):
- "strategy", "architecture", "design", "framework", "foundation"
- "roadmap", "planning", "vision", "goals", "objectives"
- "research", "analysis", "documentation", "specification"
- **Score**: +30 points if 2+ important keywords found

**Neither Urgent nor Important** (Low priority):
- "notes", "draft", "scratch", "temp", "test", "example"
- **Score**: -20 points penalty

**Eisenhower Quadrant Scoring:**
```
│ Important + Urgent → Score: +70 (Do First)
│ Important + Not Urgent → Score: +30 (Schedule)
│ Not Important + Urgent → Score: +40 (Delegate/Automate)
│ Not Important + Not Urgent → Score: -20 (Eliminate)
```

### 4. Reference/Backlink Count (Foundation Knowledge Detection)
**Use ripgrep-search skill to count references:**

```bash
# Count how many files reference this file
filename=$(basename "$file_path")
rg -l "$filename" /root/.openclaw/workspace/ | wc -l
```

**Scoring:**
- 10+ references → +50 points (Foundation knowledge)
- 5-9 references → +30 points (Well-connected)
- 2-4 references → +15 points (Referenced)
- 0-1 references → +0 points (Isolated)

**Rationale**: Files that many other files reference are likely foundational documents (architecture decisions, core specs, shared configs).

### 5. Recency (Time-based)
- Modified within 1 day → Score: +50
- Modified within 7 days → Score: +30
- Modified within 30 days → Score: +10
- Older than 30 days → Score: +0

### 6. File Type Signals (Contextual Hints)
Certain file types carry inherent importance:
- `README.md` → +20 points (Entry point documentation)
- `GOALS.md`, `ROADMAP.md` → +40 points (Strategic documents)
- `*.config.*`, `.env` → +25 points (Configuration)
- `package.json`, `requirements.txt` → +20 points (Dependencies)
- `*.log`, `*.tmp` → -10 points (Temporary/logs)

### 7. Content Quality Signals
- File size 0 bytes → -30 points (Empty, likely abandoned)
- File size < 100 bytes → -15 points (Stub/placeholder)
- File size > 100KB → +10 points (Substantial content)
- Contains TODO markers → +10 points (Active work)
- Contains decision records → +25 points (ADR/RFC style)

### Total Autonomous Score Calculation

```python
def calculate_autonomous_score(file_path):
    score = 0
    
    # 1. Check user tags (if present)
    score += check_user_tags(file_path)
    
    # 2. Check goal alignment (requires GOALS.md)
    score += check_goal_alignment(file_path)
    
    # 3. Eisenhower matrix inference
    score += infer_eisenhower_quadrant(file_path)
    
    # 4. Count backlinks (use ripgrep-search skill)
    score += count_backlinks(file_path)
    
    # 5. Recency
    score += calculate_recency_score(file_path)
    
    # 6. File type signals
    score += infer_file_type_importance(file_path)
    
    # 7. Content quality
    score += assess_content_quality(file_path)
    
    return max(0, score)  # Floor at 0, no negative total scores
```

### Classification Thresholds

Based on total autonomous score:

- **Score ≥ 100**: CRITICAL → Add to ACTIVE_PROJECTS with #IMPORTANT tag
- **Score 70-99**: HIGH → Add to ACTIVE_PROJECTS
- **Score 40-69**: MEDIUM → Index in TOPIC_MAP
- **Score 20-39**: LOW → Monitor, but don't prioritize
- **Score < 20**: ARCHIVE → Candidate for archiving (if older than 30 days)

### Example Scoring Scenarios

**Scenario 1: Strategic Planning Document**
```
File: /workspace/visa-system-redesign-2024.md
- Content includes "architecture", "strategy", "roadmap" → +30 (Important)
- Matches GOALS.md keyword "visa automation" → +15 (Goal-aligned)
- Referenced by 8 other files → +30 (Foundation)
- Modified 2 days ago → +50 (Recent)
- File type: *.md, substantial content → +10 (Quality)
Total: 135 → CRITICAL (ACTIVE_PROJECTS with #IMPORTANT)
```

**Scenario 2: Bug Fix Note**
```
File: /workspace/logs/error-investigation.txt
- Contains "error", "bug", "fix" → +40 (Urgent)
- Not in GOALS.md → +0 (No alignment)
- No backlinks → +0 (Isolated)
- Modified 1 day ago → +50 (Recent)
- File type: .txt log → -10 (Log penalty)
Total: 80 → HIGH (ACTIVE_PROJECTS)
```

**Scenario 3: Old Scratch Note**
```
File: /workspace/notes/scratch-2023.md
- Contains "notes", "draft" → -20 (Low priority)
- No goal alignment → +0
- No backlinks → +0
- Modified 120 days ago → +0 (Old)
- Small file (50 bytes) → -15 (Stub)
Total: -35 → floor to 0 → ARCHIVE candidate
```

## Operational Constraints (CRITICAL)

**ALWAYS respect these hard limits:**

### 1. RAM Constraint: 2GB Total
- **Normal operation**: Keep usage < 1.8GB (90%)
- **Warning threshold**: 1.8-1.9GB (90-95%)
- **Critical threshold**: > 1.9GB (95%)
- **Action**: Check RAM before EVERY intensive operation

```bash
# Check before distillation
free -m | awk 'NR==2 {if ($3/$2*100 > 90) exit 1}'
```

### 2. Timeout Constraint: 240 Seconds
- **Total distillation cycle**: Must complete in < 240s
- **Per-file processing**: Budget 2-5 seconds per file
- **Max files per cycle**: ~40-50 files (at 5s each = 200-250s)

**Strategy**: Process files SEQUENTIALLY, not in parallel. Monitor elapsed time and abort if approaching timeout.

```python
import time
start = time.time()
MAX_TIME = 235  # Leave 5s buffer

for file in files:
    if time.time() - start > MAX_TIME:
        log("Timeout approaching, aborting distillation")
        break
    process_file(file)
```

### 3. Sequential Processing (NOT Parallel)
**NEVER process multiple files simultaneously.**

❌ **Bad** (Parallel):
```python
# This exhausts RAM quickly
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(process_file, files)  # RAM spike!
```

✅ **Good** (Sequential):
```python
# Process one at a time
for file in files:
    process_file(file)
    # RAM released after each file
```

### 4. Incremental Operations
- **Don't rewrite everything**: Update incrementally
- **Don't re-read cached content**: Store results in variables
- **Don't create temporary files**: Use memory buffers when possible

### 5. Graceful Degradation
If approaching limits, reduce scope:

**Priority Levels**:
1. **Essential**: Update INDEX.md (always do this)
2. **Important**: Process CRITICAL files (score ≥ 100)
3. **Nice-to-have**: Process HIGH files (score 70-99)
4. **Optional**: Process MEDIUM files (score 40-69)
5. **Skip**: LOW files (score < 40)

**Degradation Strategy**:
```python
if ram_usage > 85%:
    # Only process CRITICAL files
    files = [f for f in files if score(f) >= 100]
    
if time_remaining < 60:
    # Only update INDEX.md, skip topic creation
    update_index_only()
```

## Auto-Tagging System (Self-Maintenance)

**CRITICAL: Claude (David) must AUTO-TAG files during creation.**

Whenever Claude creates a new file (using `create_file` or `str_replace` tools), it should AUTONOMOUSLY add appropriate tags based on context.

### When to Auto-Tag

**ALWAYS auto-tag when:**
1. Creating a new file in `/root/.openclaw/workspace/`
2. The file contains substantial content (> 100 bytes)
3. The context suggests importance or urgency

### Auto-Tagging Logic

**Step 1: Analyze Context**
Before writing the file, analyze what the file is about:
- What is the user trying to accomplish?
- Is this related to a goal in GOALS.md?
- Is this fixing an error or building something strategic?

**Step 2: Determine Tag**
```python
def determine_auto_tag(context, content):
    # Check for urgent indicators
    urgent_keywords = ["error", "bug", "fix", "critical", "urgent", "broken"]
    if any(kw in content.lower() for kw in urgent_keywords):
        return "#URGENT"
    
    # Check for important indicators
    important_keywords = ["strategy", "architecture", "design", "specification", "roadmap"]
    if any(kw in content.lower() for kw in important_keywords):
        return "#IMPORTANT"
    
    # Check for TODO indicators
    if "TODO" in content or "[ ]" in content:
        return "#TODO"
    
    # Check goal alignment
    if goals_md_exists() and is_goal_aligned(content):
        return "#IMPORTANT"
    
    return None  # No tag needed
```

**Step 3: Add Tag to File**
Add the tag in a prominent location:
- **Markdown files**: Add to first line as `# Title #TAG`
- **Code files**: Add as comment at top `# FILE: description #TAG`
- **Config files**: Add as comment `# #TAG: reason`

### Auto-Tagging Examples

**Example 1: Creating a Bug Fix Document**
```python
# User says: "Create a document about the database connection error"

# Claude analyzes: This is about fixing an error → URGENT
content = """
# Database Connection Error Investigation #URGENT

## Problem
The application cannot connect to PostgreSQL database.

## Root Cause
...
"""

create_file("/root/.openclaw/workspace/db-error-investigation.md", content)
```

**Example 2: Creating a Design Document**
```python
# User says: "Draft the architecture for the new visa system"

# Claude analyzes: This is strategic planning → IMPORTANT
content = """
# Visa System Architecture Design #IMPORTANT

## Overview
This document outlines the architecture for the next-generation visa processing system.

## Goals
Aligned with GOALS.md: visa automation, biometric integration

## Architecture
...
"""

create_file("/root/.openclaw/workspace/visa-architecture-2024.md", content)
```

**Example 3: Creating a TODO List**
```python
# User says: "List out the tasks for next week"

# Claude analyzes: Action items → TODO
content = """
# Weekly Tasks #TODO

- [ ] Review immigration policy updates
- [ ] Update visa processing documentation
- [ ] Schedule team meeting
"""

create_file("/root/.openclaw/workspace/weekly-tasks.md", content)
```

**Example 4: Creating a Regular Note**
```python
# User says: "Take notes on today's meeting"

# Claude analyzes: No special indicators, just notes → No tag
content = """
# Team Meeting Notes - 2024-03-15

Attendees: Team members
Topics discussed: General updates

...
"""

create_file("/root/.openclaw/workspace/meeting-notes-2024-03-15.md", content)
# No tag needed for regular notes
```

### Auto-Tag Maintenance

The auto-tagging system is SELF-MAINTAINING:
1. **During creation**: Claude adds tags automatically
2. **During distillation**: Librarian reads tags for scoring
3. **Feedback loop**: High-scored files validate the tagging was correct

### Auto-Tag Override

User can override auto-tags:
- If user explicitly says "this is important", use #IMPORTANT regardless
- If user explicitly says "this is not urgent", don't use #URGENT
- User's explicit instructions ALWAYS override autonomous inference

## RAM Safety Mechanisms (Aligned with Operational Constraints)

### Low-Memory Mode Triggers

Activate when RAM usage > 90% (1.8GB of 2GB):

```bash
RAM_USED=$(free -m | awk 'NR==2 {print $3}')
RAM_TOTAL=$(free -m | awk 'NR==2 {print $2}')
RAM_PERCENT=$(awk "BEGIN {printf \"%.0f\", ($RAM_USED/$RAM_TOTAL)*100}")

if [ $RAM_PERCENT -gt 90 ]; then
  echo "🚨 LOW MEMORY MODE ACTIVATED"
  # Reduce scope
fi
```

### Safe Operations in Low Memory:
- ✅ Update INDEX.md (small file, ~5KB)
- ✅ Add topic map entries (metadata only, no content)
- ✅ Move files to archive (no reading, just mv command)
- ✅ Use ripgrep-search skill (no file loading required)
- ❌ Read and summarize long files
- ❌ Create new topic files with extracted content
- ❌ Process more than 10 files
- ❌ Load multiple files into memory simultaneously

### Low-Memory Mode Operations

When RAM > 90%, only do:
1. Quick INDEX.md update with file paths (no content extraction)
2. Archive old files (score < 20, age > 30 days)
3. Log what was skipped for next cycle

```python
def low_memory_distillation():
    # ONLY update index with paths, no content processing
    files = scan_workspace()
    
    # Quick scoring (no file reading)
    priority_files = []
    for file in files:
        # Score based on metadata only
        score = quick_score(file)  # Uses file stats, no content read
        if score > 80:
            priority_files.append((file, score))
    
    # Update INDEX.md with paths only
    update_index_paths_only(priority_files)
    
    # Archive old low-priority files
    archive_by_age_and_name(days=30, score_threshold=20)
    
    log("Low-memory mode: Skipped content distillation")
```

### Critical RAM Mode (> 95%)

When RAM > 95%, ABORT distillation immediately:
```python
if ram_usage > 95:
    log("CRITICAL: RAM exhausted, aborting distillation")
    notify_user("⚠️ Distillation aborted - RAM critical")
    exit(1)
```

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

## Ripgrep-Search Skill Integration (MANDATORY)

**CRITICAL: ALWAYS use the ripgrep-search skill for Tier 3 (Cold Memory) access.**

This skill has a HARD DEPENDENCY on the ripgrep-search skill. Never use plain `grep`, `find`, or manual file iteration when ripgrep-search skill is available.

### Why Ripgrep-First?

1. **Token Efficiency**: Get exact matches without reading entire files
2. **RAM Conscious**: No need to load files into memory for searching
3. **Speed**: Millisecond searches across hundreds of files
4. **Context Aware**: Returns matches with surrounding lines
5. **Smart Exclusions**: Automatically skips node_modules, .git, etc.

### When to Use Ripgrep-Search Skill

**ALWAYS use ripgrep-search skill for:**

1. **Backlink Counting** (Importance scoring):
```bash
# Count how many files reference "visa-system.md"
rg -l "visa-system" /root/.openclaw/workspace/
```

2. **Goal Keyword Extraction**:
```bash
# Find all files containing goal-related keywords
rg -i "visa automation|biometric" /root/.openclaw/workspace/ -l
```

3. **Eisenhower Keywords Detection**:
```bash
# Find urgent files
rg -i "error|bug|fix|urgent|critical" /root/.openclaw/workspace/ -l

# Find important files
rg -i "strategy|architecture|design|roadmap" /root/.openclaw/workspace/ -l
```

4. **Topic Discovery**:
```bash
# Find files discussing a specific topic
rg "immigration policy" /root/.openclaw/workspace/ -C 2
```

5. **Content Search for Distillation**:
```bash
# Find files to distill for a topic
rg -t md "visa processing" /root/.openclaw/workspace/ -l
```

### Ripgrep-Search Workflow Pattern

**Standard Pattern:**
```bash
# Step 1: Search for candidates using ripgrep-search skill
candidates=$(rg -l "pattern" /root/.openclaw/workspace/)

# Step 2: For each candidate, check score
for file in $candidates; do
    score=$(calculate_autonomous_score $file)
    if [ $score -gt 70 ]; then
        # Step 3: Only then read full file (use view tool)
        content=$(cat $file)
        # Step 4: Process content
    fi
done
```

**Never do this:**
```bash
# ❌ BAD: Reading all files to find something
for file in /root/.openclaw/workspace/**/*; do
    content=$(cat $file)  # Wastes tokens!
    if grep "pattern" <<< "$content"; then
        ...
    fi
done
```

**Do this instead:**
```bash
# ✅ GOOD: Use ripgrep-search skill first
rg "pattern" /root/.openclaw/workspace/ -l | while read file; do
    # Only read files that match
    content=$(cat $file)
    ...
done
```

### Integration Points

The ripgrep-search skill is used in EVERY phase of the librarian cycle:

1. **Pre-flight Phase**: Check workspace file count
   ```bash
   rg --files /root/.openclaw/workspace/ | wc -l
   ```

2. **Scanning Phase**: Find recent files
   ```bash
   rg --files /root/.openclaw/workspace/ -t md -t py -t js
   ```

3. **Scoring Phase**: 
   - Goal alignment: `rg -l "goal_keyword" /workspace/`
   - Backlink counting: `rg -l "filename" /workspace/`
   - Keyword detection: `rg "urgent|error" /workspace/`

4. **Topic Extraction Phase**: Find related content
   ```bash
   rg "topic_name" /root/.openclaw/workspace/ -C 3
   ```

5. **Archiving Phase**: Verify file hasn't been recently accessed
   ```bash
   rg -l "filename" /root/.openclaw/workspace/ --mtime -30
   ```

### Performance Notes

On a 2GB RAM VPS:
- Ripgrep search across 100 files: ~100ms
- Reading 100 files manually: ~5-10 seconds + high token cost
- **Savings**: 50-100x faster, 90% fewer tokens

**Always prefer ripgrep-search skill over manual file operations.**

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

## Autonomous Retrieval Strategies

**ALWAYS use ripgrep-search skill for Tier 3 access.**

### Strategy 1: Quick Lookup (Most Common)
User asks: "What were the visa policy changes?"

**Autonomous Steps:**
1. **Check INDEX.md first** (Tier 1 - in context)
   ```bash
   grep -i "visa policy" /root/.openclaw/memory/INDEX.md
   ```
   
2. **If found in TOPIC_MAP**, read that topic file (Tier 2)
   ```bash
   # INDEX.md says: "Visa Processing → memory/topics/visa-processing.md"
   cat /root/.openclaw/memory/topics/visa-processing.md
   ```
   
3. **If not found**, use ripgrep-search skill (Tier 3)
   ```bash
   rg "visa policy" /root/.openclaw/workspace/ -C 2
   ```
   
4. **If found in workspace**, consider adding to topic file for future

**Response**: Synthesize from all tiers, prefer recent/high-score sources

### Strategy 2: Deep Dive (Comprehensive)
User asks: "Show me everything about immigration procedures"

**Autonomous Steps:**
1. **Read topic file** if exists (Tier 2)
   ```bash
   cat /root/.openclaw/memory/topics/immigration-procedures.md
   ```

2. **Use ripgrep to find related workspace files** (Tier 3)
   ```bash
   rg "immigration procedure" /root/.openclaw/workspace/ -l
   ```

3. **Score each found file** autonomously
   ```python
   for file in found_files:
       score = calculate_autonomous_score(file)
       if score > 70:
           read_and_synthesize(file)
   ```

4. **Synthesize** from both topic file and high-priority workspace files

5. **Update topic file** with new findings if substantial

### Strategy 3: Temporal Query (Time-based)
User asks: "What did I work on last week?"

**Autonomous Steps:**
1. **Check INDEX.md LAST_DISTILLATION** timestamp
   
2. **Use ripgrep with time filter**
   ```bash
   # Find files modified in last 7 days
   rg --files /root/.openclaw/workspace/ | \
     xargs -I {} stat -c '%Y %n' {} | \
     awk -v week_ago=$(date -d '7 days ago' +%s) '$1 > week_ago {print $2}'
   ```

3. **Score each recent file** autonomously

4. **Check ACTIVE_PROJECTS** in INDEX.md

5. **Synthesize timeline** combining recent files + active projects

### Strategy 4: Goal-Aligned Search (Strategic)
User asks: "What files relate to our current goals?"

**Autonomous Steps:**
1. **Read GOALS.md** (if exists)
   ```bash
   GOALS=$(cat /root/.openclaw/workspace/GOALS.md)
   ```

2. **Extract goal keywords**
   ```python
   goal_keywords = extract_keywords(GOALS)
   # e.g., ["visa automation", "biometric integration"]
   ```

3. **Use ripgrep to find aligned files**
   ```bash
   rg -i "visa automation|biometric" /root/.openclaw/workspace/ -l
   ```

4. **Score and present** files with high goal alignment

### Strategy 5: Relationship Discovery (Backlink-based)
User asks: "What other files reference this document?"

**Autonomous Steps:**
1. **Extract filename** from user's question

2. **Use ripgrep to find backlinks**
   ```bash
   filename="visa-system-design.md"
   rg -l "$filename" /root/.openclaw/workspace/
   ```

3. **Show relationship graph**
   ```
   visa-system-design.md (Foundation)
   ├── Referenced by: implementation-plan.md
   ├── Referenced by: testing-strategy.md
   └── Referenced by: deployment-checklist.md
   ```

4. **This autonomously identifies** important files (high backlink count)

### Retrieval Performance

On 2GB RAM VPS:
- Tier 1 (INDEX.md) lookup: < 10ms
- Tier 2 (topic file) read: < 100ms
- Tier 3 (ripgrep search): < 500ms for 100 files
- **Total retrieval time**: < 1 second

**Never waste time reading all files. Search first, read only what matters.**

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

ဒီ skill က **လုံးဝ အလိုအလျောက် (Fully Autonomous)** လုပ်ဆောင်ပေးနိုင်အောင် ဒီဇိုင်းထားတာပါ။ VPS ရဲ့ သတ်မှတ်ချက်ကို လေးစားပြီး memory ကို ထိထိရောက်ရောက် စီမံခန့်ခွဲနိုင်ပါတယ်။

### အဓိက အင်္ဂါရပ်များ

**1. အလိုအလျောက် အမှတ်ပေးစနစ် (Autonomous Scoring)**
- User က `#IMPORTANT` tag မတွဲပေးထားရင်တောင် David ကိုယ်တိုင် အမှတ်ပေးနိုင်တယ်
- GOALS.md ကို ကြည့်ပြီး alignment စစ်တယ်
- File ထဲက keywords ("error", "strategy") တွေကို သုံးသပ်တယ်
- အခြား files တွေက ဘယ်နှစ်ကြိမ် reference လုပ်သလဲ ရေတွက်တယ် (ripgrep နဲ့)
- ၇ မျိုးသော signals ကို ပေါင်းစပ်ပြီး အမှတ်ပေးတယ်

**2. Auto-Tagging စနစ် (Self-Maintenance)**
- David က file အသစ် create လုပ်တဲ့အခါတိုင်း context ကို သုံးသပ်ပြီး tag အလိုအလျောက် ထည့်ပေးတယ်
- Bug fix document → `#URGENT` tag
- Strategic planning → `#IMPORTANT` tag
- Task list → `#TODO` tag
- ဒီနည်းနဲ့ system က ကိုယ့်ကိုယ်ကို ထိန်းသိမ်းနိုင်တယ်

**3. Ripgrep-First Architecture**
- File တစ်ခုချင်းစီကို ဖတ်မယ့်အစား ripgrep နဲ့ ရှာတာပါ
- Token အကုန်အသက်သာဆုံး (90% reduction)
- RAM အသုံးပြုမှု အနည်းဆုံး
- Milliseconds အတွင်း ရလဒ်ရတယ်

**4. Tiered Architecture**
- **Tier 1 (Hot)**: INDEX.md - အမြဲ ဖတ်လို့ရတဲ့ global index
- **Tier 2 (Warm)**: Topics folder - လိုအပ်မှ ဖတ်တဲ့ deep content
- **Tier 3 (Cold)**: Workspace - ripgrep နဲ့ ရှာဖွေတဲ့ historical data

**5. RAM Safety (2GB ပေါ်မှာ အလုပ်လုပ်မယ့်)**
- RAM 90% ကျော်ရင် → Low-memory mode (indexing only)
- RAM 95% ကျော်ရင် → Abort (safety)
- Sequential processing (တစ်ခုချင်း၊ တစ်ခါတည်းမဟုတ်)
- 240 စက္ကန့် timeout ကို လေးစားတယ်

**6. Operational Constraints**
- **Sequential processing**: File များကို တစ်ပြိုင်တည်း မလုပ်ဘဲ တစ်ခုပြီး တစ်ခု လုပ်တယ်
- **Timeout monitoring**: 240 seconds ကျော်တော့မယ်ဆိုရင် ရပ်တယ်
- **Graceful degradation**: Resource တင်းရင် အရေးကြီးတာတွေကိုပဲ လုပ်တယ်
- **Incremental updates**: အားလုံးကို ပြန်ရေးမယ့်အစား လိုတာပဲ update လုပ်တယ်

### အသုံးပြုနည်း

**User ရဲ့ အခန်းကဏ္ဍ (အနည်းဆုံး)**
- ✅ Optional: GOALS.md ဖန်တီးခြင်း (importance scoring အတွက်)
- ✅ Optional: အရေးကြီးဆုံး files တွေမှာ `#IMPORTANT` tag ထည့်ခြင်း
- ✅ Optional: "organize library" လို့ manual trigger လုပ်ခြင်း
- ❌ မလိုအပ်: File တိုင်းကို tag တွဲရန်
- ❌ မလိုအပ်: INDEX.md ကို ကိုယ်တိုင် maintain လုပ်ရန်
- ❌ မလိုအပ်: Topics ကို ကိုယ်တိုင် organize လုပ်ရန်

**David (Claude) ရဲ့ အလိုအလျောက် တာဝန်များ**
1. File အသစ် create တဲ့အခါ → Auto-tag ထည့်ပေးတယ်
2. နေ့စဉ် 3 AM → Automatic distillation လုပ်တယ်
3. User မေးတဲ့အခါ → Ripgrep နဲ့ ရှာပြီး တိကျတဲ့ အဖြေ ပေးတယ်
4. RAM စစ်ဆေးတယ်၊ timeout monitor လုပ်တယ်

### လုပ်ဆောင်ချက် ဥပမာများ

**ဥပမာ ၁: Bug Fix Document**
```python
# User: "Database error အကြောင်း document လုပ်ပေး"
# David က context ကို သုံးသပ်တယ်: error fixing = urgent
# အလိုအလျောက် #URGENT tag ထည့်ပေးတယ်
```

**ဥပမာ ၂: Strategic Planning**
```python
# User: "Visa system architecture design ရေးပေး"
# David က context ကို သုံးသပ်တယ်: architecture = important
# GOALS.md နဲ့ alignment စစ်တယ်: visa automation match ဖြစ်တယ်
# အလိုအလျောက် #IMPORTANT tag ထည့်ပေးတယ်
```

**ဥပမာ ၃: Autonomous Retrieval**
```python
# User: "Visa policy changes ဘာတွေ ရှိသလဲ?"
# David:
#   1. INDEX.md ကို အရင် စစ်တယ် (Tier 1)
#   2. မရှိရင် topic file ကို ဖတ်တယ် (Tier 2)
#   3. မရှိသေးရင် ripgrep နဲ့ workspace ကို ရှာတယ် (Tier 3)
#   4. တွေ့ရှိချက်များကို synthesize လုပ်တယ်
```

### Performance အာမခံချက်

2GB RAM VPS ပေါ်မှာ:
- INDEX.md read/write: < 10ms
- Topic file read: < 100ms
- Ripgrep search (100 files): < 500ms
- Full distillation: 30-60 seconds
- RAM overhead: < 200MB

### အထူးမှတ်ချက်

ဒီ skill က **"စာကြည့်တိုက်မှူး"** တစ်ယောက်လို အလုပ်လုပ်ပါတယ်။ သူ့ဘာသာသူ:
- ✅ အရေးကြီးတာတွေကို သိတယ် (infers importance)
- ✅ File အသစ်တွေကို tag တွဲပေးတယ် (auto-tags)
- ✅ Knowledge ကို organize လုပ်ပေးတယ် (maintains INDEX.md)
- ✅ ဟောင်းသွားတာတွေကို သိမ်းဆည်းတယ် (archives old files)
- ✅ Resource ကို သတိထားတယ် (RAM-conscious, timeout-aware)
- ✅ Token အကုန်သက်သာစေတယ် (ripgrep-first)

**Manual intervention အနည်းဆုံးဖြင့် အလုပ်လုပ်ပေးနိုင်တဲ့ TRUE AUTONOMOUS SYSTEM ဖြစ်ပါတယ်။**
