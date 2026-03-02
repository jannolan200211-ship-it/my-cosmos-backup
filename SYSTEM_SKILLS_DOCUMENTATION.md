# OpenClaw System Skills Documentation

This document contains a comprehensive list of all skills available in the OpenClaw system, including their status, descriptions, and sources.

## 📊 System Skills Overview

| Status | Skill Name | Description | Source |
| :--- | :--- | :--- | :--- |
| ❌ Missing | **1password** | Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in (single or multi-account), or reading/injecting/running secrets via op. | openclaw-bundled |
| ❌ Missing | **apple-notes** | Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, and export notes). Use when a user asks OpenClaw to add a note, list notes, search notes, or manage note folders. | openclaw-bundled |
| ❌ Missing | **apple-reminders** | Manage Apple Reminders via remindctl CLI (list, add, edit, complete, delete). Supports lists, date filters, and JSON/plain output. | openclaw-bundled |
| ❌ Missing | **bear-notes** | Create, search, and manage Bear notes via grizzly CLI. | openclaw-bundled |
| ❌ Missing | **blogwatcher** | Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI. | openclaw-bundled |
| ❌ Missing | **blucli** | BluOS CLI (blu) for discovery, playback, grouping, and volume. | openclaw-bundled |
| ❌ Missing | **bluebubbles** | Use when you need to send or manage iMessages via BlueBubbles (recommended iMessage integration). Calls go through the generic message tool with channel="bluebubbles". | openclaw-bundled |
| ❌ Missing | **camsnap** | Capture frames or clips from RTSP/ONVIF cameras. | openclaw-bundled |
| ✅ Ready | **clawhub** | Use the ClawHub CLI to search, install, update, and publish agent skills from clawhub.com. Use when you need to fetch new skills on the fly, sync installed skills to latest or a specific version, or publish new/updated skill folders with the npm-installed clawhub CLI. | openclaw-bundled |
| ❌ Missing | **coding-agent** | Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. Use when: (1) building/creating new features or apps, (2) reviewing PRs (spawn in temp dir), (3) refactoring large codebases, (4) iterative coding that needs file exploration. NOT for: simple one-liner fixes (just edit), reading code (use read tool), thread-bound ACP harness requests in chat (for example spawn/run Codex or Claude Code in a Discord thread; use sessions_spawn with runtime:"acp"), or any work in ~/clawd workspace (never spawn agents here). Requires a bash tool that supports pty:true. | openclaw-bundled |
| ❌ Missing | **discord** | Discord ops via the message tool (channel=discord). | openclaw-bundled |
| ❌ Missing | **eightctl** | Control Eight Sleep pods (status, temperature, alarms, schedules). | openclaw-bundled |
| ✅ Ready | **gemini** | Gemini CLI for one-shot Q&A, summaries, and generation. | openclaw-bundled |
| ✅ Ready | **gh-issues** | Fetch GitHub issues, spawn sub-agents to implement fixes and open PRs, then monitor and address PR review comments. Usage: /gh-issues [owner/repo] [--label bug] [--limit 5] [--milestone v1.0] [--assignee @me] [--fork user/repo] [--watch] [--interval 5] [--reviews-only] [--cron] [--dry-run] [--model glm-5] [--notify-channel -1002381931352] | openclaw-bundled |
| ❌ Missing | **gifgrep** | Search GIF providers with CLI/TUI, download results, and extract stills/sheets. | openclaw-bundled |
| ✅ Ready | **github** | GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries. Use when: (1) checking PR status or CI, (2) creating/commenting on issues, (3) listing/filtering PRs or issues, (4) viewing run logs. NOT for: complex web UI interactions requiring manual browser flows (use browser tooling when available), bulk operations across many repos (script with gh api), or when gh auth is not configured. | openclaw-bundled |
| ✅ Ready | **gog** | Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. | openclaw-bundled |
| ❌ Missing | **goplaces** | Query Google Places API (New) via the goplaces CLI for text search, place details, resolve, and reviews. Use for human-friendly place lookup or JSON output for scripts. | openclaw-bundled |
| ✅ Ready | **healthcheck** | Host security hardening and risk-tolerance configuration for OpenClaw deployments. Use when a user asks for security audits, firewall/SSH/update hardening, risk posture, exposure review, OpenClaw cron scheduling for periodic checks, or version status checks on a machine running OpenClaw (laptop, workstation, Pi, VPS). | openclaw-bundled |
| ❌ Missing | **himalaya** | CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language). | openclaw-bundled |
| ❌ Missing | **imsg** | iMessage/SMS CLI for listing chats, history, and sending messages via Messages.app. | openclaw-bundled |
| ✅ Ready | **mcporter** | Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. | openclaw-bundled |
| ❌ Missing | **model-usage** | Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar, or when you need a scriptable per-model summary from codexbar cost JSON. | openclaw-bundled |
| ❌ Missing | **nano-banana-pro** | Generate or edit images via Gemini 3 Pro Image (Nano Banana Pro). | openclaw-bundled |
| ❌ Missing | **nano-pdf** | Edit PDFs with natural-language instructions using the nano-pdf CLI. | openclaw-bundled |
| ❌ Missing | **notion** | Notion API for creating and managing pages, databases, and blocks. | openclaw-bundled |
| ❌ Missing | **obsidian** | Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. | openclaw-bundled |
| ❌ Missing | **openai-image-gen** | Batch-generate images via OpenAI Images API. Random prompt sampler + `index.html` gallery. | openclaw-bundled |
| ❌ Missing | **openai-whisper** | Local speech-to-text with the Whisper CLI (no API key). | openclaw-bundled |
| ❌ Missing | **openai-whisper-api** | Transcribe audio via OpenAI Audio Transcriptions API (Whisper). | openclaw-bundled |
| ❌ Missing | **openhue** | Control Philips Hue lights and scenes via the OpenHue CLI. | openclaw-bundled |
| ❌ Missing | **oracle** | Best practices for using the oracle CLI (prompt + file bundling, engines, sessions, and file attachment patterns). | openclaw-bundled |
| ❌ Missing | **ordercli** | Foodora-only CLI for checking past orders and active order status (Deliveroo WIP). | openclaw-bundled |
| ❌ Missing | **peekaboo** | Capture and automate macOS UI with the Peekaboo CLI. | openclaw-bundled |
| ❌ Missing | **sag** | ElevenLabs text-to-speech with mac-style say UX. | openclaw-bundled |
| ✅ Ready | **session-logs** | Search and analyze your own session logs (older/parent conversations) using jq. | openclaw-bundled |
| ❌ Missing | **sherpa-onnx-tts** | Local text-to-speech via sherpa-onnx (offline, no cloud) | openclaw-bundled |
| ✅ Ready | **skill-creator** | Create or update AgentSkills. Use when designing, structuring, or packaging skills with scripts, references, and assets. | openclaw-bundled |
| ❌ Missing | **slack** | Use when you need to control Slack from OpenClaw via the slack tool, including reacting to messages or pinning/unpinning items in Slack channels or DMs. | openclaw-bundled |
| ❌ Missing | **songsee** | Generate spectrograms and feature-panel visualizations from audio with the songsee CLI. | openclaw-bundled |
| ❌ Missing | **sonoscli** | Control Sonos speakers (discover/status/play/volume/group). | openclaw-bundled |
| ❌ Missing | **spotify-player** | Terminal Spotify playback/search via spogo (preferred) or spotify_player. | openclaw-bundled |
| ❌ Missing | **summarize** | Summarize or extract text/transcripts from URLs, podcasts, and local files (great fallback for “transcribe this YouTube/video”). | openclaw-bundled |
| ❌ Missing | **things-mac** | Manage Things 3 via the `things` CLI on macOS (add/update projects+todos via URL scheme; read/search/list from the local Things database). Use when a user asks OpenClaw to add a task to Things, list inbox/today/upcoming, search tasks, or inspect projects/areas/tags. | openclaw-bundled |
| ✅ Ready | **tmux** | Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. | openclaw-bundled |
| ❌ Missing | **trello** | Manage Trello boards, lists, and cards via the Trello REST API. | openclaw-bundled |
| ✅ Ready | **video-frames** | Extract frames or short clips from videos using ffmpeg. | openclaw-bundled |
| ❌ Missing | **voice-call** | Start voice calls via the OpenClaw voice-call plugin. | openclaw-bundled |
| ❌ Missing | **wacli** | Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI (not for normal user chats). | openclaw-bundled |
| ✅ Ready | **weather** | Get current weather and forecasts via wttr.in or Open-Meteo. Use when: user asks about weather, temperature, or forecasts for any location. NOT for: historical weather data, severe weather alerts, or detailed meteorological analysis. No API key needed. | openclaw-bundled |
| ❌ Missing | **xurl** | A CLI tool for making authenticated requests to the X (Twitter) API. Use this skill when you need to post tweets, reply, quote, search, read posts, manage followers, send DMs, upload media, or interact with any X API v2 endpoint. | openclaw-bundled |

