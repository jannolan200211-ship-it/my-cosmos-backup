#!/bin/bash

# Token Usage & Session Size Monitor
# Identifies candidates for Early Compact Pattern

echo "--- SESSION_SIZES ---"
find /root/.openclaw/agents/main/sessions -name "*.jsonl" -exec du -h {} + | sort -hr

echo ""
echo "--- TOTAL_TOKEN_ESTIMATE ---"
# Just a rough count of lines in memory files to gauge size
wc -l /root/.openclaw/workspace/MEMORY.md /root/.openclaw/workspace/memory/*.md 2>/dev/null

echo ""
echo "--- COMPACTION_CANDIDATES ---"
# Find sessions > 2MB (earlier than the 5MB fail threshold)
find /root/.openclaw/agents/main/sessions -name "*.jsonl" -size +2M
