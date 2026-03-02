#!/usr/bin/python3
import subprocess
import os

# David's Librarian Script
# Logic: 12-hour interval (12:00 AM/PM)
# Task: Summarize business strategy, contacts, and decisions.

def main():
    print("David's Memory Distillation starting...")
    # Triggering the compact-framework via subagent spawn
    # This keeps the main process clean.
    task = "Perform business memory distillation from today's conversation. Update memory/david/ folder with summarized decisions and contacts."
    
    try:
        # Use openclaw command to spawn the distillation task
        # Redirect output to a log file for transparency
        subprocess.run(["openclaw", "subagents", "spawn", "david", task], check=True)
        print("David's Distillation successfully triggered.")
        # Final transparency message to Nolan (handled via subagent announce or manual send)
        # Note: In a real cron environment, this script runs independently.
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
