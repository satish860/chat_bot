import telebot
from transformers import pipeline
import wikipedia

bot = telebot.TeleBot("YOUR_BOT_TOKEN",parse_mode = None)
question_answering = pipeline("question-answering")
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
        bot.reply_to(message, "tell me a subject you wanted to talk about ")
        state = 1
        return
    if state == 1:
        print("Subject to talk about "+ message.text.lower())
        results = wikipedia.search(message.text.lower())
        context = wikipedia.summary(results[0])
        bot.reply_to(message,"ask me a question about this topic")
        state = 2
        return
    answer = question_answering(question = message.text,context = context)['answer']
    bot.reply_to(message,answer)
    state = 0
    return
    
    
bot.infinity_polling()