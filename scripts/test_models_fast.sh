#!/bin/bash
# Multi-Model Speed Tester (MMST)
# Created by David for Nolan

MODELS=(
    "google-gemini-cli/gemini-3-flash-preview"
    "google-gemini-cli/gemini-3-pro-preview"
    "ollama/qwen-opt:latest"
    "google-antigravity/claude-sonnet-4-5"
)

echo "🚀 Starting Parallel Model Test..."
echo "-----------------------------------"

for MODEL in "${MODELS[@]}"; do
    (
        START=$(date +%s%3N)
        # Using explicit model override for testing
        RESULT=$(openclaw agent --agent main --model "$MODEL" --message "respond with 'OK'" --timeout 30 --json 2>/dev/null)
        END=$(date +%s%3N)
        DIFF=$((END-START))
        
        if [[ $RESULT == *"\"status\":\"ok\""* ]]; then
            echo "✅ $MODEL: SUCCESS (${DIFF}ms)"
        else
            # Try to capture more error info if possible
            echo "❌ $MODEL: FAILED"
        fi
    ) &
done

wait
echo "-----------------------------------"
echo "🏁 All tests completed."
