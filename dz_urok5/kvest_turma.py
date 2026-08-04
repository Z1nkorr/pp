import time
import random
print("Неделю назад ты убил троих, а сегодня ты просыпаешься в холодной камере. Тебе предстоит делать выбор который повлияет на твою судьбу.")
time.sleep(7)

username = input("Но для начала как тебя зовут? ")

inv = []
number_1 = 2
number_2 = 2
number_3 = 3
vilki = 0
nozh = 0
oskolok = 0
armature = 0
guard_alert = 0
byl_vo_dvore = 0
byl_v_dushevoy = 0
chto_kriknet_ohrannik = ["Эй, ты что там делаешь?!", "Какого хрена ты там творишь?!", "ЛЭЭЭ КОТАКБАС"]
phrase = random.choice(chto_kriknet_ohrannik)

print (f"День начинается как обычно, ты слышишь шаги за дверью камеры, а затем голос: «Эй, {username}! Давай вставай!»")
time.sleep(7)

choice_1 = input("1.подойти к дверке; 2.послать охранника; 3.ничего ни делать; твой выбор: ")

if choice_1 != "3" and choice_1 != "2" and choice_1 != "1":
    print("Охранник изнасиловал тебя дубинкой насмерть НАХУЙ")
    exit()
elif choice_1 == "1":
    print("Ты подошел, тебя вывели из камеры и повели в столовую.")
    time.sleep(4)
elif choice_1 == "2":
    print("Охранник зашел к тебе в камеру и побил тебя, затем тебя повели в столовую")
    time.sleep(4)
    guard_alert += 1
elif choice_1 == "3":
    print("Охранник зашел к тебе в камеру, схватил тебя и повел в столовую")
    time.sleep(4)

print("Сегодня в столовой ты и ешь, и работаешь")
time.sleep(4)

print("Так-как ты будешь мыть за всеми посуду у тебя появилась идея")
time.sleep(4)

povtorim = True
povezlo = False

while povtorim == True:

    choice_2 = int(input("1.взять с собой вилку; 2.взять с собой нож(нож большой, могут заметить); 3.взять осколок разбитой тарелки из мусорки под раковиной; твой выбор: "))

    if choice_2 > 3 or choice_2 < 1:
        print("Охранник увидел что ты долбаеб и застрелил тебя НАХУЙ")
        povtorim = False
        exit()

    elif choice_2 == 1:
        print("Ты аккуратно берешь вилку и суешь ее себе в карман, надеясь что этого никто не заметит")
        vilki += 1
        inv.append("1.вилка")
        povtorim = False

    elif choice_2 == 2:

        while povezlo == False:

            chance_nozh = random.randint(1,2)

            if chance_nozh == 1:
                print("Ты аккуратно берешь нож и прячешь его в штанину. Тебе повезло, никто не заметил.")
                nozh += 1
                inv.append("1.нож")
                time.sleep(3)
                povezlo = True
                povtorim = False

            elif chance_nozh == 2 and guard_alert < 3:

                print(f"Охранник заметил твои махинации и крикнул: «{phrase}»\n")
                time.sleep(2)
                guard_alert += 1

                cor_inp = False

                while cor_inp == False:
                    try:
                        answer = int(input("1.попробовать еще; 2.не пробовать; твой ответ: "))
                        if answer == 1:
                            povezlo = False
                        elif answer == 2:
                            povezlo = True
                            povtorim = True
                        else:
                            print("такого ответа не дано.")
                            time.sleep(2)
                            cor_inp = False
                    except:
                        print("такого ответа не дано.")
                        time.sleep(2)
                        cor_inp = False
                    
            elif chance_nozh == 2 and guard_alert == 2:
                print("на третий раз охранник порвал тебе жопу(не повезло)")
                exit()
                
    elif choice_2 == 3:
        print("Ты наклоняешься к мусорке под раковиной и достаешь оттуда осколок разбитой тарелки.")
        oskolok += 1
        inv.append("1.осколок")
        time.sleep(4)
        povtorim = False
        povezlo = True

print("Наконец отработав поставленное время тебя ведут обратно в камеру.")
time.sleep(3)
print("Сейчас у тебя свободное время, так что можно даже сходить на тюремный дворик проветристься.")
time.sleep(4)

povtorim_2 = True

