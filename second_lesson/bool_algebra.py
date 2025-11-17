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
num = int(input("Введіть число: "))

length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парне двозначне число")
else:
    print("Ні")


#3
# Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
# Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
# Виводить "FizzBuzz", якщо число кратне обом цим числам;
# В іншому випадку виводить саме число.
# Задаємо конкретне число
num = int(input())

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)