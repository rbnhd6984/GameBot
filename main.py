import telebot
from telebot import types
import random

api_token = '6805410332:AAGdz7SHXxBnYCiK_WjCr-cZPjrTCIdXx9I'

bot = telebot.TeleBot(api_token)
pl_points = 0
pc_points = 0

pc_symbol = ['✊', '✌️', '✋']


@bot.message_handler(commands=['start'])
def start(message):
    text = (
        'Здравствуйте, этот бот будет играть с Вами в "камень ножницы бумага", пока Вам не надоест.\n'
        'Чтобы начать играть нажмите кнопку - Играть.\n'
        'Чтобы узнать правила нажмите кнопку - Правила.'
    )
    mk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mk.add(types.KeyboardButton("Играть"), types.KeyboardButton("Правила"))
    bot.send_message(message.chat.id, text, reply_markup=mk)


@bot.message_handler(content_types=['text'])
def game(message):
    global pc_points, pl_points
    text = (
        'Это классическая игра в камень, ножницы, бумага.\n'
        '\n'
        'Для выбора символа, нажмите кнопку с его изображением.\n'
        '\n'
        'Компьютер выберит свой символ в случайном порядке.\n'
        '\n'
        'Чтобы узнать/сбросить счет, нажмите 🛑\n'
        'Для возврата в главное меню 🔙'
    )

    if message.text == "Правила":
        bot.send_message(message.chat.id, text)
    elif message.text == "Играть":
        mk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mk.add(types.KeyboardButton("✊"), types.KeyboardButton("✌️"), types.KeyboardButton("✋"),
               types.KeyboardButton('🛑'), types.KeyboardButton('🔙'))
        bot.send_message(message.chat.id, "Выберите камень, ножницы или бумага", reply_markup=mk)

    symbol = random.choice(pc_symbol)

    if message.text in pc_symbol:
        bot.send_message(message.chat.id, f"{symbol}️")
        if message.text == symbol:
            bot.send_message(message.chat.id, "Ничья -_-")
        elif (message.text == '✊' and symbol == '✌️') or (message.text == '✌️' and symbol == '✋') or (
                message.text == '✋' and symbol == '✊'):
            pl_points += 1
            bot.send_message(message.chat.id, "Вы победили :D")
        else:
            pc_points += 1
            bot.send_message(message.chat.id, "Вы проиграли X_x")

    elif message.text == '🛑':
        bot.send_message(message.chat.id, f'Счёт - 🙎‍♂️ {pl_points} : {pc_points} 🤖')
        pl_points = 0
        pc_points = 0
        bot.send_message(message.chat.id, 'Наигрались?')

    elif message.text == '🔙':
        pl_points = 0
        pc_points = 0
        mk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mk.add(types.KeyboardButton("Играть"), types.KeyboardButton("Правила"))
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=mk)


bot.polling(none_stop=True)
