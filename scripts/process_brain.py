import os
import subprocess
import json
from pathlib import Path

BRAIN_PATH = "/root/nolan-brain"
INBOX_FILE = Path(BRAIN_PATH) / "inbox.md"

def run_command(cmd, cwd=None):
    return subprocess.run(cmd, shell=True, capture_with_output=True, text=True, cwd=cwd)

def process_brain():
    if not os.path.exists(BRAIN_PATH):
        print(f"Error: {BRAIN_PATH} not found.")
        return

    # 1. Pull latest changes
    print("Pulling latest changes from GitHub...")
    subprocess.run("git pull origin main", shell=True, cwd=BRAIN_PATH)

    if not INBOX_FILE.exists():
        print("Inbox is empty. Nothing to process.")
        return

    content = INBOX_FILE.read_text().strip()
    if not content:
        print("Inbox is empty. Nothing to process.")
        return

    # 2. Split entries (Assuming --- as delimiter)
    entries = [e.strip() for e in content.split("---") if e.strip()]
    
    if not entries:
        print("No valid entries found in inbox.")
        return

    print(f"Found {len(entries)} entries to process.")

    # Note: The actual AI categorization will be handled by David (the agent) 
    # during the cron job execution by calling this script or piping output.
    # For now, we'll just print them for David to see and handle.
    
    for i, entry in enumerate(entries, 1):
        print(f"\n[ENTRY {i}]\n{entry}\n[END ENTRY]")

    # We don't clear the inbox here; David will do it after successful categorization.

if __name__ == "__main__":
    process_brain()
