#!/bin/bash
# Log Guardian Script - Ko Sai

LOG_DIR="/root/.openclaw/workspace/99 Archive/logs"
BACKUP_DIR="/root/.openclaw/workspace/99 Archive/logs/backups"

# Create backup directory if not exists
mkdir -p "$BACKUP_DIR"

# 1. System Journal Vacuuming (7 days)
journalctl --vacuum-time=7d

# 2. Archive logs from LOG_DIR that are older than 7 days
find "$LOG_DIR" -maxdepth 1 -type f -mtime +7 -exec mv {} "$BACKUP_DIR/" \;

# 3. Create a zip archive of the files in BACKUP_DIR
cd "$BACKUP_DIR"
if ls *.log 1> /dev/null 2>&1; then
    zip -r "logs_archive_$(date +%Y-%m-%d).zip" . -i "*.log"
    find . -type f -name "*.log" -delete
fi

echo "Log cleaning and archiving completed for $(date)"
