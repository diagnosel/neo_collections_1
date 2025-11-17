#1
# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")


#2
#Змінна length = len(str(num)) 
# перетворює число в рядок str(num) і обчислює 
# його довжину за допомогою функції len(). 
# Ця довжина використовується для перевірки, чи число є двозначним.
# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")


#3
# Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
# Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
# Виводить "FizzBuzz", якщо число кратне обом цим числам;
# В іншому випадку виводить саме число.
# Задаємо конкретне число
# num = int(input())

# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)


#4
# У Python рекомендується для виділення одного рівня вкладеності 
# для блоку інструкцій використовувати 4 пробіли.


# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero") #4 пробіли
#     x = int(input("X: "))

# result = y / x
# print(result)


# #5
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

"""
                    y+
                     ↑
                     │
             II      │       I
                     │
                     │
x-       ────────────┼────────────      x+
                     │
                     │
            III      │       IV
                     │
                     ↓
                    y-

"""

#ternar
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

#те саме що і 
# is_nice = True
# if is_nice:
#     state = "nice"
# else:
#     state = "not nice"


#В прикладі ми присвоїмо msg значення some_data, якщо some_data не є None
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)

#те саме що і 
# some_data = None
# if some_data:
#     msg = some_data
# else:
#     msg = "Не було повернено даних"