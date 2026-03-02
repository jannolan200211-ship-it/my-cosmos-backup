#!/bin/bash
# check_ram.sh - RAM safety checker for memory librarian

set -e

# Get RAM usage in MB
RAM_TOTAL=$(free -m | awk 'NR==2 {print $2}')
RAM_USED=$(free -m | awk 'NR==2 {print $3}')
RAM_PERCENT=$(awk "BEGIN {printf \"%.0f\", ($RAM_USED/$RAM_TOTAL)*100}")

# Threshold: 90% of 2GB = 1800MB
THRESHOLD=90

echo "RAM Status Check"
echo "================"
echo "Total: ${RAM_TOTAL}MB"
echo "Used: ${RAM_USED}MB (${RAM_PERCENT}%)"
echo ""

if [ $RAM_PERCENT -gt $THRESHOLD ]; then
    echo "⚠️  WARNING: RAM usage at ${RAM_PERCENT}% (threshold: ${THRESHOLD}%)"
    echo "Recommendation: LOW_MEMORY_MODE activated"
    exit 1
else
    echo "✅ RAM usage healthy (${RAM_PERCENT}% < ${THRESHOLD}%)"
    echo "Safe to proceed with distillation"
    exit 0
fi
