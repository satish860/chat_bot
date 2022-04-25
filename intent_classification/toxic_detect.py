import telebot
from detoxify import Detoxify

bot = telebot.TeleBot("YOUR_BOT_TOKEN",parse_mode = None)
model = Detoxify('original')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  print(message.text)
  results = model.predict(message.text)
  if (max(zip(results.values(), results.keys()))[0] * 100) > 50:
    bot.reply_to(message,"I Consider this message as toxic")
    print()
  else:
    bot.reply_to(message,"This message doesnt look as toxic")
  
     
    
bot.infinity_polling()