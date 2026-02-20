# Cloudflare Telegram Bot Workflow (Nolan's Standard)

This workflow is optimized for building autonomous Telegram bots on Cloudflare Workers that integrate with GitHub for long-term storage (Second Brain).

## 1. Credentials Gathering
- **Telegram:** Get a bot token from `@BotFather`.
- **Cloudflare:** Create an API Token with `Edit Cloudflare Workers` permissions at [dash.cloudflare.com](https://dash.cloudflare.com/profile/api-tokens).
- **GitHub:** Create a Personal Access Token (PAT) with `repo` scope at [github.com/settings/tokens](https://github.com/settings/tokens).

## 2. Local Project Setup (VPS)
- Create a directory for the bot.
- Initialize `wrangler.json` with project name and compatibility date.
- Create `src/index.js` for the main logic.

## 3. Integration Logic
- **Telegram Webhook:** Include a `/setup` endpoint in the Worker to call `setWebhook` automatically.
- **Environment Variables:** Store `TELEGRAM_TOKEN` and `GITHUB_TOKEN` in `wrangler.json` (or use `wrangler secret put`).
- **GitHub Sync:** Use the GitHub API within the Worker to push incoming data to a specific repository (e.g., `inbox.md`).

## 4. Deployment & Activation
- Use `wrangler deploy` with the `CLOUDFLARE_API_TOKEN` exported.
- Call the `/setup` endpoint once to link Telegram to the Worker.

## 5. Processing (OpenClaw Side)
- Set up a **Cron Job** in OpenClaw to process the GitHub data periodically (e.g., daily at 02:00 AM).
- Use an agent (David) to categorize the data and move it from `inbox.md` to structured files.

---
*Reference: Setup completed on 2026-02-20 for Brain5000 Bot.*
