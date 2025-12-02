import time

current_time = time.time()
print(f"Поточний час: {current_time}")
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")


print("Початок паузи")
time.sleep(5)
print("Кінець паузи")