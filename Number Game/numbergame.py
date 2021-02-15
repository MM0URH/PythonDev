import random

numberinput = input ("Enter a number ")
if numberinput != "":
    numout = random.randint(0, 9)

numin = int(numberinput)
if numin < 0:
    print ("invalid number")
elif numin > 10:
    print ("invalid number")
elif numin == numout:
    print("Correct")
else:
    print(f'The correct answer was {numout}, try again!')

