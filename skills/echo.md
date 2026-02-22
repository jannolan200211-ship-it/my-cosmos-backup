---
name: echo
version: 1.0.0
description: Echo back the user's message
triggers:
  - keyword: echo
  - command: /echo
---

# Echo Skill
Repeats what you say.

## Code
```python
import sys
import json

def main():
    try:
        data = json.loads(sys.stdin.read())
        msg = data.get('message', '')
        # Clean trigger
        for t in ['echo', '/echo']:
            msg = msg.replace(t, '', 1).strip()
        
        print(json.dumps({"content": f"🔊 Echo: {msg}"}))
    except:
        print(json.dumps({"content": "Error in echo skill"}))

if __name__ == "__main__":
    main()
```
