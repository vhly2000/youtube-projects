#Computer has a secret number that we have to guess 
#random funtion 

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    
    while guess!= random_number:
        guess = int(input('Guess a number between 1 and {x}:'))
        
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    print(f'Yay, congrats. You have guess the number {random_number} correctly!')
        
guess(10)
        
        