## 🛠️ Custom Skills (Workspace Specific)

These are specialized skills developed specifically for this workspace.

### 1. compact-framework (Custom Memory Utils)
- **Path:** `/root/.openclaw/workspace/.openclaw/skills/custom-memory-utils/`
- **Description:** Autonomous conversation distillation system for long Telegram threads.
- **Key Features:** Search-first approach, RAM-aware processing, 80/20 distillation logic.

---

## 📄 Original Custom Skill Definition (compact-framework)

```markdown
---
name: compact-framework
description: Autonomous conversation distillation system for long Telegram threads. Use this skill when Telegram conversations exceed 50+ messages, when user says "summarize this thread", "compact the conversation", or "save this discussion to memory". Also triggers automatically when context window is filling up (>15K tokens). Distills conversations into Tier 2 (Warm Memory) while preserving critical decisions, tasks, and metadata. Uses ripgrep-first approach for token efficiency and RAM-aware processing for VPS safety.
compatibility: Requires ripgrep-search skill (mandatory), memory-librarian skill (for storage integration), bash_tool, view, str_replace, create_file tools
---

# Compact Framework: Autonomous Conversation Distillation

Ultra-efficient system for distilling long Telegram thread conversations into structured, searchable Tier 2 (Warm Memory) while maintaining critical logic and metadata.

## Core Philosophy

**"Search first, check resources, distill smart, store tiered."**

This skill operates in 4 distinct phases:
1. **Search First** - Use ripgrep to find existing memories (50% token savings)
2. **Resource Awareness** - Check RAM, choose appropriate AI model
3. **Distillation Logic** - Apply 80/20 rule intelligently
4. **Multi-layered Storage** - Update Hot/Warm/Cold memory tiers

## Use Cases

**Primary Triggers:**
- Telegram thread exceeds 50+ messages
- User says: "summarize this thread", "compact the conversation", "save discussion"
- Context window approaching limit (>15K tokens)
- Before starting new conversation phase
- When switching topics in long thread

**Autonomous Triggers:**
- Message count > 100 in current thread
- Token usage > 15,000 in current context
- Thread age > 2 hours without distillation
- Before running intensive operations (needs context space)

## Skill Architecture

### Integration with Memory Librarian

This skill is a **specialized companion** to the memory-librarian skill:

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **memory-librarian** | Organizes workspace files | File-based knowledge |
| **compact-framework** | Distills conversations | Telegram thread history |

**Storage alignment:**
- Both use same Tier 2 location: `/root/.openclaw/memory/topics/`
- Both update same INDEX.md: `/root/.openclaw/memory/INDEX.md`
- Both follow same importance scoring principles

### Conversation vs File Knowledge

**Conversations** (compact-framework):
- Ephemeral, time-sensitive discussions
- Task decisions, preferences, instructions
- Stored by thread_id and topic

**Files** (memory-librarian):
- Persistent documents, code, configs
- Long-term reference material
- Stored by topic and importance

---

## Phase 1: Search First (Token Saver)

**Goal: Avoid reading full conversations if memory already exists.**

### Step 1.1: Identify Thread Context

Extract key metadata from current conversation:
```python
thread_metadata = {
    'thread_id': message_thread_id,  # Telegram thread ID
    'topic': infer_topic_from_messages(),  # "visa-processing", "bug-fix", etc.
    'date_range': (start_date, end_date),
    'message_count': len(messages)
}
```

### Step 1.2: Ripgrep Search for Existing Memory

**ALWAYS use ripgrep-search skill before reading anything.**

```bash
# Search for existing memory file with this thread_id
rg "thread_id: $thread_id" /root/.openclaw/memory/topics/ -l

