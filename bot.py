# bot.py
import telebot
import subprocess
import threading

BOT_TOKEN = "8058304193:AAHK6jt0s7L2Qg8S_dxdzeuWBhHfyMn5PYc"
OWNER_ID = 1730899531

bot = telebot.TeleBot(BOT_TOKEN)

def run_attack(ip, port, sec):
    subprocess.call(["python3", "loadtest.py", ip, port, sec])

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "🔥 Vijay Load Test Bot चालू आहे!\nकमांड:\n`/attack <ip> <port> <sec>`\n`/stop`")
    else:
        bot.reply_to(message, "तुला access नाही ❌")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "❌ फक्त Admin वापरू शकतो")
        return
    try:
        _, ip, port, sec = message.text.split()
        t = threading.Thread(target=run_attack, args=(ip, port, sec))
        t.start()
        bot.reply_to(message, f"🚀 Attack सुरू!\nIP: {ip}\nPort: {port}\nवेळ: {sec} सेकंद")
    except:
        bot.reply_to(message, "❌ Format: /attack <ip> <port> <sec>")

bot.polling()