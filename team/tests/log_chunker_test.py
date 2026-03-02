import json

def test_log_chunking():
    # Mock Logs: Actionable + General
    mock_logs = """
2026-03-01 10:00: INFO: System started.
2026-03-01 10:05: ERROR: Connection failed to database.
2026-03-01 10:10: INFO: User Nolan logged in.
2026-03-01 10:15: DECISION: Switched to AIDD framework.
2026-03-01 10:20: INFO: Background sync completed.
2026-03-01 10:25: GOAL: Finish Phase 3 by tonight.
2026-03-01 10:30: INFO: Cleaning up temporary files.
    """
    
    # Simple Python implementation of our JS logic for testing
    priority_keywords = ["error", "fix", "decision", "preference", "goal", "update"]
    lines = mock_logs.strip().split('\n')
    
    priority_lines = [l for l in lines if any(kw in l.lower() for kw in priority_keywords)]
    general_lines = [l for l in lines if not any(kw in l.lower() for kw in priority_keywords)]
    
    print("--- Original Logs ---")
    print(mock_logs)
    
    print("\n--- Processed (Priority Only Test) ---")
    for line in priority_lines:
        print(f"DEBUG: Found Priority -> {line}")
    
    print("\n--- Final Balanced Output Simulation ---")
    # Simulating the balance (All Priority + Recent General)
    final = priority_lines + general_lines[-2:] 
    for line in final:
        print(line)

if __name__ == "__main__":
    test_log_chunking()
