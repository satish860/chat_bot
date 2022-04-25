import telebot
from transformers import pipeline

bot = telebot.TeleBot("5266165301:AAHYKpM2XEIaqiA2TRWDJ0i7-6AGIzKNN4c",parse_mode = None)
intent_classfication = pipeline("zero-shot-classification")
labels = ["choose drinks", "order a pizza", "inform my address"]

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  print(message.text)
  result = intent_classfication(message.text,labels)
  bot.reply_to(message, result['labels'][0])
    
    
    
bot.infinity_polling()