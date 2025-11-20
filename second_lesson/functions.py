# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # Кінець функції say_hello()

# # виклик функції
# say_hello()

# # ще один виклик функції
# say_hello()

#2
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів



#типізація пареметрів з версії 3.15 
# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів


#return
# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15

#return str
# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!


#return bool
# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(4)
# print(check_even)  # Виведе: True


#Незмінні типи в Python - int, float, str, tuple
# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал



#Змінні типи - list, dict, set
# def modify_list(lst: list) -> None:
#     lst.append(4) #відбулося присвоювання lst = my_list

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]


# Використовуйте метод copy() для створення копій змінних об'єктів, якщо не хочете змінювати оригінал
# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]

#задача: конвертувати кожен символ у рядку в його відповідний код ASCII
# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("Hello world!")
# print(result)



#ключові параметри

def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

# використовує значення за замовчуванням для message
greet("Олексій")  

# передача власного значення для message
greet("Марія", message="Добрий день")  


#
def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)

#
def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)


#Функція real_cost повинна приймати два аргументи: базову ціну товару base 
# та розмір знижки discount, який за замовчуванням будемо вважати 0. 
# Вона повинна повертати вартість товару після застосування знижки.

def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)

#Якщо знижка відсутня, то використовується лише базова ціна.
price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)
print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')


#*args

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

#
def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))

#**kwargs
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25)

#коли разом
def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)