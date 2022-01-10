redsleftinput = input("How many reds are on the table? :") ##Ask user to input the number of red balls left
redsleft = int(redsleftinput) ##Convert user input to integer
if redsleft < 0: ##validate lower end of input
    print("\n Not Valid Choice Try again") ##display error
elif redsleft > 15: ##validate upper end of input
    print("\n Not Valid Choice Try again")##display error
else:
    total = (redsleft * 8)+27 ## add the number of reds (1 point each), all taken with blacks (7 points each), and the value of the coloured balls in sequence (27 in total)
    print ("There is a total of",total,"points left on the table, excluding fouls") ##show total score possible.