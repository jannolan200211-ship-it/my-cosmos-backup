#!/usr/bin/python3
import subprocess
import os

# Ko Sai's Librarian Script (Fixed for OpenClaw 2026.2.26)
# Logic: 12:15 interval (12:15 AM/PM)

def main():
    print("Ko Sai's Technical Distillation starting...")
    task = "Perform technical memory distillation for Topic 78 (Ko Sai). Update memory/00_Shared/02_Ko_Sai/02_Logs/ with technical health trends and error summaries. Sync with 00_INDEX.md."
    
    try:
        # Use 'openclaw agent' CLI to run the distillation turn
        subprocess.run(["openclaw", "agent", "--agent", "ko-sai", "--message", task], check=True)
        print("Ko Sai's Distillation successfully triggered.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
