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
    git push origin main
    echo "$(date): Backup successful."
fi
