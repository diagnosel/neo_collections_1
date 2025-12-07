from datetime import timedelta, datetime

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)


print(delta)


#Якщо відняти від одного datetime об'єкту інший, 
# то отримаємо timedelta об'єкт. Він відповідає за відрізок часу між двома датами.

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019

print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

#Об'єкти timedelta можна створювати, щоб отримати дату/час віддалену від початкової.
now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)

#Або від якоїсь конкретної дати.
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00



# ми хочемо визначити скільки пройшло повних днів, 
# коли Наполеон спалив Москву, а це відбулося 14 вересня 1812 року

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)


d = datetime(2025, 11, 23)
print("date to days - ", d.toordinal())

d1 = datetime.fromordinal(739578)
print(d1)


#timestamp
ts = now.timestamp()
print ("now in timestamp is ", ts)

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу



#Конвертація timestamp в об'єкт datetime
# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime


print("is now", now)
print("formatted: ", now.strftime("[%d.%m.%y %H:%M:%S]"))

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)


#strptime
text = "2023-12-14 18:30:00"
dt = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")

print(dt)        # 2023-12-14 18:30:00
print(type(dt))  # <class 'datetime.datetime'>



# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу



date_print = datetime.strptime("12 June, 2025", "%d %B, %Y")
print(date_print)