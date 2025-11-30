#my_list = [1, 2, 3, 4, 5]
#print(len(my_list))

#nums = [3, 1, 4, 1, 5, 9, 2]
#nums.sort()
#print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]


#nums.sort(reverse=True)
#print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#words = ["banana", "apple", "cherry"]
#words.sort(key=len)
#print(words)  # Виведе ['apple', 'banana', 'cherry']

#nums = [3, 1, 4, 1, 5, 9, 2]
#sorted_nums = sorted(nums)
#print(nums)
#print(sorted_nums)

#sorted_nums_desc = sorted(nums, reverse=True)
#print(sorted_nums_desc)

#words = ["banana", "apple", "cherry"]
#sorted_words = sorted(words, key=len)
#print(words)
#print(sorted_words)
#words.reverse()
#print(words)


# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# my_dict["age"]=28
# my_dict["email"] = "lala@gmail.com"
# print(my_dict) 

# del my_dict["age"]
# print(my_dict) 
# print("name" in my_dict)
# print("age" in my_dict)

# my_dict = {"name": "Alice", "age": 25}
# age = my_dict.pop("age")
# print(age)
# print(my_dict)

# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)  # {1, 2, 3, 4}

# #remove(elem) — видаляє елемент із множини, викликає виняток, якщо такого елемента немає
# numbers.remove(3)
# print(numbers) 

# #discard(elem) — видаляє елемент із множини і не викликає виняток, якщо його немає
# numbers = {1, 2, 3}
# numbers.discard(2)
# print(numbers)  # {1, 3}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a & b)  # {3}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))  # {1, 2}
# print(a - b)  # {1, 2}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))  # {1, 2, 4, 5}
# print(a ^ b)  # {1, 2, 4, 5}


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))  # {1, 2, 3, 4, 5}
# print(a | b)  # {1, 2, 3, 4, 5}

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця

# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# s = "Hello world!"
# print(s[0])# H
# print(s[-1])# !

# print(s.upper()) 

# s = "Some Text"
# print(s.lower())  # Виведе 'some text'

# s = "Bill Jons"
# print(s.startswith("Bi"))  # Виведе True

# s = "hello.jpg"
# print(s.endswith("jpg"))  # Виведе True


# s = "hello world".capitalize()  # Результат: "Hello world"

# s = "hello world".title()  # Результат: "Hello World"

# "123".isdigit()  # True
# "hello".isalpha()  # True
# " ".isspace()  # True

# Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[0:10:2]
# #odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9]
# print(odd_numbers)

# even_numbers = numbers[1:10:2]
# #even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]
# print(even_numbers)

# three_numbers = numbers[2::3]
# print(three_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reverse_numbers = numbers[::-1]
# print(reverse_numbers) #10, 9, 8, 7, 6, 5, 4, 3, 2, 1

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers2[:]
print(copy_numbers)
