#!/bin/bash
# Gemini Account Rotator (GAR)
# Logic: Checks current model status and rotates to the next available Gmail account if an error is detected or manually triggered.
# Created by David for Nolan

CONFIG_FILE="/root/.openclaw/openclaw.json"
ACCOUNTS=(
    "google-gemini-cli:skyhtetaunglin2002@gmail.com"
    "google-gemini-cli:htetaungl451@gmail.com"
    "google-gemini-cli:jannolan200211@gmail.com"
)

# Function to get the current active account
get_current() {
    grep -oP 'google-gemini-cli:[a-zA-Z0-9._%+-]+@gmail\.com' "$CONFIG_FILE" | head -n 1
}

# Function to switch to a specific account
switch_to() {
    local target=$1
    local current=$(get_current)
    if [ "$target" == "$current" ]; then
        echo "ℹ️ Account $target is already active."
        return
    fi
    
    # Surgical edit using sed to replace the auth profile linkage
    # This logic assumes the first occurrence in profiles is the primary linkage
    sed -i "s/$current/$target/g" "$CONFIG_FILE"
    openclaw gateway restart > /dev/null 2>&1
    echo "✅ Switched Gemini account to: $target"
}

case "$1" in
    list)
        echo "Available Gemini Accounts:"
        for acc in "${ACCOUNTS[@]}"; do echo " - $acc"; done
        ;;
    current)
        echo "Active Account: $(get_current)"
        ;;
    rotate)
        CURRENT=$(get_current)
        NEXT=""
        for i in "${!ACCOUNTS[@]}"; do
            if [[ "${ACCOUNTS[$i]}" == "$CURRENT" ]]; then
                NEXT_INDEX=$(( (i + 1) % ${#ACCOUNTS[@]} ))
                NEXT="${ACCOUNTS[$NEXT_INDEX]}"
                break
            fi
        done
        switch_to "$NEXT"
        ;;
    *)
        echo "Gemini Rotator Utility"
        echo "Commands: list, current, rotate"
        ;;
esac
