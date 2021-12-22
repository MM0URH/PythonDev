import os
from datetime import datetime
from datetime import date
now = datetime.now()
today = date.today()

nowTime = now.strftime("%H:%M:%S")
nowDate = today.strftime("%d/%m/%Y")

print("Last Updated at:", nowTime, "on",nowDate)




ans=True


while ans:
    print ("""
    1.Convert from C to F
    2.Convert from F to C
    3.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1":
        inpt = float(input('What is the Temperature in C: '))
        workout = float(((inpt*9)/5)+32)
        outpt = round(workout,1)
        print("Temp in C is ", outpt , "Degrees")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans =="2":
        inpt = float(input('What is the Temperature in F: '))
        workout = float(((inpt-32)*5)/9)
        outpt = round(workout,1)
        print("Temp in C is ", outpt , "Degrees")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="3":
        print("\n Goodbye")
        raise SystemExit
    elif ans !="":
        print("\n Not Valid Choice Try again") 