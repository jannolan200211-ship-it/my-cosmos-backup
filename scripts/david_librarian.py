#!/usr/bin/python3
import subprocess
import os

# David's Librarian Script (Fixed for OpenClaw 2026.2.26)
# Logic: 12-hour interval (12:00 AM/PM)

def main():
    print("David's Memory Distillation starting...")
    task = "Perform business memory distillation for Topic 44 (David). Update memory/00_Shared/01_David/02_Logs/ with summarized decisions and contacts. Sync with 00_INDEX.md."
    
    try:
        # Use 'openclaw agent' CLI to run the distillation turn
        subprocess.run(["openclaw", "agent", "--agent", "david", "--message", task], check=True)
        print("David's Distillation successfully triggered.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
