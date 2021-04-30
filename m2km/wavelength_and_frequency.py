ans=True
while ans:
    print ("""
    1.Calculate Wavelength (Frequency known).
    2.Calculate Frequency (Wavelenght known).
    3.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1":
        f = input ("Enter Frequency (in MHz): ")
        fcalc = float(f)
        lamdaflt = float (300/fcalc)
        lamda_dipole = float(lamdaflt/2)
        if lamdaflt < 1:
            lamda = round (lamdaflt,3)
            print ("A frequency of",f,"MHz has a wavelength around",lamda, "metres")
            print ("Which is also around",int(lamda*100),"centimetres")
            print ("A dipole to match this frequency will have 2 elements of",round(lamda_dipole,2),"metres")
            print ("\nAll sizes are approximate")
        elif lamdaflt >= 1:
            lamda = int (lamdaflt)
            print ("A frequency of",f,"MHz has a wavelength around",lamda, "metres")
            print ("A dipole to match this frequency will have 2 elements of",int(lamda_dipole),"metres")
            print ("\nAll sizes are approximate")
            
    elif ans=="2":
        lamda = input ("Enter Wavelength (in metres): ")
        lamdacalc = float(lamda)
        fflt = float (300/lamdacalc)
        f = round (fflt,3)
        if f < 1:
            f = round (fflt,3)
            print ("A wavelength of",lamda,"metres, has a frequency around",f, "MHz")
        elif f >= 1:
            f = int (fflt)
            print ("A wavelength of",lamda,"metres, has a frequency around",f, "MHz")
    elif ans=="3":
        print("\n Goodbye")
        raise SystemExit
    elif ans !="":
        print("\n Not Valid Choice Try again") 
