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
    1.Calculate Voltage (Current and Resistance known)
    2.Calculate Current (Voltage and Resistance known)
    3.Calculate Resistance (Voltage and Current known)
    4.Calculate Current (Voltage and Power known)
    5.Calculate Voltage (Current and Power known)
    6.Calculate Voltage Divider Vout (Vin, R1, and R2 known)
    7.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1": 
        ampi = input ("Amps: ")
        ohmi = input ("Ohms: ")
        ampcalc = float(ampi)
        ohmcalc = float (ohmi)
        volto = float(ampcalc * ohmcalc)
        pwr = float (ampcalc * volto)
        print ("With ", ampi, "Amps and ", ohmi, "Ohms, you will have ", volto, "Volts of potential difference")
        print ("\nWhich equates to ", pwr, "watts of power")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="2":
        volti = input ("Volts: ")
        ohmi = input ("Ohms: ")
        voltcalc = float(volti)
        ohmcalc = float (ohmi)
        ampo = float (voltcalc / ohmcalc)
        pwr = float (ampo * voltcalc)
        print ("With ", volti, "Volts and ", ohmi, "Ohms, you will have ", ampo, "Amps of current")
        print ("\nWhich equates to ", pwr, "watts of power")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="3":
        volti = input ("Volts: ")
        ampi = input ("Amps: ")
        voltcalc = float(volti)
        ampcalc = float(ampi)
        ohmo = float(voltcalc / ampcalc)
        pwr = float (ampcalc * voltcalc)
        print ("With ", volti, "Volts and ", ampi, "Amps, you will have ", ohmo, "ohms of resitance")
        print ("\nWhich equates to ", pwr, "watts of power")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="4":
        volti = input ("Volts: ")
        poweri = input ("Watts: ")
        voltcalc = float(volti)
        powercalc = float(poweri)
        ampout = float(powercalc / voltcalc)
        print ("There are ", ampout, "Amps of current")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="5":
        ampi = input ("Amps: ")
        poweri = input ("Watts: ")
        ampcalc = float(ampi)
        powercalc = float (poweri)
        voltout = float (powercalc / ampcalc)
        print ("There are ", voltout, "volts")
        print("Last Updated at:", nowTime, "on",nowDate)
        ans=True
    elif ans=="6":
        Vin = input ("Vin (in Volts): ")
        r1 = input ("R1 (in ohms): ")
        r2 = input ("R2 (in ohms): ")
        Vinf = float (Vin)
        r1f = float (r1)
        r2f = float (r2)
        r3 = float (r1f + r2f)
        Rtotal = float (r2f / r3)
        Vout = float (Vinf * Rtotal)
        print("Last Updated at:", nowTime, "on",nowDate)
        print ("Vout is", Vout, "volts")
        ans=True
    elif ans=="7":
        print("\n Goodbye")
        raise SystemExit
    elif ans !="":
        print("\n Not Valid Choice Try again") 