# Search for similar topic memories
rg "topic: $topic_name" /root/.openclaw/memory/topics/ -l

# Search for date-overlapping memories
rg "date: $date_pattern" /root/.openclaw/memory/topics/ -l
```

### Step 1.3: Indexing Strategy

If existing memory found:
```python
# Read ONLY the metadata section (first 20 lines)
existing_metadata = read_file_lines(memory_file, 1, 20)

# Determine if this is:
# - CONTINUATION (same thread, add to existing)
# - DUPLICATE (same content, skip)
# - SEPARATE (different content, create new)

if is_continuation:
    # Only read the "Active Tasks" section, append new data
    append_mode = True
elif is_duplicate:
    log("Skipping: Memory already exists")
    return
else:
    create_new_memory = True
```

**Token Savings:**
- Without search-first: Read entire conversation (10K-20K tokens)
- With search-first: Read metadata only (200-500 tokens)
- **Savings: 95% reduction in token usage**

### Step 1.4: Conversation Chunking

If conversation is very long (>100 messages), don't load all at once:

```python
# Identify natural break points
breakpoints = find_conversation_breaks(messages)
# Examples: topic changes, long time gaps, explicit decisions

# Process in chunks
for chunk in split_by_breakpoints(messages, breakpoints):
    if should_distill_chunk(chunk):
        distill_chunk(chunk)
```

**RAM Impact:**
- Loading 200 messages: ~500MB RAM
- Loading 50 message chunks: ~125MB RAM per chunk
- **Reduction: 75% less peak RAM usage**

---

## Phase 2: Resource Awareness Check (VPS Safety)

**Goal: Choose appropriate AI model based on available resources.**

### Step 2.1: RAM Check

```bash
#!/bin/bash
# Check available RAM
AVAILABLE_RAM=$(free -m | awk 'NR==2 {print $7}')

