#!/bin/bash

# OpenClaw Health Check Data Gatherer
# Outputs raw system data for status classification

echo "--- GATEWAY_PROCESS ---"
if systemctl is-active openclaw &>/dev/null; then
    echo "status: active (systemd)"
elif pgrep -f openclaw &>/dev/null; then
    echo "status: active (pgrep)"
else
    echo "status: inactive"
fi

echo "--- DISK_SPACE ---"
df -h / | awk 'NR==2 {print "usage_pct: "$5}'

echo "--- RECENT_ERRORS ---"
LOG_FILE="/root/.openclaw/logs/gateway.log"
if [ -f "$LOG_FILE" ]; then
    tail -100 "$LOG_FILE" | grep -ic error | awk '{print "count: "$1}'
else
    echo "count: 0 (no log file found)"
fi

echo "--- SESSION_INTEGRITY ---"
find /root/.openclaw/agents/main/sessions -name "*.jsonl" -size +5M | wc -l | awk '{print "large_sessions_count: "$1}'

echo "--- OPENCLAW_STATUS ---"
# Check if openclaw CLI is available
if command -v openclaw &>/dev/null; then
    openclaw status --json || echo "{\"error\": \"failed to run openclaw status\"}"
else
    echo "{\"error\": \"openclaw CLI not found\"}"
fi
