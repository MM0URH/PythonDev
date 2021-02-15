import os
ans=True
while ans:
    print ("""
    1.Calculate Voltage (Current and Resistance known)
    2.Calculate Current (Voltage and Resistance known)
    3.Calculate Resistance (Voltage and Current known)
    4.Calculate Current (Voltage and Power known)
    5.Calculate Voltage (Current and Power known)
    6.Exit/Quit
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
      os.system('Pause')
      os.system('CLS')
    elif ans=="2":
      volti = input ("Volts: ")
      ohmi = input ("Ohms: ")
      voltcalc = float(volti)
      ohmcalc = float (ohmi)
      ampo = float (voltcalc / ohmcalc)
      pwr = float (ampo * voltcalc)
      print ("With ", volti, "Volts and ", ohmi, "Ohms, you will have ", ampo, "Amps of current")
      print ("\nWhich equates to ", pwr, "watts of power")
      os.system('Pause')
      os.system('CLS')
    elif ans=="3":
      volti = input ("Volts: ")
      ampi = input ("Amps: ")
      voltcalc = float(volti)
      ampcalc = float(ampi)
      ohmo = float(voltcalc / ampcalc)
      pwr = float (ampcalc * voltcalc)
      print ("With ", volti, "Volts and ", ampi, "Amps, you will have ", ohmo, "ohms of resitance")
      print ("\nWhich equates to ", pwr, "watts of power")
      os.system('Pause')
      os.system('CLS')
    elif ans=="4":
      volti = input ("Volts: ")
      poweri = input ("Watts: ")
      voltcalc = float(volti)
      powercalc = float(poweri)
      ampout = float(powercalc / voltcalc)
      print ("There are ", ampout, "Amps of current")
      os.system('Pause')
      os.system('CLS')
    elif ans=="5":
      ampi = input ("Amps: ")
      poweri = input ("Watts: ")
      ampcalc = float(ampi)
      powercalc = float (poweri)
      voltout = float (powercalc / ampcalc)
      print ("There are ", voltout, "volts")
      os.system('Pause')
      os.system('CLS')
    elif ans=="6":
      print("\n Goodbye")
      raise SystemExit
    elif ans !="":
      print("\n Not Valid Choice Try again") 
