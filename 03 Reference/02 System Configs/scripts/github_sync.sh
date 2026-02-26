#!/bin/bash
# Cosmos System - Automated GitHub Sync Script
# Runs every 6 hours

WORKSPACE_DIR="/root/.openclaw/workspace"
cd $WORKSPACE_DIR

# Add changes
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "$(date): No changes to backup."
else
    # Commit with Burmese date format as requested
    TIMESTAMP=$(date +'%d/%m/%Y %H:%M:%S')
    git commit -m "Auto-backup: $TIMESTAMP"
    
    # Push to GitHub
    if git push origin main; then
        echo "$(date): Backup successful."
        # Send Telegram notification via OpenClaw CLI (LLM-free)
        openclaw message send --target "telegram:1839077362" --message "✅ GitHub Auto-backup အောင်မြင်ပါသည် (Timestamp: $TIMESTAMP)"
    else
        echo "$(date): Backup failed."
        openclaw message send --target "telegram:1839077362" --message "❌ GitHub Auto-backup ကျရှုံးပါသည်။ ကျေးဇူးပြု၍ စစ်ဆေးပေးပါ။"
    fi
fi
