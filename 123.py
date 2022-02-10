from ast import Global
import telebot

from telebot import types

import requests

s_city = "Moscow,RU"
appid = "261e523ee42b698e0f420388a7a862d9"


token = "5184527373:AAHf8xr7QFk3nCLWLr_3JDoAk0oGIQ4haeA"
bot = telebot.TeleBot(token)
AList = []



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("список", "cколько у меня тайтлов", "чё глянуть", "/help", "/del", "/anime")
    bot.send_message(message.chat.id, 'Привет! Я твой аниме бот) Если хочешь узнать что я умею, жмякай на кнопку /help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я могу вести твой список аниме \n чтобы посмотреть свой список пиши - список \n Чтобы добавить аниме в список пиши - добавить название аниме \n а если ты криворукий, то и для тебя найдётся команда пиши - удалить название анимехи \n Также могу посоветовать аниме для этого пиши - чё глянуть \n Ещё я могу подсказать, сколько у тебя тайтлов  в списке, для этого пиши - сколько у меня тайтлов \n /del - обнулить список \n /anime - ссылка на сайт где можно посмотреть аниме')

@bot.message_handler(commands=['del'])
def start_message(message):
    AList.clear()
    bot.send_message(message.chat.id, 'Список обнулён!')
@bot.message_handler(commands=['anime'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://animego.org/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "чё глянуть":
        bot.send_message(message.chat.id, 'посмотри вот это, не пожалеешь ;) \n boku no piko')
    if "добавить" == message.text.lower().split(' ')[0]: 
    
        AList.append(message.text[9:])
        k = ' '.join(AList)
        print(k)
        bot.send_message(message.chat.id, 'Готово, твоё аниме в списке :)')
        bot.send_message(message.chat.id, k)

    if "удалить" == message.text.lower().split(' ')[0]: 
        AList.remove(message.text[8:])
        k = ' '.join(AList)
        bot.send_message(message.chat.id, 'Готово, твоё аниме больше не в списке :)')
        bot.send_message(message.chat.id, k)
    if message.text.lower() == "список":
        k = ' '.join(AList)
        bot.send_message(message.chat.id, 'Вот твой список, братик: \n')
        bot.send_message(message.chat.id, k)
    if message.text.lower() == "cколько у меня тайтлов":
        s = len(AList)
        print(s)
        bot.send_message(message.chat.id, s)
           
        
bot.infinity_polling()
