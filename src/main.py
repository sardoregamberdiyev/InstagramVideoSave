import telebot
from selenium.common.exceptions import TimeoutException
from lib.reel import is_instagram_reels_url, download_reels

bot = telebot.TeleBot("5813050765:AAGRm_cTWB7WGtNBYI5CoGRriGqxi5GK-3Y", parse_mode=None)


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    if not is_instagram_reels_url(message.text):

        bot.reply_to(message, "Kechirasiz, berilgan url yaroqsiz 🥲")

    else:

        bot.send_message(message.chat.id, "Iltimos kuting ! \nVideoga ishlov berilmoqda 🔄")

        bot.send_chat_action(message.chat.id, action="upload_video")

        try:
            bot.send_video(message.chat.id, download_reels(message.text))
        except TimeoutException:
            bot.send_message(message.chat.id, "Videoni yuklab bo‘lmadi\n\n"
                                              "Berilgan url haqiqiy ekanligiga ishonch hosil qiling !")


bot.infinity_polling()

