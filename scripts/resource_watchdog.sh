#!/bin/bash

# resource_watchdog.sh - Monitor RAM and reload PM2 if memory is low
# Threshold: 300MB Available RAM

THRESHOLD=300
AVAILABLE_RAM=$(free -m | awk '/^Mem:/{print $7}')

echo "$(date): Available RAM is ${AVAILABLE_RAM}MB"

if [ "$AVAILABLE_RAM" -lt "$THRESHOLD" ]; then
    echo "$(date): Low memory detected (${AVAILABLE_RAM}MB). Reloading PM2 (Cosmos-Automation)..."
    pm2 reload 0
    echo "$(date): Reload complete."
else
    echo "$(date): Memory is healthy."
fi
