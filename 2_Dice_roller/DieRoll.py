import random
shallWePlay = "y"

while shallWePlay != 'n':
    if shallWePlay == 'y':

        die1 = (random.randrange(1, 6))
        die2 = (random.randrange(1, 6))
        if die1 == die2:
            print(f'You rolled double {die1}')
            shallWePlay = input('Do you want to play again [y] or [n]? ')  
        else:
            print (f'You rolled a {die1} and a {die2}')
            shallWePlay = input('Do you want to play again [y] or [n]? ')  
    else:
        print('Invalid response. Please type [y] or [n].')
        shallWePlay = input('Do you want to play again [y] or [n]? ')        

print('Thanks for playing, Toodles!!')
