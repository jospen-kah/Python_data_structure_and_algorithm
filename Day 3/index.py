import time
import random

guess  =  random.randint(1, 10)

counter = 1 

while counter <= 4:
    num_to_guess = input("Enter the number to guess: ")
    
    if not num_to_guess.isnumeric():
        print("Enter a numeric string")
        continue
    num_to_guess = int(num_to_guess)
    if num_to_guess < 1 or num_to_guess > 10:
        print("enter numbers between 1 and 10")
        continue
    if num_to_guess == guess:
        print("congratulations!!")
        
    else:
        print(f"Sorry you failed and you are left with {4-counter} ")
        counter += 1