while povtorim_2 == True:

    print("что хочешь сделать?")
    time.sleep(1)
    answer_2 = int(input("1.просмотреть инвентарь; 2.пойти на тюремный дворик; 3.пойти в душевую; твой ответ: "))

    if answer_2 == 1:
        
        povtorim_inv = True

        while povtorim_inv == True:

            print(f"твой инвентарь:\n")
            time.sleep(1)
            print(inv)
            print("можешь попробовать что-то создать")
            time.sleep(1)
            first_element = input("нижний слот для создания: ")
            second_element = input("средний слот для создания: ")
            third_element = input("верхний слот для создания: ")

            povtorim_inv = False

    elif answer_2 == 2:

        if byl_vo_dvore == 0:

            if byl_v_dushevoy == 1:
                continue
            elif byl_v_dushevoy == 0:
                number_1 = 4

            byl_vo_dvore += 1

            print("Ты идешь во внутренний двор и видишь как какого-то слабака избивает двое")
            time.sleep(4)

            cor_inp_2 = False

            while cor_inp_2 == False:
                try:
                    answer_biut = int(input("1.помочь; 2.не помочь; твой ответ: "))

                    if answer_biut == 1:

                        print("Вас двоих сильно побили, но ты смог дать отпор и в благодарность он дал тебе зажигалку и отвертку")
                        armature += 1
                        inv.append(f"{number_2}.зажигалка")
                        inv.append(f"{number_3}.отвертка")
                        cor_inp_2 = True

                    elif answer_biut == 2:

                        print("ты немного посмотрел, затем слабака увели куда-то за угол.")
                        time.sleep(3)
                        print("Проходя мимо места где проходило избиение ты заметил арматуру")
                        armature += 1
                        inv.append(f"{number_2}.арматура")
                        cor_inp_2 = True

                    else:
                        print("некорректный ввод.")
                        cor_inp_2 = False
                except:
                    print("некорректный ввод.")
                    cor_inp_2 = False

        print(f"Ты пришел во двор\n")
        time.sleep(1)
        
        sasal_povtor = True

        while sasal_povtor == True:

            print("выбирай:")
            time.sleep(0.5)

            choice_3=int(input("1.поиграть в футбол; 2.по отжиматься; 3.обратно в камеру; твой выбор: "))


            if choice_3 == 1:

                povtorim_inv = False
                povtorim_2 = False

                print(f"футбол: 5 попыток забить гол!\n")
                print(f"Угол: 1‑левый, 2‑центр, 3‑правый | Сила: 1‑слабая, 2‑средняя, 3‑сильная\n")

                score = 0
                angles = ["левый", "центр", "правый"]

                for attempt in range(5):
                    print(f"Попытка {attempt + 1}:")
                    
                    try:
                        angle = int(input("Угол (1‑3): ")) - 1
                        power = int(input("Сила (1‑3): "))
                        if not (0 <= angle <= 2 and 1 <= power <= 3):
                            raise ValueError
                    except ValueError:
                        print(f"Ошибка! Пропускаем попытку.\n")
                        continue
                    
                    goalkeeper = random.randint(0, 2)
                    print(f"Вратарь прыгает в {angles[goalkeeper]} угол.")
                    
                    if angle == goalkeeper:
                        result = "Сэйв! Вратарь поймал мяч." if power < 3 else "ГОЛ! Мощный удар пробил вратаря!"
                    else:
                        result = "ГОЛ! Вратарь не успел!" if power > 1 else "Удар мимо ворот."

                    print(result)
                    if "ГОЛ" in result:
                        score += 1
                    print(f"Счёт: {score}\n")

                print(f"\nМатч окончен! Итоговый счёт: {score}/5")
                if score >= 3:
                    print("Победа! Вы выиграли матч!")
                else:
                    print("В следующий раз повезёт больше!")

            elif choice_3 == 2:
                povtorim_inv = False
                povtorim_2 = False

                print("«Отжимания»: нужно достичь цели")
                target = random.randint(30, 50)
                total = 0

                print(f"Ваша цель: {target} отжиманий\n")

                while total < target:
                    try:
                        current = int(input("Сколько отжиманий сделаешь? "))
                        if current < 0:
                            print("Количество не может быть отрицательным")
                            continue
                        total += current
                        remaining = max(0, target - total)
                        if remaining == 0:
                            print(f"Молодец, достиг цели: {target} отжиманий")
                        else:
                            print(f"Всего сделано: {total}. Осталось: {remaining}")
                    except ValueError:
                        print("введи число.")

                if total > target:
                    extra = total - target
                    print(f"Ты сделал больше на {extra} отжиманий. Хороший результат!")
                    povtorim_2 = False

            elif choice_3 == 3:
                sasal_povtor = False

        povtorim_2 = True