echo "Available RAM: ${AVAILABLE_RAM}MB"

if [ $AVAILABLE_RAM -lt 200 ]; then
    echo "LOW_RAM_MODE: Using cloud AI (Gemini)"
    AI_MODE="cloud"
elif [ $AVAILABLE_RAM -lt 500 ]; then
    echo "MODERATE_RAM: Using local AI with streaming"
    AI_MODE="local_streaming"
else
    echo "SUFFICIENT_RAM: Using local AI (qwen-opt)"
    AI_MODE="local_full"
fi
```

### Step 2.2: AI Model Selection Strategy

**Decision Tree:**

```
Available RAM?
├─ < 200MB → CLOUD AI (Gemini)
│  ├─ Send conversation to Gemini API
│  ├─ Get distilled summary
│  └─ No local RAM usage
│
├─ 200-500MB → LOCAL AI (Streaming)
│  ├─ Spawn qwen-opt session
│  ├─ Stream conversation in chunks
│  ├─ Process incrementally
│  └─ Moderate RAM usage
│
└─ > 500MB → LOCAL AI (Full)
   ├─ Spawn qwen-opt session
   ├─ Load full conversation
   ├─ Single-pass processing
   └─ Higher RAM but faster
```

### Step 2.3: Cloud AI Integration (Gemini)

When RAM < 200MB, use Gemini:

```python
import google.generativeai as genai

def distill_with_gemini(conversation_text):
    """
    Use Gemini for distillation when local RAM is insufficient
    """
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
You are a conversation distillation expert. Extract ONLY the critical information from this Telegram thread:

CONVERSATION:
{conversation_text}

