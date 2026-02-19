export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Handle Webhook Setup (optional utility)
    if (url.pathname === "/setup") {
      const webhookUrl = `https://${url.hostname}/webhook`;
      const tgUrl = `https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/setWebhook?url=${encodeURIComponent(webhookUrl)}`;
      const response = await fetch(tgUrl);
      return new Response(await response.text());
    }

    // Handle Incoming Telegram Updates
    if (request.method === "POST" && url.pathname === "/webhook") {
      try {
        const payload = await request.json();
        if (payload.message && payload.message.text) {
          const chatId = payload.message.chat.id;
          const text = payload.message.text;
          const firstName = payload.message.from.first_name;

          let responseText = "";
          if (text.toLowerCase() === "/start") {
            responseText = `မင်္ဂလာပါ ${firstName}! ကျွန်တော်က Brain5000 Bot ပါ။ Cloudflare Workers ပေါ်မှာ အောင်မြင်စွာ တည်ဆောက်ပြီးပါပြီ။ 🚀`;
          } else {
            responseText = `Nolan ရဲ့ Brain5000 Bot က ပြန်ပြောလိုက်ပါတယ်: "${text}"`;
          }

          const sendUrl = `https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/sendMessage`;
          await fetch(sendUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              chat_id: chatId,
              text: responseText
            })
          });
        }
      } catch (e) {
        return new Response("Error: " + e.message, { status: 500 });
      }
    }

    return new Response("Brain5000 is Alive!");
  },
};
