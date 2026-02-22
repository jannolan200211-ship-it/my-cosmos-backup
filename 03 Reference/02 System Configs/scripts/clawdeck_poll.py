#!/usr/bin/env python3
import os
import requests
import json

API_URL = "https://clawdeck.io/api/v1"
TOKEN = "928369817463d1815c8a3d2be15e391f98b5e00cbee4aa87c344e4698dd6e531"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "X-Agent-Name": "David",
    "X-Agent-Emoji": "Lobster",
    "Content-Type": "application/json"
}

def get_assigned_tasks():
    try:
        response = requests.get(f"{API_URL}/tasks?assigned=true", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []

def update_task_status(task_id, status):
    try:
        response = requests.patch(
            f"{API_URL}/tasks/{task_id}",
            headers=HEADERS,
            data=json.dumps({"status": status})
        )
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Error updating task {task_id}: {e}")
        return False

if __name__ == "__main__":
    tasks = get_assigned_tasks()
    if tasks:
        print(json.dumps(tasks, indent=2))
    else:
        print("No assigned tasks found.")
