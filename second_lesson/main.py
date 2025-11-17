#1
# num = 15  # приклад значення для num

# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

#2
# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

#3
# a = input('Введіть число: ')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

#4
# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

#5
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

#6
# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

"""У цьому прикладі, b є тим самим об'єктом, що й a, 
тому що вони вказують на один і той же список. 
Натомість c створює новий список, який містить ті самі значення, 
але фізично є окремим об'єктом."""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False

"""Однак основне його застосування - це перевірка, чи змінна є None.

if my_var is None:
    # Робимо щось, якщо 'my_var' є 'None'

Таке використання is є оптимальним, оскільки існує лише один об'єкт None у Python.
"""

