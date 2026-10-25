import telebot
from telebot import types

# "8646229502:AAEAsnMptnhLXjrWjiJM7XrKAoEXcblpe10"

# @choose_numbot

bot = telebot.TeleBot("8646229502:AAEAsnMptnhLXjrWjiJM7XrKAoEXcblpe10")

que_and_answ = [
    ["Сколько будет 2 + 2?", "3", "4", "5", "6"],
    ["Какого цвета трава летом?", "Красная", "Синяя", "Зелёная", "Белая"],
    ["Сколько дней в неделе?", "5", "6", "7", "8"],
    ["Какое животное говорит «мяу»?", "Собака", "Кошка", "Корова", "Лошадь"],
]

right_answers = [2, 3, 3, 2]

que_num = 0

fails = 0


@bot.message_handler(commands=["start"])
def process_command_start(message):

    global fails

    chat_id = message.chat.id
    output_text = ""

    if que_num <= 3:
        inline_keyboard = types.InlineKeyboardMarkup(row_width=2)

        for i in range(0,4,2):
            inline_keyboard.add(types.InlineKeyboardButton(que_and_answ[que_num][i+1], callback_data=f"que:{i+1}"),
                                types.InlineKeyboardButton(que_and_answ[que_num][i+2], callback_data=f"que:{i+2}"),
    )   

        for i in range(0,4):
            if que_num == i:
                output_text = "Викторина!"
                output_text += "\n"
                output_text += "\n"
                output_text += f"Вопрос: {que_and_answ[i][0]}"
                output_text += "\n"
                output_text += "\n"
                output_text += "Выберите правильный вариант ответа:"

        bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )

    else:
        output_text = "Вы прошли викторину."

        bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
    )

                        



@bot.callback_query_handler(func=lambda call: call.data.startswith("que:") == True)
def process_inline_btn_keyboard(call):

    global fails, que_num

    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    input_text = call.data
    output_text = "i"

    user_answer = int(input_text.split(":")[1])

    if user_answer == right_answers[que_num] and que_num < 3:
        output_text = "Правильный ответ!"
        output_text += "\n"
        output_text += "\n"
        output_text += "Напишите /start для того чтобы узнать следующий вопрос"
        que_num += 1
    elif user_answer != right_answers[que_num] and que_num < 3:
        output_text = f"Вы ошиблись, правильный ответ был {que_and_answ[que_num][right_answers[que_num]]}"
        output_text += "\n"
        output_text += "\n"
        output_text += "Напишите /start для того чтобы узнать следующий вопрос"
        fails += 1
        que_num += 1
    elif user_answer != right_answers[que_num] and que_num == 3:
        output_text = f"Вы ошиблись, правильный ответ был {que_and_answ[que_num][right_answers[que_num]]}"
        output_text += "\n"
        output_text += "\n"
        output_text += f"Вы ответили правильно на {4-fails}/4 вопросов."
        fails += 1
        que_num += 1
    elif user_answer == right_answers[que_num] and que_num == 3:
        output_text = "Правильный ответ!"
        output_text += "\n"
        output_text += "\n"
        output_text += f"Вы ответили правильно на {4-fails}/4 вопросов."
        que_num += 1
    

    bot.send_message(
    chat_id,
    output_text,
)

print("Бот запущен")
bot.infinity_polling()