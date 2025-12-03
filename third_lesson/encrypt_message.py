
def encrypt_by_key(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = "" #Створює порожній рядок для результату, Сюди буде записуватись зашифроване повідомлення.

    message = message.upper() #Переводить повідомлення у верхній регістр

    for letter in message: #Проходить по кожному символу повідомлення
        if letter in alpha: #Якщо літера є в алфавіті
            index = (alpha.find(letter) + key) % len(alpha) #Знаходить нову позицію літери з урахуванням ключа

# Розбиваємо цей вираз:

# alpha.find(letter) — знаходить індекс літери в алфавіті
# Наприклад: 'A' → 0, 'B' → 1, 'Z' → 25

# + key — зміщує індекс на задану кількість
# (це і є шифр Цезаря)

# % len(alpha) — модуль 26:
# якщо індекс вийшов за межі алфавіту, він “закручується” на початок.
# Наприклад: 25 + 3 = 28 → 28 % 26 = 2 → літера 'C'

            cipher += alpha[index] #Додає зашифровану літеру
        else:
            cipher += letter #Якщо символ НЕ літера (пробіл, ., ?, цифра тощо) - Код залишає його без змін.

    print(cipher)

encrypt_by_key("to be or not to be", 5)
encrypt_by_key("YT GJ TW STY YT GJ", -5) #обратний шифр до того шо вгорі
print(20 % 26)             