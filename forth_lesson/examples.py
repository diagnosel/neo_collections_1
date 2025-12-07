import time

symbols = "|/-\\"
for symbol in symbols * 3:
    print(f"\r{symbol} Loading...", end="")
    time.sleep(0.1)
    
for i in range(101):
    print(f"\rProgress: {i}%", end="")
    time.sleep(0.02)