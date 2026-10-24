# @Patsanoid_tsitati_bot 

#8900152038:AAGAgquv7LhOa5E5gKgEDRbK6hbeNsGOu44

import telebot
import random

bot = telebot.TeleBot("8900152038:AAGAgquv7LhOa5E5gKgEDRbK6hbeNsGOu44")

@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):

    input_text = message.text
    chat_id = message.chat.id
    output_text = ""
    quotes = ["Не важно кто поджег, важно что волк теперь горит блять сука.",
              "Дальше меньше брат.",
              "67 67 67 67 67 67 67 67 67.",
              "Если ты толстый, значит ты много ешь.",
              "Если заблудился в лесу, иди домой.",
              "Если есть на свете рай - это Краснодарский край.",
              "Не имей имей, а 100 рублей друзей.",
              "Сегондня друг, завтра новый день.",
              "Ты не бесполезен. Тебя можно использовать как плохой пример.",
              "Чем меньше ты знаешь, тем больше ты тупой.",
              "Веди себя так будто ты моешься, но никогда этого не делай.",
              "За двумя зайцами, воробей с яйцами.",
              "Твоего деда изнасиловали три Бен Ладена.",
              "Соль не сахар.",
              "Умный в гору не пойдет, умный гору ам ам ам.",
              "Бенито Массалини",
              "Больше ли тебе стольки ли лет?",
              "Скажи мне кто твой друг и оба идите нахуй.",
              "Одна ошибка и ты ошибся.",
              "важно не то что не важно, важно то что важно."]

    if input_text == "/start":

        output_text = "Здарова брат, ты как всегда немощь! Если хочешь глянуть команды напиши /help. (67)"

    elif input_text == "/show_quotes":

        output_text = "Вот все цитатки:"
        for quote in quotes:
            output_text += "\n"
            output_text += quote

    elif input_text == "/random_quote":

        random_quote = random.choice(quotes)
        output_text = random_quote

    elif input_text == "/help":

        output_text = "Команды брат:"
        output_text += "\n"
        output_text += "/start (Запуск)"
        output_text += "\n"
        output_text += "/show_quotes (Все цитаты)"
        output_text += "\n"
        output_text += "/random_quote (Рандомная цитата)"
        output_text += "\n"
        output_text += "/help (Все команды)"

    

    bot.send_message(chat_id, output_text)



print("Бот запущен") 
bot.infinity_polling()