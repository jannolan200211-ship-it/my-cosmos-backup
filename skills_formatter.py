import json

try:
    with open('skills_data.json', 'r') as f:
        data = json.load(f)
    
    print("# OpenClaw System Skills List\n")
    print("| Status | Skill Name | Description | Source |")
    print("| :--- | :--- | :--- | :--- |")
    
    for skill in data.get('skills', []):
        status = "✅ Ready" if skill.get('eligible') else "❌ Missing"
        name = skill.get('name', 'N/A')
        desc = skill.get('description', 'No description').replace('\n', ' ')
        source = skill.get('source', 'N/A')
        print(f"| {status} | **{name}** | {desc} | {source} |")
        
except Exception as e:
    print(f"Error: {e}")
