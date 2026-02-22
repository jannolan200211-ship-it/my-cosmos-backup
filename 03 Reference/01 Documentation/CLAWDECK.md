# CLAWDECK.md - Task Dashboard Configuration

## Connection
- **API URL:** `https://clawdeck.io/api/v1`
- **Token:** `928369817463d1815c8a3d2be15e391f98b5e00cbee4aa87c344e4698dd6e531`
- **Headers:**
  - `Authorization: Bearer 928369817463d1815c8a3d2be15e391f98b5e00cbee4aa87c344e4698dd6e531`
  - `X-Agent-Name: David`
  - `X-Agent-Emoji: Lobster`

## Workflow
1. **Polling:** Every 30s or on heartbeat, call `GET /tasks?assigned=true`.
2. **Execution:** Pick the oldest task, move to `in_progress`.
3. **Updates:** Use `blocked: true` if stuck, move to `in_review` or `done` when finished.

## Statuses
`inbox`, `up_next`, `in_progress`, `in_review`, `done`
