import random
ans=True
while ans:
    print ("""
    1.Pick for Lotto
    2.Pick for EuroMillions
    3.Exit/Quit
    """)
    ans = input("What would you like to do? ") 
    if ans=="1":
        nums = sorted(random.sample(range(1,50), 6))
        print("My Predected numbers for this weeks UK lottery are: ", nums[0],",", nums[1],",",nums[2],",",nums[3],",",nums[4],", and",nums[5])
        print("\n")
        print("Good Luck!")
        ans=True
    elif ans =="2":
        nums = sorted(random.sample(range(1,50), 5))
        print("My Predected numbers for this weekes Euromillions lottery are: ", nums[0],",", nums[1],",",nums[2],",",nums[3],", and",nums[4])
        print("\n")
        stars = sorted(random.sample(range(1,12), 2))
        print("My Predected numbers for this weeks Euromillions stars are: ",stars[0]," and ", stars[1])
        print("\n")
        print("Good Luck!")
        ans=True
    elif ans=="3":
        print("\n Goodbye")
        raise SystemExit
    elif ans !="":
        print("\n Not Valid Choice Try again") 

