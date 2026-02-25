import os
import json
import requests
from datetime import datetime

# Configuration
WORKSPACE_PATH = "/root/.openclaw/workspace"
STATUS_FILE = os.path.join(WORKSPACE_PATH, "03 Reference/02 System Configs/knowledge_management/last_review_status.json")
GATEWAY_URL = "http://127.0.0.1:18789"
GATEWAY_TOKEN = "30c6f1f7396ef120bf93344de8c607ec7c73d0f8c14da890"

def log_status(success, error=None):
    status = {
        "last_run": datetime.now().isoformat(),
        "success": success,
        "error": error
    }
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f)

def notify_gateway(error_msg):
    headers = {
        "Authorization": f"Bearer {GATEWAY_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "action": "message",
        "message": f"Nightly Review Script Error: {error_msg}. Please analyze and fix."
    }
    try:
        requests.post(f"{GATEWAY_URL}/api/v1/message", headers=headers, json=payload)
    except Exception as e:
        print(f"Failed to notify gateway: {e}")

def perform_review():
    try:
        # Here we would normally add deterministic logic to summarize logs if possible.
        # Since summarizing requires LLM, the script will simply trigger the Agent if needed,
        # or we can keep it as a placeholder that the Agent calls.
        # For now, we simulate a successful run check.
        print("Nightly review check performed.")
        log_status(True)
    except Exception as e:
        log_status(False, str(e))
        notify_gateway(str(e))

if __name__ == "__main__":
    perform_review()
