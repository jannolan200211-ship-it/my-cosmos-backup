#!/bin/bash
# Nolan's Secure Master Vault (NSMV)
# Logic: Key-based verification before retrieving passwords.
# Created by David for Nolan

VAULT_DIR="/root/.openclaw/workspace/memory/vault"
VAULT_FILE="$VAULT_DIR/passwords.txt"
SECRET_KEY_FILE="$VAULT_DIR/.master_secret"

mkdir -p "$VAULT_DIR"
touch "$VAULT_FILE"
chmod 600 "$VAULT_FILE"

# Initialize Master Secret if not exists
if [ ! -f "$SECRET_KEY_FILE" ]; then
    if [ -z "$1" ]; then
        echo "INIT_REQUIRED: Please provide a Master Secret Key to initialize the vault."
        exit 1
    else
        echo "$1" > "$SECRET_KEY_FILE"
        chmod 600 "$SECRET_KEY_FILE"
        echo "✅ Master Secret Key established. Do not forget it!"
        exit 0
    fi
fi

MASTER_SECRET=$(cat "$SECRET_KEY_FILE")

case "$1" in
    add)
        # Usage: vault add <master_secret> <account_name> <password>
        if [ "$2" != "$MASTER_SECRET" ]; then
            echo "❌ ERROR: Invalid Master Secret Key. Access Denied."
            exit 1
        fi
        if [ -z "$3" ] || [ -z "$4" ]; then
            echo "Usage: vault add <master_secret> <account_name> <password>"
            exit 1
        fi
        # Remove existing entry if any
        grep -v "^$3: " "$VAULT_FILE" > "${VAULT_FILE}.tmp" && mv "${VAULT_FILE}.tmp" "$VAULT_FILE"
        echo "$3: $4" >> "$VAULT_FILE"
        echo "✅ Password for '$3' stored safely."
        ;;
    get)
        # Usage: vault get <master_secret> <account_name>
        if [ "$2" != "$MASTER_SECRET" ]; then
            echo "❌ ERROR: Invalid Master Secret Key. Access Denied."
            exit 1
        fi
        if [ -z "$3" ]; then
            echo "Usage: vault get <master_secret> <account_name>"
            exit 1
        fi
        RESULT=$(grep "^$3: " "$VAULT_FILE" | cut -d' ' -f2-)
        if [ -z "$RESULT" ]; then
            echo "❓ No entry found for '$3'."
        else
            echo "$RESULT"
        fi
        ;;
    list)
        # Usage: vault list <master_secret>
        if [ "$2" != "$MASTER_SECRET" ]; then
            echo "❌ ERROR: Invalid Master Secret Key. Access Denied."
            exit 1
        fi
        cut -d':' -f1 "$VAULT_FILE"
        ;;
    change-secret)
        # Usage: vault change-secret <old_secret> <new_secret>
        if [ "$2" != "$MASTER_SECRET" ]; then
            echo "❌ ERROR: Invalid Master Secret Key. Access Denied."
            exit 1
        fi
        echo "$3" > "$SECRET_KEY_FILE"
        echo "✅ Master Secret Key updated successfully."
        ;;
    *)
        echo "Nolan's Secure Master Vault"
        echo "Commands: add, get, list, change-secret"
        ;;
esac
