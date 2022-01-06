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
    1.Convert from Miles
    2.Convert from KM
    3.Convert from Nautical Miles
    0.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1":
        inpt = float(input('What is the distance in Miles: '))
        workoutkm = float(inpt*1.60934)
        outptkm = round(workoutkm,2)
        workoutnm = float(inpt*0.8689766590092)
        outptnm = round(workoutnm,2)
        print(inpt, "miles is", outptkm , "kilometres")
        print(inpt, "miles is", outptnm , "nautical miles")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans =="2":
        inpt = float(input('What is the distance in Km: '))
        workoutsm = float(inpt*0.62137141841645)
        outptsm = round(workoutsm,2)
        workoutnm = float(inpt*0.539957)
        outptnm = round(workoutnm,2)
        print(inpt, "kilometres is", outptsm , "statute miles")
        print(inpt, "kilometres is", outptnm , "nautical miles")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans =="3":
        inpt = float(input('What is the distance in nm: '))
        workoutkm = float(inpt*1.85200088896)
        outptkm = round(workoutkm,2)
        workoutsm = float(inpt*1.15078)
        outptsm = round(workoutsm,2)
        print(inpt, "nautical miles is", outptkm , "kilometres")
        print(inpt, "nautical miles is", outptsm , "statute miles")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="0":
        print("\n Goodbye")
        raise SystemExit
    elif ans !="":
        print("\n Not Valid Choice Try again") 