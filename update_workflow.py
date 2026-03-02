import os
import json
import requests

def update_n8n_workflow():
    api_key = os.getenv("N8N_API_KEY")
    base_url = os.getenv("N8N_BASE_URL").rstrip('/')
    workflow_id = "Ees5kEdheiIckOUy"
    
    # Load original
    with open('workflow_backup.json', 'r') as f:
        workflow = json.load(f)

    # 1. Update AI Distiller with System Prompt (Micro-Task 3.1)
    with open('ai/custom/memory_distiller_v1.md', 'r') as f:
        system_prompt = f.read()
    
    for node in workflow['nodes']:
        if node['name'] == "AI Distiller":
            node['parameters']['systemMessage'] = system_prompt
            # Ensure it takes the logs correctly
            node['parameters']['prompt'] = "={{ \$json.processedLogs }}"

    # 2. Add Log Chunker Node (Micro-Task 3.2)
    with open('ai/custom/n8n/log_chunker.js', 'r') as f:
        chunker_code = f.read()
    
    chunker_node = {
        "parameters": {
            "jsCode": chunker_code
        },
        "id": "log-chunker",
        "name": "Log Chunker (3.2)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 1,
        "position": [1030, 224]
    }
    workflow['nodes'].append(chunker_node)

    # 3. Add Report Formatter Node (Micro-Task 3.3)
    with open('ai/custom/n8n/report_formatter.js', 'r') as f:
        formatter_code = f.read()
    
    formatter_node = {
        "parameters": {
            "jsCode": formatter_code
        },
        "id": "report-formatter",
        "name": "Report Formatter (3.3)",
        "type": "n8n-nodes-base.code",
        "typeVersion": 1,
        "position": [1350, 224]
    }
    workflow['nodes'].append(formatter_node)

    # 4. Fix Connections
    # Read File Content -> Log Chunker -> AI Distiller -> Report Formatter
    workflow['connections']['Read File Content']['main'] = [[{"node": "Log Chunker (3.2)", "type": "main", "index": 0}]]
    workflow['connections']['Log Chunker (3.2)'] = {"main": [[{"node": "AI Distiller", "type": "main", "index": 0}]]}
    workflow['connections']['AI Distiller']['main'] = [[{"node": "Report Formatter (3.3)", "type": "main", "index": 0}]]

    # 5. Push to n8n
    resp = requests.put(
        f"{base_url}/api/v1/workflows/{workflow_id}",
        headers={"X-N8N-API-KEY": api_key, "Content-Type": "application/json"},
        json={"nodes": workflow['nodes'], "connections": workflow['connections']}
    )
    
    if resp.status_code == 200:
        print("✅ Workflow updated successfully via API.")
    else:
        print(f"❌ Failed to update: {resp.status_code} {resp.text}")

if __name__ == "__main__":
    update_n8n_workflow()
