import telebot
import wikipedia
bot = telebot.TeleBot('6425604599:AAH1BpzGrisvHSeBH-1zy5DLY0CgeedpJWg')
wikipedia.set_lang('uz')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Assalamu alaikum')

@bot.message_handler()
def main(message):
    try:
        article = wikipedia.summary(message)
        bot.send_message(message.chat.id, article)
    except:
        bot.send_message(message.chat.id,'Maqola mavjud emas')

bot.polling(none_stop=True)