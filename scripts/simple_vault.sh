#!/bin/bash
# Simple Password Vault Helper (SPVH)
# Created by David for Nolan

VAULT_DIR="/root/.openclaw/workspace/memory/vault"
VAULT_FILE="$VAULT_DIR/passwords.txt"
mkdir -p "$VAULT_DIR"
touch "$VAULT_FILE"
chmod 600 "$VAULT_FILE"

case "$1" in
    add)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: vault add <key_name> <password>"
            exit 1
        fi
        echo "$2: $3" >> "$VAULT_FILE"
        echo "✅ Password for '$2' stored safely."
        ;;
    get)
        if [ -z "$2" ]; then
            echo "Usage: vault get <key_name>"
            exit 1
        fi
        grep "^$2: " "$VAULT_FILE" | cut -d' ' -f2-
        ;;
    list)
        cut -d':' -f1 "$VAULT_FILE"
        ;;
    *)
        echo "Simple Vault Helper"
        echo "Commands: add, get, list"
        ;;
esac
