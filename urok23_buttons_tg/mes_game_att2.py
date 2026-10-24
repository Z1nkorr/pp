import telebot
from telebot import types

import random

# 8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA

# @calc_game2026bot

bot = telebot.TeleBot("8540510916:AAHxP2cmbQJ1jViDccVFXZfXjRKE5gpKbnI")

right_answer = 0
pizdec_semye = 0

@bot.message_handler(commands=["start"])
def process_command_start(message):

    global right_answer

    chat_id = message.chat.id
    output_text = ""

    a = random.randint(1,10)
    b = random.randint(1,10)
    right_answer = a + b

    answers = [right_answer]

    while len(answers)<4:
        other_answer = random.randint(2,20)
        if other_answer not in answers:
            answers.append(other_answer)

    output_text = f"Решите пример {a} + {b} = ?"

    inline_keyboard = types.InlineKeyboardMarkup()

    random.shuffle(answers)

    for answer in answers:
        inline_keyboard.add(
            types.InlineKeyboardButton(str(answer), callback_data=f"answer: {answer}")
            )


    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("answer:") == True)
def process_inline_btn_keyboard(call):

    global pizdec_semye

    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    input_text = call.data
    output_text = ""

    user_answer = int(input_text.split(":")[1])

    if user_answer == right_answer and pizdec_semye == 0:
        output_text = "Твоей семье уже пиздец"
        pizdec_semye += 1
    elif user_answer != right_answer and pizdec_semye == 0:
        output_text = "Твоей семье уже пиздец"
        pizdec_semye += 1
    elif user_answer == right_answer and pizdec_semye == 1:
        output_text = "Твоей семье в любом случае пиздец"
        pizdec_semye += 1
    elif user_answer != right_answer and pizdec_semye == 1:
        output_text = "Твоей семье в любом случае пиздец"
        pizdec_semye += 1
    elif user_answer == right_answer and 2 <= pizdec_semye <= 5 or user_answer != right_answer and 2 <= pizdec_semye <= 5:
        output_text = "Иди нахуй"
        pizdec_semye += 1
    elif user_answer == right_answer and 5 < pizdec_semye < 10 or user_answer != right_answer and 5 < pizdec_semye < 10:
        output_text = "Ты еблан?"
        pizdec_semye += 1
    elif user_answer == right_answer and 10 == pizdec_semye or user_answer != right_answer and 10 == pizdec_semye:
        output_text = "Ты написал /start 10 раз чтобы что? Один хуй ты тупой"
        pizdec_semye += 1
    else:
        output_text = "Это все тут больше ничего не увидишь. Завтра тебя насильно помоют"
    

    bot.send_message(
    chat_id,
    output_text,
    message_thread_id=call.message.message_thread_id,
    )



print("Бот запущен")
bot.infinity_polling()