#Guess Game
import random
import math

guess = math.floor((random.random()*10)+1)

a = input("Enter the number to guess between 1 to 10: ")
num_to_guess = a.isdigit()
num_to_guess = int(num_to_guess)
if(num_to_guess == True):
    if(num_to_guess == guess):
        print("Congratulations You made the right guess!!!")
    elif(num_to_guess != guess):
        print("Sorry you didn't make the write guess try again")
    else:
        print("Please enter a number between 1 to 10")
        
else: 
    print("/n/n/nEnter a whole number")





