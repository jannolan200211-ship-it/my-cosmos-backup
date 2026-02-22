#!/usr/bin/env python3
import json
import os
import time

SESSIONS_FILE = "/root/.openclaw/agents/main/sessions/sessions.json"
OUTPUT_FILE = "/root/.openclaw/workspace/state/llm-routing.json"

def calculate_usage():
    try:
        with open(SESSIONS_FILE, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, dict) and "sessions" in data:
            sessions = data.get("sessions", [])
        elif isinstance(data, dict):
            sessions = list(data.values())
        else:
            sessions = []
            
        gemini_tokens = 0
        local_tasks = 0
        local_tokens = 0
        active_sessions = []
        
        now_ms = time.time() * 1000
        
        for s in sessions:
            # Main session stats
            if s.get("modelProvider") == "google-antigravity":
                gemini_tokens += s.get("totalTokens", 0)
            elif s.get("modelProvider") == "ollama":
                local_tasks += 1
                local_tokens += s.get("totalTokens", 0)
            
            # Check if session is active (last updated within 30 minutes)
            updated_at = s.get("updatedAt", 0)
            if now_ms - updated_at < 30 * 60 * 1000:
                active_sessions.append(s.get("sessionId"))

            # Check individual messages in jsonl for mixed usage if needed
            # For now, we'll keep it simple and use session-level stats
        
        # Mapping to the structure Jon Tsai's dashboard expects
        total_tokens = gemini_tokens + local_tokens
        gemini_used_pct = min(1.0, gemini_tokens / 1000000.0)
        
        usage_data = {
            "claude": {
                "session": {
                    "used_pct": gemini_used_pct,
                    "remaining_pct": 1.0 - gemini_used_pct,
                    "resets_in": "Daily"
                },
                "weekly_all_models": {
                    "used_pct": gemini_used_pct,
                    "remaining_pct": 1.0 - gemini_used_pct,
                    "resets": "Sunday"
                },
                "last_synced": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            },
            "codex": {
                "sessions_today": local_tasks,
                "tasks_today": local_tasks,
                "usage_5h_pct": min(100, int((local_tokens / 50000) * 100)) if local_tokens > 0 else 5,
                "usage_day_pct": min(100, int((local_tokens / 200000) * 100)) if local_tokens > 0 else 5
            },
            "routing": {
                "total_tasks": len(sessions),
                "claude_tasks": len(sessions) - local_tasks,
                "codex_tasks": local_tasks,
                "claude_pct": int(((len(sessions) - local_tasks) / len(sessions)) * 100) if sessions else 100,
                "codex_pct": int((local_tasks / len(sessions)) * 100) if sessions else 0
            }
        }
        
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(usage_data, f, indent=2)
            
        print(f"Updated dashboard usage with {total_tokens} tokens.")
        
    except Exception as e:
        print(f"Error updating usage: {e}")

if __name__ == "__main__":
    calculate_usage()
