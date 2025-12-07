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
print('TestHook'.removeprefix('Hook')) # TestHook

