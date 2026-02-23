import telebot
import json
import sqlite3
import os

# Configuration
BASE_DIR = "/root/.openclaw/workspace/02 Work/02 Projects/vpn-agency-bot"
TOKENS_PATH = os.path.join(BASE_DIR, "tokens.json")
DB_PATH = os.path.join(BASE_DIR, "vpn_agency.db")

# Load Token
def load_token():
    with open(TOKENS_PATH, 'r') as f:
        tokens = json.load(f)
        return tokens.get("customer_bot_token")

TOKEN = load_token()
bot = telebot.TeleBot(TOKEN)

# Database Setup
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Check if table exists, if not create it
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER PRIMARY KEY,
            username TEXT,
            full_name TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    
    # Ensure all required columns exist (if table was created before)
    cursor.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    if 'joined_at' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        conn.commit()
    conn.close()

def save_user(chat_id, username, full_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO users (chat_id, username, full_name)
        VALUES (?, ?, ?)
    ''', (chat_id, username, full_name))
    conn.commit()
    conn.close()

# Bot Handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    full_name = f"{first_name} {last_name}".strip()
    
    # Save user to DB
    save_user(chat_id, username, full_name)
    
    # Create Keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_buy = telebot.types.KeyboardButton('🇲🇲 Buy VPN')
    btn_check = telebot.types.KeyboardButton('📊 Check Expiry')
    btn_support = telebot.types.KeyboardButton('☎️ Support')
    markup.add(btn_buy, btn_check, btn_support)
    
    welcome_text = (
        f"Mingalaba {full_name or 'there'}! 🙏\n"
        "Welcome to our VPN Service. How can we help you today?"
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '🇲🇲 Buy VPN':
        bot.reply_to(message, "Pricing plans coming soon! 🚀")
    elif message.text == '📊 Check Expiry':
        bot.reply_to(message, "You don't have an active subscription yet.")
    elif message.text == '☎️ Support':
        bot.reply_to(message, "Please contact our admin for support.")

if __name__ == "__main__":
    print("Initializing Database...")
    init_db()
    print("Bot is starting...")
    bot.infinity_polling()
