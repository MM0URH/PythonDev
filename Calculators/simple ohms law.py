
volti = input ("Volts: ")
ampi = input ("Amps: ")
###ohmi = input int("Ohms")

voltcalc = int(volti)
ampcalc = int(ampi)

ohmo = int(voltcalc * ampcalc)

print ("With ", volti, "Volts and ", ampi, "Amps, you will have ", ohmo, "ohms of resitance")
