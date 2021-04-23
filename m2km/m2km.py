import os
ans=True
while ans:
    print ("""
    1.Calculate Miles to Kilometres.
    2.Calculate Kilometres to Miles.
    3.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1": 
      m = input ("Miles: ")
      mcalc = float(m)
      kmflt = float (mcalc * 1.60934)
      km = round (kmflt,1)
      print (m, " miles equates to ", km, "Kilometres")
    elif ans=="2":
      km = input ("How many kilometres would you like to convert?: ")
      kmcalc = float (km)
      mflt = float (kmcalc * 0.621371)
      m = round(mflt,1)
      print (km, "kilometres equates to ", m, "miles")
    elif ans=="3":
      print("\n Goodbye")
      raise SystemExit
    elif ans !="":
      print("\n Not Valid Choice Try again") 
