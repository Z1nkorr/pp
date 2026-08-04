ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя!#$%&()*+,-./:;<=>?@[]^_`{|}~ "

original_text = ""
enc_key = 0

enc_text = ""

original_text = input("Введите текст для шифрования: ")
enc_key = int(input("Введите ключ для шифрования от 1 до 100000: "))

enc_key = enc_key % len(ALPHABET)

for symbol in original_text:
    original_index_in_alphabet = ALPHABET.find(symbol)

    if original_index_in_alphabet == -1:
        enc_text += symbol
    else:
        enc_index_in_alphabet = (original_index_in_alphabet + enc_key) % len(ALPHABET)
    
        enc_text += ALPHABET[enc_index_in_alphabet]

print(enc_text)

decrypted_text = ""

for symbol in enc_text:
    original_index_in_alphabet = ALPHABET.find(symbol)

    if original_index_in_alphabet == -1:
        decrypted_text += symbol
    else:
        decrypted_index_in_alphabet = (original_index_in_alphabet - enc_key) % len(ALPHABET)
        decrypted_text += ALPHABET[decrypted_index_in_alphabet]

print(decrypted_text)