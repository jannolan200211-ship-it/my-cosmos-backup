#!/usr/bin/python3
import subprocess
import os

# Ko Sai's Librarian Script
# Logic: 12:15 interval (12:15 AM/PM)
# Task: Summarize VPS logs, health trends, and technical errors.

def main():
    print("Ko Sai's Technical Distillation starting...")
    # Triggering the technical distillation via subagent spawn
    # This keeps the technical context separated from David's.
    task = "Perform technical memory distillation. Review logs from today. Update memory/ko_sai/ with technical health trends and error summaries."
    
    try:
        # Use openclaw command to spawn the distillation task
        subprocess.run(["openclaw", "subagents", "spawn", "ko_sai", task], check=True)
        print("Ko Sai's Distillation successfully triggered.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
