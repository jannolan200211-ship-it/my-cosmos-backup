#!/bin/bash
# ram_check_ai_mode.sh - Determine which AI mode to use based on available RAM

set -e

# Get available RAM in MB
AVAILABLE_RAM=$(free -m | awk 'NR==2 {print $7}')
TOTAL_RAM=$(free -m | awk 'NR==2 {print $2}')
USED_RAM=$(free -m | awk 'NR==2 {print $3}')
RAM_PERCENT=$(awk "BEGIN {printf \"%.0f\", ($USED_RAM/$TOTAL_RAM)*100}")

echo "================================"
echo "RAM Status Check"
echo "================================"
echo "Total RAM:     ${TOTAL_RAM}MB"
echo "Used RAM:      ${USED_RAM}MB (${RAM_PERCENT}%)"
echo "Available RAM: ${AVAILABLE_RAM}MB"
echo ""

# Determine AI mode based on available RAM
if [ $AVAILABLE_RAM -lt 200 ]; then
    AI_MODE="cloud"
    echo "⚠️  LOW RAM MODE"
    echo "Available: ${AVAILABLE_RAM}MB < 200MB threshold"
    echo "Decision: Use Gemini API (cloud processing)"
    echo ""
    echo "Advantages:"
    echo "  - Zero local RAM usage"
    echo "  - Fast processing"
    echo "  - No risk of OOM"
    echo ""
    echo "Requirements:"
    echo "  - GEMINI_API_KEY must be set"
    echo "  - Internet connection required"
    
elif [ $AVAILABLE_RAM -lt 500 ]; then
    AI_MODE="local_streaming"
    echo "⚡ MODERATE RAM MODE"
    echo "Available: ${AVAILABLE_RAM}MB (200-500MB)"
    echo "Decision: Use local qwen-opt with streaming"
    echo ""
    echo "Strategy:"
    echo "  - Process conversation in chunks"
    echo "  - Stream results incrementally"
    echo "  - Peak RAM: ~150MB"
    
else
    AI_MODE="local_full"
    echo "✅ SUFFICIENT RAM MODE"
    echo "Available: ${AVAILABLE_RAM}MB > 500MB"
    echo "Decision: Use local qwen-opt (full processing)"
    echo ""
    echo "Strategy:"
    echo "  - Load full conversation"
    echo "  - Single-pass processing"
    echo "  - Fastest option"
fi

echo ""
echo "Selected AI Mode: $AI_MODE"
echo "================================"

# Return AI mode as exit code for script usage
case $AI_MODE in
    cloud)
        exit 1
        ;;
    local_streaming)
        exit 2
        ;;
    local_full)
        exit 0
        ;;
esac
