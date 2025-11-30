from datetime import timedelta, datetime

now = datetime.now()
future_date = now + timedelta(days=37)  # Додаємо X днів до поточної дати
print(future_date)