EXTRACT:
1. Topic ID/Name
2. Core Logic/Decisions (especially #IMPORTANT, #URGENT items)
3. Active Tasks (with status)
4. Next Goals
5. Key Preferences/Instructions from Nolan

FORMAT:
[Topic ID / Name]
Topic: <name>
Thread ID: <id>
Date: <date>

[Core Logic/Decision]
- <decision 1>
- <decision 2>

[Active Tasks]
- [ ] <task 1> (Status: <status>)
- [x] <task 2> (Status: Done)

[Next Goals]
- <goal 1>
- <goal 2>

IMPORTANT: Preserve all #IMPORTANT and #URGENT tagged items exactly.
"""
    
    response = model.generate_content(prompt)
    return response.text
```

**Cost vs Performance:**
- Gemini API call: ~$0.001 per distillation
- Local qwen-opt: Free but requires RAM
- **Trade-off: Pay tiny fee to stay within VPS limits**

### Step 2.4: Local AI Integration (qwen-opt)

When RAM ≥ 200MB, use local model:

```python
def distill_with_local_ai(conversation_text, mode='streaming'):
    """
    Use local qwen-opt for distillation when RAM is available
    """
    # Spawn AI session
    session_id = spawn_ai_session('qwen-opt')
    
    if mode == 'streaming':
        # Stream in chunks to manage RAM
        chunks = split_conversation(conversation_text, chunk_size=50)
        distilled_chunks = []
        
        for chunk in chunks:
            result = send_to_ai_session(session_id, {
                'prompt': f"Summarize key points: {chunk}",
                'max_tokens': 500
            })
            distilled_chunks.append(result)
        
        # Combine distilled chunks
        final_summary = combine_summaries(distilled_chunks)
    
    else:  # mode == 'full'
        # Single pass (faster but more RAM)
        final_summary = send_to_ai_session(session_id, {
            'prompt': f"Distill this conversation: {conversation_text}",
            'max_tokens': 2000
        })
    
    # Clean up session
    close_ai_session(session_id)
    
    return final_summary
```

### Step 2.5: Fallback Strategy

If both fail (RAM critical AND no API key):

```python
def emergency_distillation(conversation_text):
    """
    Manual rule-based distillation as last resort
    """
    # Extract messages with tags
    important_msgs = [m for m in messages if '#IMPORTANT' in m or '#URGENT' in m]
    
    # Extract decision keywords
    decision_msgs = [m for m in messages if any(kw in m.lower() for kw in 
                     ['decide', 'agreed', 'will do', 'must', 'should'])]
    
    # Extract tasks
    task_msgs = [m for m in messages if '[ ]' in m or '[x]' in m]
    
    # Combine
    distilled = {
        'critical': important_msgs,
        'decisions': decision_msgs,
        'tasks': task_msgs
    }
    
    return format_distilled(distilled)
```

---

## Phase 3: Distillation Logic (80/20 Rule)

**Goal: Retain 20% of content that contains 80% of value.**

### Step 3.1: Content Classification

Classify each message into priority tiers:

**TIER 1: MUST RETAIN (20% of messages, 80% of value)**
- Messages with `#IMPORTANT` or `#URGENT` tags
- Explicit decisions ("We decided to...", "The plan is...")
- Task assignments ("You need to...", "I'll handle...")
- Nolan's preferences ("I prefer...", "Always do...")
- Error resolutions ("The fix was...", "Root cause:")
- Action items with deadlines

**TIER 2: CONDITIONAL RETAIN (30% of messages, 15% of value)**
- Context-setting explanations
- Problem descriptions (without solutions)
- Questions that led to decisions
- Intermediate reasoning steps

**TIER 3: DISCARD (50% of messages, 5% of value)**
- Greetings and small talk ("Hi", "Thanks", "Sure")
- Repeated questions (asked 3+ times without progress)
- Dead-end discussions (no resolution)
- Acknowledgments without content ("Ok", "Got it", "👍")
- Off-topic tangents

### Step 3.2: Data Retention Rules

**PRESERVE 100%:**
```python
# Always keep these patterns exactly as-is
preserve_patterns = [
    r'#IMPORTANT',
    r'#URGENT',
    r'#TODO',
    r'DECISION:',
    r'AGREED:',
    r'ACTION:',
    r'DEADLINE:',
    r'\[ \]',  # Unchecked task
    r'\[x\]',  # Completed task
]

for msg in messages:
    if any(re.search(pattern, msg) for pattern in preserve_patterns):
        critical_messages.append(msg)
```

**Nolan's Preferences Detection:**
```python
# Extract and preserve user preferences
preference_indicators = [
    'I prefer',
    'I want',
    'Always',
    'Never',
    'Make sure to',
    'Remember to',
    'Don\'t forget',
]

for msg in nolan_messages:
    if any(indicator in msg for indicator in preference_indicators):
        preferences.append(msg)
```

**Task Status Tracking:**
```python
# Track task states across conversation
tasks = {}

for msg in messages:
    # Find task definitions
    if '[ ]' in msg or '[x]' in msg:
        task_id = extract_task_id(msg)
        tasks[task_id] = {
            'description': extract_task_description(msg),
            'status': 'done' if '[x]' in msg else 'pending',
            'mentioned_at': msg_timestamp,
            'assigned_to': extract_assignee(msg)
        }
```

### Step 3.3: Noise Removal

**Eliminate low-value content:**

```python
def is_noise(message):
    """
    Identify messages that can be safely removed
    """
    # Short acknowledgments
    if len(message.split()) <= 3 and message.lower() in [
        'ok', 'sure', 'thanks', 'got it', 'yes', 'no', 'hi', 'hello'
    ]:
        return True
    
    # Pure emojis
    if all(c in emoji_chars for c in message.strip()):
        return True
    
    # Repeated without progress
    if message in seen_messages and no_new_info_after(message):
        return True
    
    # Abandoned discussions
    if is_question(message) and no_answer_within(30_messages):
        return True
    
    return False
```

**Compression Techniques:**

```python
def compress_conversation(messages):
    """
    Apply compression while preserving meaning
    """
    # Combine sequential messages from same person
    combined = combine_sequential_messages(messages)
    
    # Remove redundant explanations
    deduplicated = remove_redundant_explanations(combined)
    
    # Merge similar questions into one
    merged_questions = merge_similar_questions(deduplicated)
    
    # Extract core logic only
    distilled = extract_core_logic(merged_questions)
    
    return distilled
```

### Step 3.4: Structured Output Format

**MANDATORY OUTPUT FORMAT:**

```markdown
# [Topic ID / Name]

**Metadata:**
- Topic: <topic_name>
- Thread ID: <telegram_thread_id>
- Date Range: <start_date> to <end_date>
- Message Count: <original_count> → <distilled_count>
- Participants: <user_list>

---

## [Core Logic/Decision]

### Key Decisions
- **[Decision 1]** #IMPORTANT
  - Context: <brief context>
  - Rationale: <why this decision>
  - Timestamp: <when decided>

- **[Decision 2]** #URGENT
  - Context: <brief context>
  - Action Required: <what needs to be done>
  - Deadline: <when>

### Technical Specifications
- <spec 1>
- <spec 2>

### Preferences (Nolan)
- <preference 1>
- <preference 2>

---

## [Active Tasks]

- [ ] **Task 1** #URGENT
  - Status: In Progress
  - Assigned: David
  - Deadline: 2024-03-20
  - Blockers: None

- [x] **Task 2** #DONE
  - Status: Completed
  - Completed: 2024-03-15
  - Result: <outcome>

- [ ] **Task 3**
  - Status: Pending
  - Dependencies: Task 1

---

## [Next Goals]

### Immediate (Next Session)
1. <goal 1>
2. <goal 2>

### Short-term (This Week)
1. <goal 3>
2. <goal 4>

### Long-term (This Month)
1. <goal 5>

---

## [Reference Links]

- Original Thread: `openclaw.db/threads/<thread_id>`
- Related Topics: `memory/topics/<related_topic>.md`
- Previous Distillation: `memory/topics/<topic>_archive_<date>.md`
```

### Step 3.5: Quality Validation

Before finalizing distillation:

```python
def validate_distillation(original, distilled):
    """
    Ensure critical info wasn't lost
    """
    checks = {
        'important_tags': count_tags(original, '#IMPORTANT') == count_tags(distilled, '#IMPORTANT'),
        'urgent_tags': count_tags(original, '#URGENT') == count_tags(distilled, '#URGENT'),
        'tasks_preserved': count_tasks(original) == count_tasks(distilled),
        'decisions_present': has_decisions_section(distilled),
        'format_valid': matches_required_format(distilled),
        'size_reduction': len(distilled) < len(original) * 0.3  # At least 70% reduction
    }
    
    if not all(checks.values()):
        raise ValidationError(f"Distillation failed checks: {checks}")
    
    return True
```

---

## Phase 4: Multi-layered Storage Update

**Goal: Update all three memory tiers consistently.**

### Step 4.1: Tier 1 (Hot Memory) - INDEX.md Update

**Add entry to INDEX.md:**

```python
def update_index_md(distilled_summary):
    """
    Add reference to new distilled memory in INDEX.md
    """
    # Read current INDEX.md
    index_content = read_file('/root/.openclaw/memory/INDEX.md')
    
    # Determine if this goes to ACTIVE_PROJECTS or TOPIC_MAP
    score = calculate_importance_score(distilled_summary)
    
    if score >= 70:
        # Add to ACTIVE_PROJECTS section
        new_entry = f"""
### Project: {distilled_summary['topic']}
- **Status**: Active
- **Priority**: {'#IMPORTANT' if score >= 100 else 'High'}
- **Thread**: {distilled_summary['thread_id']}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
- **Memory File**: `memory/topics/{distilled_summary['topic']}.md`
- **Summary**: {distilled_summary['core_decision'][:100]}...
"""
        index_content = insert_into_section(
            index_content, 
            '## 🔥 ACTIVE_PROJECTS', 
            new_entry
        )
    
    else:
        # Add to TOPIC_MAP section
        new_entry = f"- **{distilled_summary['topic'].title()}** → `memory/topics/{distilled_summary['topic']}.md` (Updated: {datetime.now().strftime('%Y-%m-%d')})\n"
        index_content = insert_into_section(
            index_content,
            '## 📂 TOPIC_MAP',
            new_entry
        )
    
    # Write updated INDEX.md
    write_file('/root/.openclaw/memory/INDEX.md', index_content)
```

### Step 4.2: Tier 2 (Warm Memory) - Topics File

**Create or update topic file:**

```python
def save_to_warm_memory(distilled_content, thread_metadata):
    """
    Save distilled conversation to appropriate topic file
    """
    topic_name = thread_metadata['topic']
    topic_file = f'/root/.openclaw/memory/topics/{topic_name}.md'
    
    # Check if topic file exists
    if file_exists(topic_file):
        # APPEND mode: Add new distillation
        existing_content = read_file(topic_file)
        
        # Add separator
        separator = f"\n\n---\n## Update: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        updated_content = existing_content + separator + distilled_content
        
        write_file(topic_file, updated_content)
        log(f"Appended to existing topic: {topic_name}")
    
    else:
        # CREATE mode: New topic file
        header = f"""# {topic_name.replace('-', ' ').title()}

Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Source: Telegram Thread {thread_metadata['thread_id']}

---

"""
        new_content = header + distilled_content
        
        write_file(topic_file, new_content)
        log(f"Created new topic file: {topic_name}")
```

### Step 4.3: Tier 3 (Cold Memory) - Database Cleanup

**Signal to flush original conversation:**

```python
def signal_cold_storage_cleanup(thread_id):
    """
    Signal that original conversation can be archived/compressed
    """
    # Create signal file for database management
    signal_file = f'/root/.openclaw/.signals/compact_{thread_id}.signal'
    
    signal_data = {
        'thread_id': thread_id,
        'action': 'archive',
        'reason': 'Distilled to Tier 2',
        'distilled_to': f'memory/topics/{topic_name}.md',
        'timestamp': datetime.now().isoformat(),
        'original_size': len(conversation_text),
        'distilled_size': len(distilled_content),
        'compression_ratio': len(distilled_content) / len(conversation_text)
    }
    
    write_json(signal_file, signal_data)
    
    log(f"Signal created for database cleanup: {thread_id}")
```

**Database vacuum recommendation:**

```python
def recommend_vacuum():
    """
    Check if database needs vacuuming after multiple compactions
    """
    signal_files = list_files('/root/.openclaw/.signals/', '*.signal')
    
    if len(signal_files) >= 10:
        log("⚠️ 10+ compaction signals detected")
        log("Recommendation: Run database vacuum to reclaim space")
        log("Command: sqlite3 openclaw.db 'VACUUM;'")
        
        # Optionally auto-vacuum if safe
        if is_safe_to_vacuum():
            execute('sqlite3 /root/.openclaw/openclaw.db "VACUUM;"')
            log("✅ Database vacuumed successfully")
```

### Step 4.4: Cross-referencing

**Link related memories:**

```python
def create_cross_references(current_topic, distilled_content):
    """
    Find and link related topic files
    """
    # Extract keywords from current distillation
    keywords = extract_keywords(distilled_content)
    
    # Use ripgrep to find related topics
    related_files = []
    for keyword in keywords[:5]:  # Top 5 keywords
        results = ripgrep_search(
            keyword, 
            '/root/.openclaw/memory/topics/',
            file_list_only=True
        )
        related_files.extend(results)
    
    # Remove duplicates and current file
    related_files = list(set(related_files))
    related_files = [f for f in related_files if current_topic not in f]
    
    # Add "Related Topics" section to distilled content
    if related_files:
        references = "\n\n## Related Topics\n\n"
        for file in related_files[:3]:  # Top 3 most related
            topic_name = extract_topic_name(file)
            references += f"- [{topic_name}]({file})\n"
        
        distilled_content += references
    
    return distilled_content
```

---

## Complete Workflow Example

### Example: Distilling a Long Bug Fix Discussion

**Input**: 150-message Telegram thread about database connection error

**Phase 1: Search First**
```bash
# Check for existing bug-fix memories
rg "database connection error" /root/.openclaw/memory/topics/ -l
# Found: memory/topics/database-issues.md

# Read metadata only
head -20 memory/topics/database-issues.md
# Contains previous error from 2 weeks ago, but different root cause

# Decision: Create new entry in same file (related issues)
```

**Phase 2: Resource Check**
```bash
free -m
# Available: 350MB
# Decision: Use local AI with streaming mode
```

**Phase 3: Distillation**
```python
# Extract from 150 messages:
# - 15 messages with #IMPORTANT or #URGENT
# - 8 decision messages
# - 12 task-related messages
# - Remove 115 noise messages (greetings, redundant explanations)

# Output: 35 messages (77% reduction) containing all critical info
```

**Phase 4: Storage**
```markdown
# Updated: memory/topics/database-issues.md
## Update: 2024-03-15 14:30

# Database Connection Error - PostgreSQL Timeout #IMPORTANT

**Metadata:**
- Thread ID: 12345
- Date: 2024-03-15
- Original Messages: 150 → Distilled: 35

## [Core Logic/Decision]

### Root Cause #IMPORTANT
- PostgreSQL connection pool exhausted due to missing connection.close() in API endpoints
- Max connections: 20, but 50+ connections attempted during peak load

### Solution Decided
- AGREED: Implement connection pooling with SQLAlchemy
- AGREED: Add connection timeout of 30 seconds
- AGREED: Monitor connection count with Prometheus

## [Active Tasks]

- [ ] Implement SQLAlchemy connection pool #URGENT
  - Assigned: David
  - Deadline: 2024-03-17
  - Priority: High

- [ ] Add Prometheus monitoring
  - Assigned: David
  - Deadline: 2024-03-20

- [x] Identify root cause
  - Completed: 2024-03-15
  - Result: Found missing connection.close() calls

## [Next Goals]

### Immediate
1. Deploy connection pool fix to staging
2. Test under load

### Short-term
1. Implement monitoring dashboard
2. Document connection management best practices

## [Reference Links]

- Original Thread: `openclaw.db/threads/12345`
- Related: [Database Configuration](database-config.md)
```

**Result:**
- Original: 150 messages, ~15K tokens
- Distilled: 35 key points, ~2K tokens
- **Savings: 87% token reduction**
- **Preserved: 100% of critical decisions and tasks**

---

## Performance & Safety

### Token Efficiency

| Operation | Without Compact | With Compact | Savings |
|-----------|----------------|--------------|---------|
| Read thread | 15K tokens | 2K tokens | 87% |
| Search memory | 5K tokens | 200 tokens | 96% |
| Total per query | 20K tokens | 2.2K tokens | 89% |

### RAM Management

| RAM Available | AI Strategy | RAM Usage | Speed |
|---------------|-------------|-----------|-------|
| < 200MB | Gemini API | 0MB (cloud) | Fast |
| 200-500MB | Local streaming | 150MB peak | Medium |
| > 500MB | Local full | 300MB peak | Fastest |

### Storage Impact

- Hot (INDEX.md): +100 bytes per entry
- Warm (topics/): +2-5KB per distillation
- Cold (openclaw.db): Can archive/compress original (70-90% space savings)

---

## Edge Cases & Error Handling

### Case 1: API Key Missing (Gemini)

```python
if ram_low and not gemini_api_key:
    # Fallback to emergency rule-based distillation
    log("WARNING: Low RAM and no API key, using emergency mode")
    result = emergency_distillation(conversation)
```

### Case 2: Distillation Failed Validation

```python
if not validate_distillation(original, distilled):
    # Retry with stricter rules
    log("Validation failed, retrying with conservative settings")
    distilled = distill_with_high_precision(original)
```

### Case 3: Corrupted Topic File

```python
if file_corrupted(topic_file):
    # Backup and regenerate
    backup_file(topic_file, f"{topic_file}.backup")
    regenerate_from_index(topic_file)
```

### Case 4: Thread Too Large (>500 messages)

```python
if message_count > 500:
    # Split into multiple distillations
    log(f"Thread too large ({message_count} msgs), splitting")
    chunks = split_thread(messages, max_chunk=100)
    for i, chunk in enumerate(chunks):
        distill_chunk(chunk, part=i+1)
```

---

## Maintenance & Monitoring

### Health Checks

```python
def health_check():
    """Daily health check for compact-framework"""
    checks = {
        'ripgrep_available': check_ripgrep(),
        'memory_dirs_exist': check_directories(),
        'index_md_valid': validate_index_md(),
        'topic_files_count': count_topic_files(),
        'signal_files_pending': count_signal_files(),
        'ram_status': check_ram_status()
    }
    return checks
```

### Statistics

```python
def show_statistics():
    """Show distillation statistics"""
    stats = {
        'total_distillations': count_signal_files(),
        'avg_compression_ratio': calculate_avg_compression(),
        'total_tokens_saved': calculate_token_savings(),
        'total_space_saved': calculate_space_savings(),
        'topics_created': count_topic_files(),
        'ram_mode_distribution': count_ram_modes()
    }
    print_statistics(stats)
```

---

## မြန်မာဘာသာ မှတ်ချက်

ဒီ Compact Framework Skill က Telegram thread conversations တွေကို အလွန် ထိရောက်စွာ distill လုပ်ပေးတဲ့ autonomous system ဖြစ်ပါတယ်။

### အဓိက လုပ်ဆောင်ချက် (၄) ဆင့်

**1. Search First (Token Saver)**
- အရင် ripgrep နဲ့ ရှာတယ်
- ဖိုင်အပြည့်အစုံ မဖတ်ခင် metadata ကိုပဲ စစ်တယ်
- Token 50% သက်သာတယ်

**2. Resource Awareness (VPS Safety)**
- RAM ကို အရင်စစ်တယ်
- RAM < 200MB → Gemini API သုံးတယ် (cloud)
- RAM >= 200MB → Local qwen-opt သုံးတယ်
- VPS ကို လုံခြုံစေတယ်

**3. Distillation Logic (80/20 Rule)**
- အရေးကြီးတဲ့ 20% ကိုပဲ ထားတယ်
- #IMPORTANT, #URGENT, decisions, tasks → 100% သိမ်းတယ်
- Noise (greetings, redundant) → ဖယ်ထုတ်တယ်
- 70-90% compression ratio ရတယ်

**4. Multi-layered Storage**
- Hot (INDEX.md) → Link ထည့်တယ်
- Warm (topics/) → အနှစ်ချုပ် သိမ်းတယ်
- Cold (openclaw.db) → Archive signal ပို့တယ်

### အသုံးပြုနည်း

**Trigger အမျိုးမျိုး:**
- User: "summarize this thread"
- Auto: Message count > 100
- Auto: Token usage > 15K
- Auto: Thread age > 2 hours

**Output Format:**
```
[Topic ID / Name]
[Core Logic/Decision]
[Active Tasks]
[Next Goals]
```

### အားသာချက်များ

1. **Token Efficiency**: 87-89% reduction
2. **RAM Safety**: Auto-selects AI based on RAM
3. **Critical Data**: 100% preserved (decisions, tasks)
4. **Structured Output**: Easy to search and reference
5. **Integration**: Works with memory-librarian skill

**အရေးကြီးဆုံး**: Thread conversations တွေက token အများကြီး စားတဲ့အတွက် ဒီ skill က အလွန်အသုံးဝင်ပါတယ်။ 150 messages ကို 35 key points အဖြစ် ချုံ့လိုက်ရင် token 87% သက်သာပါတယ်!
```

---
*Last Updated: 2026-03-02 by David (Manager)*
