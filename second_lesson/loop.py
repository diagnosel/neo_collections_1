str = "******** \n"  
#1
# fruit = 'apple'
# for char in fruit:
#     print(char)

#2
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

#3
# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

#4
#Код з цього прикладу виведе в консоль 
# квадрати чисел списку odd_numbers

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

#5
# Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

##WHILE

#Цикл while у Python — це один із способів 
# організації циклічного виконання коду. 
# Він продовжує виконувати блок інструкцій, 
# поки задана умова залишається істинною. 
# Цикл while часто використовується, коли 
# кількість ітерацій заздалегідь невідома або 
# коли ітерації залежать від змінних, 
# які можуть бути модифіковані в процесі 
# виконання циклу

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1


#Наприклад echo скрипт, який виводить в консоль 
# те, що ви введете, доки ви не введете рядок 
# тексту exit:



# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

#3
# інструкція print(a) не виконувалась, 
# коли a ділилося на 2 без залишку, 
# оскільки ітерація завершувалася за допомогою continue.
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)


#4
# Оператори continue та break працюють тільки всередині одного циклу.
# В ситуації вкладених циклів немає способу вийти з усіх циклів одразу.
# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
# str = "******** \n"     
# for i in range(5):
#     print(i)           #0,1,2,3,4

# print(str)

# for i in range(2, 10):
#     print(i)  # 2,3,4,5,6,7,8,9

# print(str)

# for i in range(0, 10, 2):
#     print(i)   #0,2,4,6,8


# print(str)


#enumerate

# some_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(some_list):
#     print(index, value)


#zip
# list1 = ["зелене", "стигла", "червоний"]
# list2 = ["яблуко", "вишня", "томат"]
# for adj, fruit in zip(list1, list2):
#     print(adj, fruit)

print(str)

#Коли колекції, передані в zip, мають різну довжину, 
# zip обробляє елементи до тих пір, поки не закінчаться елементи в найкоротшій колекції.

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)


numbers = {
    1: "one",
    2: "two",
    3: "three"
}

#перебрати ключі 1 спосіб
# for key in numbers:
#     print(key)

#перебрати ключі 
for key in numbers.keys():
    print(key)

print(str)

#перебрати значення 
for val in numbers.values():
    print(val)

print(str)

#перебрати ключ-значення 
for key,val in numbers.items():
    print(key,val)