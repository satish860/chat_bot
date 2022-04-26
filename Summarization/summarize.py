import telebot
from transformers import pipeline
import wikipedia

bot = telebot.TeleBot("YOUR_BOT_TOKEN",parse_mode = None)
summary = pipeline("summarization")
state = 0 
context = '';

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global state
    global context
    
    if state == 0:
        bot.reply_to(message, "tell me a subject you wanted to summarize about ")
        state = 1
        return
    if state == 1:
        print("Subject to talk about "+ message.text.lower())
        results = wikipedia.search(message.text.lower())
        context = wikipedia.summary(results[0])
        outputs = summary(context, max_length=45,min_length=5,clean_up_tokenization_spaces=True)
        bot.reply_to(message,outputs[0]["summary_text"])
        state = 0
        return
    return
    
    
bot.infinity_polling()