import telebot
from telebot import types

import random

# "8822757239:AAEXC018vBPyckxSTjZYBsiVmdaRNXuMp70"

# @choose_numbot

bot = telebot.TeleBot("8822757239:AAEXC018vBPyckxSTjZYBsiVmdaRNXuMp70")

@bot.message_handler(commands=["start"])
def process_command_start(message):

    chat_id = message.chat.id
    output_text = ""

    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)

    for i in range(1,7,2):
        inline_keyboard.add(types.InlineKeyboardButton(str(i), callback_data=f"num:{i}"),
                            types.InlineKeyboardButton(str(i+1), callback_data=f"num:{i+1}"),
)   

    output_text = "Выберите число:"

    bot.send_message(
    chat_id,
    output_text,
    message_thread_id=message.message_thread_id,
    reply_markup=inline_keyboard,
)

@bot.callback_query_handler(func=lambda call: call.data.startswith("num:") == True)
def process_inline_btn_keyboard(call):

    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    input_text = call.data
    output_text = ""

    user_answer = int(input_text.split(":")[1])

    output_text = f"Вы выбрали число {user_answer}."

    bot.send_message(
    chat_id,
    output_text,
)

print("Бот запущен")
bot.infinity_polling()