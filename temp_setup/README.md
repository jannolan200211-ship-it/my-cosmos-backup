# Memory Librarian Skill

Intelligent knowledge organization system for VPS environments with limited RAM.

## Features

- 🧠 **Tiered Memory Architecture** - Hot/Warm/Cold storage optimization
- 🔍 **Ripgrep Integration** - Lightning-fast content search
- 📊 **Automatic Distillation** - Scheduled knowledge organization
- 🏷️ **Smart Importance Scoring** - User tags + recency + frequency
- 📦 **Intelligent Archiving** - Automatic cleanup of old files
- 💾 **RAM-Safe Operations** - Respects 2GB memory constraints
- 📱 **Telegram Notifications** - Stay informed of library updates

## Directory Structure

```
/root/.openclaw/
├── memory/
│   ├── INDEX.md              # Global knowledge index (Tier 1)
│   ├── topics/               # Topic-specific files (Tier 2)
│   │   ├── immigration-policies.md
│   │   ├── visa-processing.md
│   │   └── ...
│   └── archive/              # Archived old files
├── workspace/                # Active working files (Tier 3)
└── logs/
    └── librarian.log         # Operation logs
```

## Installation

1. **Install ripgrep** (required dependency):
```bash
apt-get update && apt-get install -y ripgrep
```

2. **Create directory structure**:
```bash
mkdir -p /root/.openclaw/memory/topics
mkdir -p /root/.openclaw/memory/archive
mkdir -p /root/.openclaw/logs
```

3. **Copy skill files** to your skills directory

4. **(Optional) Configure Telegram notifications**:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"

# Add to ~/.bashrc to make permanent
echo 'export TELEGRAM_BOT_TOKEN="your_token"' >> ~/.bashrc
echo 'export TELEGRAM_CHAT_ID="your_chat_id"' >> ~/.bashrc
```

## Usage

### Manual Distillation

Run distillation manually:
```bash
python3 /path/to/memory-librarian/scripts/distill.py
```

### Scheduled Distillation (Recommended)

Add to crontab for automatic daily runs:
```bash
# Edit crontab
crontab -e

# Add this line (runs at 3 AM daily):
0 3 * * * /usr/bin/python3 /root/.openclaw/memory-librarian/scripts/distill.py >> /root/.openclaw/logs/librarian.log 2>&1
```

### Check System Health

```bash
python3 /path/to/memory-librarian/scripts/health_check.py
```

### View Statistics

```bash
python3 /path/to/memory-librarian/scripts/stats.py
```

### Check RAM Status

```bash
bash /path/to/memory-librarian/scripts/check_ram.sh
```

## How It Works

### 1. Scanning Phase
- Scans `/root/.openclaw/workspace/` for all files
- Identifies recently modified files
- Detects user priority tags (`#IMPORTANT`, `#URGENT`, `#TODO`)

### 2. Scoring Phase
- Calculates importance score for each file:
  - User tags: 70-100 points
  - Recency: 10-50 points
  - Access frequency: 0-40 points

### 3. Organization Phase
- High-priority files (score > 80) → ACTIVE_PROJECTS
- Medium-priority files (40-80) → TOPIC_MAP
- Low-priority old files (< 40, > 30 days) → Archive

### 4. Distillation Phase
- Creates/updates topic files in `memory/topics/`
- Extracts key facts and summaries
- Merges duplicate information

### 5. Update Phase
- Updates `INDEX.md` with current state
- Records timestamp and statistics
- Logs all operations

### 6. Notification Phase
- Sends summary to Telegram (if configured)
- Logs completion message

## Using with Claude

### Triggering the Skill

Claude will automatically use this skill when you say:
- "organize library"
- "organize memory"
- "update knowledge index"
- "what's in my workspace?"
- "show me active projects"

### Memory Retrieval

Claude uses the tiered architecture efficiently:

1. **Quick lookup**: Checks `INDEX.md` first
2. **Topic dive**: Reads relevant topic file from `memory/topics/`
3. **Deep search**: Uses ripgrep on `workspace/` if needed

### Importance Tagging

Add tags to your files for better organization:
```markdown
# Project: Visa System Upgrade #IMPORTANT

This project needs to be completed by Q2 2024.

## Tasks #TODO
- [ ] Design database schema
- [ ] Implement API endpoints
```

## RAM Safety

The system respects your 2GB RAM limit:

- **Normal mode** (RAM < 90%): Full distillation with summarization
- **Low-memory mode** (RAM ≥ 90%): Index-only updates, skip heavy operations
- **Critical mode** (RAM > 95%): Abort and notify

Check RAM before operations:
```bash
bash /path/to/memory-librarian/scripts/check_ram.sh
```

## Troubleshooting

### Issue: "ripgrep not found"
```bash
apt-get install -y ripgrep
```

### Issue: "Permission denied" on scripts
```bash
chmod +x /path/to/memory-librarian/scripts/*.sh
chmod +x /path/to/memory-librarian/scripts/*.py
```

### Issue: INDEX.md corrupted
```bash
# Backup old index
mv /root/.openclaw/memory/INDEX.md /root/.openclaw/memory/INDEX.md.backup

# Run distillation to regenerate
python3 /path/to/memory-librarian/scripts/distill.py
```

### Issue: RAM exhaustion during distillation
The system will automatically enter low-memory mode or abort if RAM is critical. Check logs:
```bash
tail -f /root/.openclaw/logs/librarian.log
```

## Performance

Typical performance on 2GB RAM VPS:

- Workspace scan (100 files): ~2 seconds
- Importance scoring: ~5 seconds
- INDEX.md update: <1 second
- Full distillation cycle: 30-60 seconds
- RAM overhead: <200MB

## Myanmar Language Notes / မြန်မာဘာသာ မှတ်ချက်

ဒီ Memory Librarian က VPS environment တွေအတွက် ထူးခြားစွာ optimize လုပ်ထားတာပါ။

**အဓိက အားသာချက်များ:**
- Token အကုန်အသက်သာဆုံး (search first, read later)
- RAM 2GB ပေါ်မှာ အလွယ်တကူ အလုပ်လုပ်နိုင်တယ်
- အလိုအလျောက် organize လုပ်ပေးတယ်
- ဟောင်းသွားတဲ့ files တွေကို archive လုပ်ပေးတယ်

**သုံးရတာ လွယ်ကူတယ်:**
1. Claude ကို "organize library" လို့ ပြောရုံပါပဲ
2. သို့မဟုတ် cron job နဲ့ နေ့တိုင်း အလိုအလျောက် run ခိုင်းလို့ရတယ်

**အရေးကြီးတဲ့ files တွေကို tag တွဲပါ:**
```markdown
#IMPORTANT - အရေးကြီးဆုံး
#URGENT - အမြန်လုပ်ရမယ့်
#TODO - လုပ်စရာရှိသေးတာ
```

## License

MIT License - Free to use and modify

## Support

For issues or questions, check:
1. Health check: `python3 scripts/health_check.py`
2. Logs: `tail -f /root/.openclaw/logs/librarian.log`
3. Statistics: `python3 scripts/stats.py`
