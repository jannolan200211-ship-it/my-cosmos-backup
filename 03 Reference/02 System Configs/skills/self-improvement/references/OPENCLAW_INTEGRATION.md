# OpenClaw Integration
Complete setup and usage guide for integrating the self-improvement skill with OpenClaw.

## Overview
OpenClaw uses workspace-based prompt injection combined with event-driven hooks. Context is injected from workspace files at session start, and hooks can trigger on lifecycle events.

## Workspace Structure
```
~/.openclaw/
├── workspace/      # Working directory
│   ├── AGENTS.md   # Multi-agent coordination patterns
│   ├── SOUL.md     # Behavioral guidelines and personality
│   ├── TOOLS.md    # Tool capabilities and gotchas
│   ├── MEMORY.md   # Long-term memory (main session only)
│   └── memory/     # Daily memory files
│       └── YYYY-MM-DD.md
├── skills/         # Installed skills
│   └── <skill-name>/
│       └── SKILL.md
└── hooks/          # Custom hooks
    └── <hook-name>/
        ├── HOOK.md
        └── handler.ts
```

## Quick Setup

### 1. Install the Skill
```bash
clawdhub install self-improving-agent
```
Or copy manually:
```bash
cp -r self-improving-agent ~/.openclaw/skills/
```

### 2. Install the Hook (Optional)
Copy the hook to OpenClaw's hooks directory:
```bash
cp -r hooks/openclaw ~/.openclaw/hooks/self-improvement
```
Enable the hook:
```bash
openclaw hooks enable self-improvement
```

### 3. Create Learning Files
Create the `.learnings/` directory in your workspace:
```bash
mkdir -p ~/.openclaw/workspace/.learnings
```

## Injected Prompt Files

### AGENTS.md
Purpose: Multi-agent workflows and delegation patterns.
```markdown
# Agent Coordination
## Delegation Rules
- Use explore agent for open-ended codebase questions
- Spawn sub-agents for long-running tasks
- Use sessions_send for cross-session communication
```

### SOUL.md
Purpose: Behavioral guidelines and communication style.
```markdown
# Behavioral Guidelines
## Communication Style
- Be direct and concise
- Avoid unnecessary caveats and disclaimers
- Use technical language appropriate to context
```

### TOOLS.md
Purpose: Tool knowledge and integration gotchas.
```markdown
# Tool Knowledge
## Self-Improvement Skill
Log learnings to `.learnings/` for continuous improvement.
```

## Learning Workflow

### Capturing Learnings
1. **In-session**: Log to `.learnings/` as usual
2. **Cross-session**: Promote to workspace files

### Promotion Decision Tree
```
Is the learning project-specific?
├── Yes → Keep in .learnings/
└── No → Is it behavioral/style-related?
    ├── Yes → Promote to SOUL.md
    └── No → Is it tool-related?
        ├── Yes → Promote to TOOLS.md
        └── No → Promote to AGENTS.md (workflow)
```

## Available Hook Events
| Event | When It Fires |
|-------|---------------|
| `agent:bootstrap` | Before workspace files inject |
| `command:new` | When `/new` command issued |
| `gateway:startup` | When gateway starts |

## Verification
Check hook is registered:
```bash
openclaw hooks list
```
Check skill is loaded:
```bash
openclaw status
```
