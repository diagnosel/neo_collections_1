from datetime import datetime, timezone, timedelta

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC


# Щоб перетворити час з UTC в іншу часову зону, 
# вам знадобиться визначити об'єкт timezone з відповідним зсувом. 
# Наприклад, для перетворення UTC часу в час, 
# що відповідає Східному часовому поясу США (UTC-5 годин), можна зробити наступне:

utc_time = datetime.now(timezone.utc)
# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  



#Щоб перетворити локальний час у час UTC, спочатку потрібно призначити
#локальному часу відповідну часову зону, а потім використати метод astimezone() для конвертації його в UTC:

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC