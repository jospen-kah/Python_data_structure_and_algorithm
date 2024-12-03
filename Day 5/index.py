# Reusing functions

def myfunct(num1):
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        return myfunct(num1-1)+ myfunct(num1-2) 
    
    
num = input("Enter the number to get the the Fibonacci")
if num.isnumeric():
 while True:
    num = int(num)
    fib = myfunct(num)
    print(f"The fibonacci of {num} is {fib}")
    continue
else:
    print("Try to enter a digit")