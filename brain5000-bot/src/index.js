export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Setup endpoint to set Telegram Webhook
    if (url.pathname === "/setup") {
      const webhookUrl = `https://${url.hostname}/webhook`;
      const tgUrl = `https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/setWebhook?url=${encodeURIComponent(webhookUrl)}`;
      const response = await fetch(tgUrl);
      return new Response(await response.text());
    }

    // Handle incoming Telegram updates
    if (request.method === "POST" && url.pathname === "/webhook") {
      try {
        const payload = await request.json();
        
        if (payload.message && payload.message.text) {
          const chatId = payload.message.chat.id;
          const text = payload.message.text;
          const fromUser = payload.message.from.username || payload.message.from.first_name;

          // 1. Save to GitHub Inbox
          await saveToGitHub(text, fromUser, env);

          // 2. Reply to user
          const responseText = "Brain5000: မှတ်သားပြီးပါပြီ Nolan! ✅ ဒီနေ့ညမှာ David က စနစ်တကျ ခွဲခြားသိမ်းဆည်းပေးပါလိမ့်မယ်။";
          await fetch(`https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/sendMessage`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ chat_id: chatId, text: responseText })
          });
        }
        return new Response("OK");
      } catch (e) {
        return new Response("Error: " + e.message, { status: 500 });
      }
    }

    return new Response("Brain5000 is running as Nolan's Second Brain.");
  }
};

async function saveToGitHub(content, user, env) {
  const GITHUB_TOKEN = env.GITHUB_TOKEN;
  const REPO = "jannolan200211-ship-it/nolan-second-brain";
  const FILE_PATH = "inbox.md";
  const timestamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Yangon' });

  // 1. Get current file state (for SHA)
  const getRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
    headers: {
      "Authorization": `token ${GITHUB_TOKEN}`,
      "User-Agent": "Brain5000-Worker",
      "Accept": "application/vnd.github.v3+json"
    }
  });

  let oldContent = "";
  let sha = "";
  if (getRes.ok) {
    const data = await getRes.json();
    oldContent = b64_to_utf8(data.content);
    sha = data.sha;
  }

  // 2. Prepare new content with entry metadata
  const entry = `\n---\n> **From:** ${user}\n> **Time:** ${timestamp}\n\n${content}\n`;
  const newContent = oldContent + entry;

  // 3. Update file on GitHub
  const putRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
    method: "PUT",
    headers: {
      "Authorization": `token ${GITHUB_TOKEN}`,
      "User-Agent": "Brain5000-Worker",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: `Brain Entry: ${timestamp}`,
      content: utf8_to_b64(newContent),
      sha: sha
    })
  });

  if (!putRes.ok) {
    const errorText = await putRes.text();
    throw new Error(`GitHub API Error: ${errorText}`);
  }
}

// Helper functions for base64 encoding/decoding
function utf8_to_b64(str) {
  return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, (match, p1) => String.fromCharCode('0x' + p1)));
}

function b64_to_utf8(str) {
  return decodeURIComponent(atob(str).split('').map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)).join(''));
}
