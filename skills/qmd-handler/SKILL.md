---
name: qmd-handler
description: "Execute QMD (Quick Markdown) skills. These skills are standalone markdown files containing metadata and Python code. Use this to run pre-defined logic (like search, math, or API calls) without having to write the code yourself, saving context tokens."
---

# QMD Handler

Use this skill to execute deterministic logic stored in `.md` files.

## How to use

1. **Find a skill**: Look in `skills/` for `.md` files.
2. **Execute**: Use the `qmd_runner.py` script.

```bash
python3 vps/qmd_runner.py skills/your-skill.md '{"param": "value"}'
```

## Benefits
- **Token Efficiency**: The code lives on disk, not in your context window.
- **Reliability**: Deterministic Python execution.
- **Safety**: Runs in a separate subprocess.
