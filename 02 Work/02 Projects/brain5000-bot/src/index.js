export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Endpoint to setup webhook
    if (url.pathname === "/setup") {
      const webhookUrl = `https://${url.hostname}/webhook`;
      const tgUrl = `https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/setWebhook?url=${encodeURIComponent(webhookUrl)}`;
      const response = await fetch(tgUrl);
      return new Response(await response.text());
    }

    // Handle incoming Telegram Webhook
    if (request.method === "POST" && url.pathname === "/webhook") {
      try {
        const payload = await request.json();
        if (payload.message && payload.message.text) {
          const text = payload.message.text;
          const fromUser = payload.message.from.username || payload.message.from.first_name;
          const chatId = payload.message.chat.id;

          // 1. Save to GitHub with Error Handling and YAML Safety
          const saveResult = await saveToGitHub(text, fromUser, env);

          // 2. Notify User of result
          let responseText = "Brain5000: မှတ်သားပြီးပါပြီ Nolan! ✅";
          if (!saveResult.success) {
            responseText = `Brain5000 Error ❌: ${saveResult.error}`;
          }

          await fetch(`https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/sendMessage`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ chat_id: chatId, text: responseText })
          });
        }
        return new Response("OK");
      } catch (e) {
        console.error("Worker Crash:", e.message);
        return new Response("Internal Server Error", { status: 500 });
      }
    }

    return new Response("Brain5000 Pro is Running.");
  }
};

async function saveToGitHub(content, user, env, retryCount = 0) {
  const GITHUB_TOKEN = env.GITHUB_TOKEN;
  const REPO = "jannolan200211-ship-it/nolan-second-brain";
  const FILE_PATH = "inbox.md";
  const timestamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Yangon' });

  try {
    // 1. Get current file state
    const getRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
      headers: {
        "Authorization": `token ${GITHUB_TOKEN}`,
        "User-Agent": "Brain5000-Pro",
        "Accept": "application/vnd.github.v3+json"
      }
    });

    let oldContent = "";
    let sha = "";
    if (getRes.ok) {
      const data = await getRes.json();
      oldContent = decodeBase64(data.content);
      sha = data.sha;
    }

    // 2. YAML Safety: Use block scalar | and indent content
    // This prevents colons, quotes, etc. from breaking the YAML structure
    const indentedContent = content.split('\n').map(line => '    ' + line).join('\n');
    const entry = `\n---\nauthor: "${user}"\ntime: "${timestamp}"\ncontent: |\n${indentedContent}\n`;
    const newContent = oldContent + entry;

    // 3. Update file on GitHub
    const putRes = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
      method: "PUT",
      headers: {
        "Authorization": `token ${GITHUB_TOKEN}`,
        "User-Agent": "Brain5000-Pro",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: `Brain Sync: ${timestamp}`,
        content: encodeBase64(newContent),
        sha: sha
      })
    });

    if (putRes.ok) {
      return { success: true };
    }

    // Handle Race Condition (409 Conflict)
    const errorData = await putRes.json();
    if (putRes.status === 409 && retryCount < 3) {
      console.log(`Conflict detected, retrying... (${retryCount + 1})`);
      return await saveToGitHub(content, user, env, retryCount + 1);
    }

    return { success: false, error: errorData.message || "GitHub Upload Failed" };

  } catch (error) {
    return { success: false, error: error.message };
  }
}

// Professional Base64 helpers for Cloudflare Workers (V8)
function encodeBase64(str) {
  const bytes = new TextEncoder().encode(str);
  const binString = String.fromCodePoint(...bytes);
  return btoa(binString);
}

function decodeBase64(base64) {
  const binString = atob(base64);
  const bytes = Uint8Array.from(binString, (m) => m.codePointAt(0));
  return new TextDecoder().decode(bytes);
}
