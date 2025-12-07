#Цей метод повертає індекс початку першого збігу в рядку s, 
# починаючи з позиції start до позиції end. Якщо start та end не вказані, 
# то пошук відбувається з початку і до кінця рядку. 
# Метод повертає -1, якщо послідовність не знайдена.

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1


#Вираз s.find("o") поверне 1, а вираз s.rfind('o') поверне 6 бо шукає справа рядка 
# і матимемо наступне виведення:
s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))

#те саме
s = 'Some words'

print(s.index("o"))
print(s.rindex('o'))


text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

clean = '   spacious   '.strip()
print(clean) # spacious

#Якщо нам треба обмеження кількості замін, то:
text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

#text = "one fish, two fish, red fish, blue fish"
text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)

#Для видалення фіксованої послідовності на початку рядка є метод removeprefix:
print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook ('Hook' це суфікс рядка і видалений не буде)

#Є парний метод для видалення послідовності в кінці рядка, removesuffix:
print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

#Ви маєте URL пошукового запиту, 
# і ваше завдання - видобути та обробити параметри цього запиту. 
# Наприклад пошуковий запит "Cat and dog"

#<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?') #використовуємо символ _ для ігнорування частини URL до ?, Та отримуємо змінну query яка рядок, що містить необхідні нам параметри запиту.
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key:value.replace('+', ' ')})
print(obj_query)


#isdigit() використовується для перевірки, 
# чи складається рядок повністю з цифр. 
# Цей метод повертає True, якщо всі символи в рядку є цифрами 
# та рядок складається принаймні з одного символу, інакше повертає False.
number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False


user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
