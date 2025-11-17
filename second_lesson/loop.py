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

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1