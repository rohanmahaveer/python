from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot=ChatBot('CHOTTU')
bot.set_trainer(ListTrainer)

while True:
        message=input('You:')
        if message.strip!='Bye' or message.strip!='bye':
                 reply=bot.get_response(message)
                 print('Chatbot:',reply)
        if message.strip=='Bye' or message.strip=='bye':
                 print('Chatbot:it was nice talking to you.Bye') 
                 break
