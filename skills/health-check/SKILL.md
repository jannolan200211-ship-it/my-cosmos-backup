---
name: health-check
description: Comprehensive system health monitoring and status classification for OpenClaw VPS deployments. Use when the user asks for a health check, system status, or when automated cron jobs report issues. Classifies health as OK, WARN, FAIL, or UNKNOWN based on the 5-core-check Status Classification Protocol.
---

# Health Check Skill

This skill implements the **Status Classification Protocol** (5 Core Checks) for VPS deployments.

## Workflow

1. **Gather Data**: Run `scripts/check.sh` to get raw system data.
2. **Read Protocol**: Load `references/STATUS_PROTOCOL.md` to review status thresholds and classification rules.
3. **Classify Status**: Analyze the gathered data against the protocol thresholds.
4. **Report**: Deliver a status report in Myanmar language.

## 5 Core Health Checks

The skill analyzes the following subsystems:

1. **Gateway Process**: Is the OpenClaw gateway running?
2. **Disk Space**: Is there sufficient disk space (threshold: 85%/95%)?
3. **OpenClaw Status**: Are the channels and services online?
4. **Error Logs**: Are there too many recent errors in the logs?
5. **Session Size**: Are any session files dangerously large (>5MB)?

## Output Guidelines

- **If OK**: Provide a brief, natural confirmation in Myanmar.
- **If WARN/FAIL**: Provide a detailed report, identifying the specific subsystem, and list remediation steps in Myanmar.

## Automated Execution

This skill is also configured to run periodically via Cron (every 12 hours) using the `gemini-3-flash` model for cost efficiency.
