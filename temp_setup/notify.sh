#!/bin/bash
# notify.sh - Send Telegram notification after distillation

# Telegram Bot Configuration
# TODO: User needs to set these environment variables:
# export TELEGRAM_BOT_TOKEN="your_bot_token"
# export TELEGRAM_CHAT_ID="your_chat_id"

TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN:-}"
TELEGRAM_CHAT_ID="${TELEGRAM_CHAT_ID:-}"

# Default message if none provided
MESSAGE="${1:-📚 Library operation completed}"

# Function to send Telegram message
send_telegram() {
    local msg="$1"
    
    if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ -z "$TELEGRAM_CHAT_ID" ]; then
        echo "⚠️  Telegram credentials not configured"
        echo "To enable notifications, set:"
        echo "  export TELEGRAM_BOT_TOKEN='your_token'"
        echo "  export TELEGRAM_CHAT_ID='your_chat_id'"
        echo ""
        echo "Message that would be sent:"
        echo "$msg"
        return 1
    fi
    
    # Send via Telegram API
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        -d "chat_id=${TELEGRAM_CHAT_ID}" \
        -d "text=${msg}" \
        -d "parse_mode=HTML" > /dev/null
    
    if [ $? -eq 0 ]; then
        echo "✅ Notification sent to Telegram"
        return 0
    else
        echo "❌ Failed to send Telegram notification"
        return 1
    fi
}

# Build formatted message
build_message() {
    local topics_updated="${2:-0}"
    local files_archived="${3:-0}"
    local active_projects="${4:-0}"
    local ram_percent="${5:-0}"
    local duration="${6:-0}"
    
    cat <<EOF
📚 <b>Library Organized</b> ($(date '+%H:%M'))

✅ ${topics_updated} Topics Updated
📁 ${files_archived} Files Archived
🔥 ${active_projects} Active Projects
💾 RAM: ${ram_percent}% $([ $ram_percent -gt 80 ] && echo "(High)" || echo "(Safe)")
⏱️ Time: ${duration}s
EOF
}

# If called with multiple arguments, build formatted message
if [ $# -gt 1 ]; then
    MESSAGE=$(build_message "$@")
fi

# Send notification
send_telegram "$MESSAGE"
