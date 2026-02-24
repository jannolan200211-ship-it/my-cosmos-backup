# Knowledge Management System (Tiago Forte Based)

This system implements a Second Brain using the P.A.R.A. method and Daily Logging.

## 1. P.A.R.A. Structure
- **Projects:** Active tasks with a deadline (Location: `02 Work/02 Projects/`)
- **Areas:** Ongoing responsibilities with no end date (Location: `01 Personal/` or `02 Work/03 Operations/`)
- **Resources:** Interests and topics of ongoing research (Location: `03 Reference/`)
- **Archives:** Completed or inactive items (Location: `99 Archive/`)

## 2. Daily Note System
- **Daily Note:** Created/Updated daily in `01 Personal/01 Daily Notes/YYYY-MM-DD.md`.
- **Content:** Logs of decisions, important info, and task progress.

## 3. Nightly Review (Cron)
- **Job Name:** Nightly Knowledge Sync
- **Time:** 23:55 (Asia/Yangon)
- **Action:** Review session logs, update `MEMORY.md`, and summarize into the Daily Note.
