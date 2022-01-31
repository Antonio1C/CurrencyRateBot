#!/usr/bin/env python

from os import path
import  sys
from inspect import getabsfile
from telebot import types, telebot

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        file_path = path.abspath(sys.executable)
    else:
        file_path = getabsfile(get_script_dir)

    if follow_symlinks:
        file_path = path.realpath(file_path)
    return path.dirname(file_path)

token_file_path = get_script_dir()
with open(token_file_path + '/token.txt', 'r') as token_file:
    token = token_file.readline()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, message.text, reply_markup=markup)

bot.infinity_polling()
