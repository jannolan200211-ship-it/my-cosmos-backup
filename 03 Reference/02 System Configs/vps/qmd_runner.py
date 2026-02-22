import sys
import os
import json
import yaml
import re
import subprocess
from pathlib import Path

def run_qmd_skill(skill_path, context):
    """
    Parses a QMD markdown file and executes the embedded Python code.
    """
    path = Path(skill_path)
    if not path.exists():
        return {"success": False, "error": f"Skill file not found: {skill_path}"}
    
    content = path.read_text()
    
    # Extract YAML frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return {"success": False, "error": "No YAML frontmatter found."}
    
    # Extract Python code block
    code_match = re.search(r'```python\n(.*?)\n```', content, re.DOTALL)
    if not code_match:
        return {"success": False, "error": "No Python code block found."}
    
    code = code_match.group(1)
    
    # Run the code in a subprocess
    try:
        process = subprocess.run(
            [sys.executable, "-c", code],
            input=json.dumps(context),
            text=True,
            capture_output=True,
            timeout=30
        )
        
        if process.returncode != 0:
            return {"success": False, "error": process.stderr}
        
        try:
            result = json.loads(process.stdout.strip())
            return {"success": True, "result": result}
        except json.JSONDecodeError:
            return {"success": True, "result": process.stdout.strip()}
            
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Skill execution timed out."}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"success": False, "error": "Usage: qmd_runner.py <skill_path> <context_json>"}))
        sys.exit(1)
    
    skill_file = sys.argv[1]
    try:
        context_data = json.loads(sys.argv[2])
    except:
        context_data = {"message": sys.argv[2]}
        
    print(json.dumps(run_qmd_skill(skill_file, context_data)))
