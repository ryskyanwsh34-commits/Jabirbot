import os
import telebot
import yt_dlp

TOKEN = "8452831676:AAHGol2Q-Z-RqanH9yz7LueTG9ejQX4te0A"
ADMIN_ID = 6467716023

bot = telebot.TeleBot(TOKEN)

def download_video(url, output="video.mp4"):
    try:
        ydl_opts = {
            'outtmpl': output,
            'quiet': True,
            'format': 'mp4/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output
    except:
        return None

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,
                 "🎥 سلام جگر!\nلینک YouTube, TikTok یا Facebook بده تا ویدیو دانلود کنم🔥")

@bot.message_handler(func=lambda m: True)
def handle(msg):
    url = msg.text.strip()

    if not any(x in url for x in ["youtube", "youtu", "tiktok", "facebook"]):
        bot.reply_to(msg, "❌ لینک معتبر نیست جگر 😔")
        return

    bot.reply_to(msg, "⏳ دارم دانلود میکنم، صبر کن جگرم...")

    name = "video.mp4"
    result = download_video(url, name)

    if result:
        bot.send_video(msg.chat.id, open(name, "rb"))
        os.remove(name)
    else:
        bot.reply_to(msg, "⚠ دانلود نشد! شاید لینک محدود است.")

bot.infinity_polling()
