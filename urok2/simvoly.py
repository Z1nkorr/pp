symbol = input("введите любой символ с клавиатуры: ")

if len(symbol) == 0 or len(symbol) > 1:
    print("Слишком много символов. Программа будет закрыта.")
    exit()

if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("это английская буква")
    if symbol >= "a" and symbol <= "z":
        print("маленькая")
    else:
        print("большая")

elif symbol >= "0" and symbol <= "9":
    print("это цифра")
    if ord(symbol) % 2 == 0:
        print("чётная")
    else:
        print("HEчётная")
else:
    print("это неизвестный символ")