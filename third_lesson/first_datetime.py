
import datetime

now = datetime.datetime.now()
print(now)

today_date=now.date()
today_time=now.time()


print("Today date - ", today_date)
print("Today time - ", today_time)
today_date_time = datetime.datetime.combine(today_date, today_time)
print("Today date and time - ", today_date_time)



# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"


# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"


# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


#Метод weekday() використовується для отримання номера дня тижня для вказаної дати. 
# Він повертає номер дня тижня, де понеділок має номер 0, а неділя - 6.

# Створення об'єкта datetime
now = datetime.datetime.now()

# Отримання номера дня тижня
# корисний для встановлення умов в залежності від дня тижня.

day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  


# порівняння дат

# Створення двох об'єктів datetime
datetime1 = datetime.datetime(2023, 3, 14, 12, 0)
datetime2 = datetime.datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2