---
name: token-saver
version: 1.0.0
description: Calculate potential token savings using QMD skills
triggers:
  - keyword: token savings
---

# Token Saver Info
Calculates how many tokens you save by using QMD.

## Code
```python
import sys
import json

def main():
    # Average code block in context: 500-1000 tokens
    # QMD metadata in context: 50 tokens
    # Savings per execution: ~450-950 tokens
    
    savings_report = """
📊 **Token Savings Report**
-------------------------
Standard Skill: ~800 tokens (Full code in context)
QMD Skill: ~50 tokens (Metadata only)

✨ **Estimated Savings: 94% per skill**
    """
    print(json.dumps({"content": savings_report.strip()}))

if __name__ == "__main__":
    main()
```
