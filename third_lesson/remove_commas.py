

def dad_filter(message):
    while ",," in message:
        message = message.replace(",,",",")
    return(message.strip(",")) #почистити якщо лишилась кома в кінці

mes = dad_filter("Hello,,,,, son,, when are you coming home?,,,,")
print(mes)

print("Hello,,, son,, when are you coming home?,,,,".replace(",,",","))