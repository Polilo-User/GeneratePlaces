import telebot
from telebot import types
import random
import globals as g
import time


token="7499700473:AAFE3QejdIrhQUah3IQgdBI6ETaJU9QDEpg"



bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Генерировать")
    markup.add(item1)
    bot.send_message(message.chat.id,"Привет ✌️ ", reply_markup=markup)

@bot.message_handler() 
def generatePlace(message) :
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Генерировать")
    markup.add(item1)
    try:
        if message.text == "Генерировать" : 
            if message.chat.id in g.UsersInTable :
                bot.send_message(message.chat.id,"Вы уже генерировали рассадку", reply_markup=markup)
            else :
                l = random.choice(g.List)	
                bot.send_message(message.chat.id,"Ваш слот номер " + str(l), reply_markup=markup)
                g.UsersInTable.append(message.chat.id)
                g.List.remove(l)
                g.i = g.i + 1
                if g.i == 10 : 
                    g.List = [1,2,3,4,5,6,7,8,9,10]
                if len(g.UsersInTable) == 10 : 
                    Timer()
    except TypeError:
        bot.send_message(message.chat.id,"Хорошая попытка!")


def Timer() :
    timing = time.time()
    while True:
        if time.time() - timing > 15.0 * 60:
            timing = time.time()
            g.UsersInTable = []
            return
        
bot.infinity_polling()
