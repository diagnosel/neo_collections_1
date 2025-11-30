from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

#Для зворотного перетворення рядка у форматі ISO 8601 на об'єкт datetime
iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)


#Метод isoweekday() у об'єкті datetime використовується для отримання дня 
# тижня відповідно до ISO 8601. Згідно з цим стандартом, 
# тиждень починається з понеділка, який має значення 1, 
# і закінчується неділею, яка має значення 7.


# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня


# isocalendar() - це кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня), де:
# ISO_рік - це рік у форматі ISO.
# ISO_тиждень - номер тижня в році за ISO 8601 (від 1 до 53).
# ISO_день_тижня - день тижня за ISO 8601, де 1 означає понеділок, а 7 - неділю.

now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

# Створення дати з ISO календаря: рік 2023, тиждень 50, день 3 (середа)
isoCl = datetime.fromisocalendar(2023, 50, 3)
print(type(isoCl))
iso_cl_print = isoCl.isocalendar()
print(iso_cl_print)
print(f"Дата створена з ISO календаря: {isoCl}")
print(iso_calendar)

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")