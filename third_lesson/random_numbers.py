import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

num = random.random()
print(num)



#Припустимо, вам потрібно симулювати випадкове відсоткове заповнення. 
# Можна використовувати random.random() для цього:
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")


print(random.randrange(10)) 
target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")


cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")


fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))


ch = random.choices([1, 2, 3], k=5)
print("random: ", ch)


colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color) 


#повертає список довжиною k з унікальними елементами, вибраними випадково з population.
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")


price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")