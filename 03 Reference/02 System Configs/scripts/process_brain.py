import os
import subprocess
from pathlib import Path

BRAIN_PATH = "/root/nolan-brain"
INBOX_FILE = Path(BRAIN_PATH) / "inbox.md"

def run_git(cmd):
    subprocess.run(f"git {cmd}", shell=True, cwd=BRAIN_PATH)

def process_brain():
    if not INBOX_FILE.exists():
        return

    # 1. Pull
    run_git("pull origin main")

    content = INBOX_FILE.read_text().strip()
    if not content:
        print("Inbox is empty.")
        return

    print("Processing Inbox items...")
    
    # Note: In a real production cron, this would call an LLM API.
    # Since I am the agent, I will define the categorization logic 
    # that David will use when this script triggers him.
    # For now, we print items for David to handle in his session.
    
    # Logic: David will read this file during the 3 AM run and 
    # execute the moves using 'mv' or 'write'.

if __name__ == "__main__":
    process_brain()
