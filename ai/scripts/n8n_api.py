#!/usr/bin/env python3
import os
import sys
import json
import argparse
import requests
from typing import Optional, Dict, Any

# --- Configuration ---
N8N_API_KEY = os.getenv("N8N_API_KEY")
N8N_BASE_URL = os.getenv("N8N_BASE_URL")

def die(msg: str, code: int = 1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)

API_BASE = ""
if N8N_BASE_URL:
    API_BASE = f"{N8N_BASE_URL.rstrip('/')}/api/v1"
HEADERS = {
    "X-N8N-API-KEY": N8N_API_KEY,
    "Content-Type": "application/json"
}

# --- API Functions ---
def list_workflows(active: Optional[bool] = None) -> Dict[str, Any]:
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    resp = requests.get(f"{API_BASE}/workflows", headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()

def get_workflow(workflow_id: str) -> Dict[str, Any]:
    resp = requests.get(f"{API_BASE}/workflows/{workflow_id}", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def activate_workflow(workflow_id: str, active: bool = True) -> Dict[str, Any]:
    resp = requests.patch(
        f"{API_BASE}/workflows/{workflow_id}",
        headers=HEADERS,
        json={"active": active}
    )
    resp.raise_for_status()
    return resp.json()

def list_executions(workflow_id: Optional[str] = None, limit: int = 20) -> Dict[str, Any]:
    params = {"limit": limit}
    if workflow_id:
        params["workflowId"] = workflow_id
    resp = requests.get(f"{API_BASE}/executions", headers=HEADERS, params=params)
    resp.raise_for_status()
    return resp.json()

def execute_workflow(workflow_id: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    payload = {"data": data} if data else {}
    resp = requests.post(f"{API_BASE}/workflows/{workflow_id}/execute", headers=HEADERS, json=payload)
    resp.raise_for_status()
    return resp.json()

# --- CLI Setup ---
def main():
    parser = argparse.ArgumentParser(description="n8n API CLI Tool (Cosmos Team)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # list-workflows
    lw = subparsers.add_parser("list-workflows", help="List all workflows")
    lw.add_argument("--active", type=str, choices=["true", "false"], help="Filter by active status")

    # get-workflow
    gw = subparsers.add_parser("get-workflow", help="Get workflow details")
    gw.add_argument("--id", required=True, help="Workflow ID")

    # activate / deactivate
    subp_act = subparsers.add_parser("activate", help="Activate a workflow")
    subp_act.add_argument("--id", required=True)
    subp_deact = subparsers.add_parser("deactivate", help="Deactivate a workflow")
    subp_deact.add_argument("--id", required=True)

    # list-executions
    le = subparsers.add_parser("list-executions", help="List recent executions")
    le.add_argument("--id", help="Filter by workflow ID")
    le.add_argument("--limit", type=int, default=20, help="Max results (default 20)")

    # execute
    ex = subparsers.add_parser("execute", help="Manually execute a workflow")
    ex.add_argument("--id", required=True, help="Workflow ID")
    ex.add_argument("--data", help="JSON data string for execution")

    args = parser.parse_args()

    if not N8N_API_KEY:
        die("N8N_API_KEY environment variable is required.")
    if not N8N_BASE_URL:
        die("N8N_BASE_URL environment variable is required.")

    try:
        result = None
        if args.command == "list-workflows":
            active_val = None
            if args.active: active_val = args.active == "true"
            result = list_workflows(active_val)
        elif args.command == "get-workflow":
            result = get_workflow(args.id)
        elif args.command == "activate":
            result = activate_workflow(args.id, True)
        elif args.command == "deactivate":
            result = activate_workflow(args.id, False)
        elif args.command == "list-executions":
            result = list_executions(args.id, args.limit)
        elif args.command == "execute":
            data_dict = json.loads(args.data) if args.data else None
            result = execute_workflow(args.id, data_dict)
        else:
            parser.print_help()
            return

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if args.command == "list-workflows":
                for wf in result.get("data", []):
                    status = "✅" if wf.get("active") else "❌"
                    print(f"{status} {wf.get('id')}: {wf.get('name')}")
            elif args.command == "list-executions":
                for ex in result.get("data", []):
                    status = "🟢" if ex.get("status") == "success" else "🔴"
                    print(f"{status} {ex.get('id')} | Workflow: {ex.get('workflowId')} | Started: {ex.get('startedAt')}")
            else:
                print(f"Success: {args.command} completed.")
                if result: print(json.dumps(result, indent=2))

    except Exception as e:
        die(str(e))

if __name__ == "__main__":
    main()
