import math 

print(0.1 + 0.2 == 0.3)  # Це повертає False

print(0.1 + 0.2)

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

r = math.isclose(0.1, 0.10000000009)
print(r)  # Це поверне True