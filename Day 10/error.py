def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except ValueError:
        print("you entered a wrong value")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
        
def add(x,y):
    try: 
        result = x + y
    except ValueError:
        print("you entered a wrong value")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
  
def sub(x,y):
    try: 
        result = x - y
    except ValueError:
        print("you entered a wrong value")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")    

def mul(x,y):
    try: 
        result = x * y
    except ValueError:
        print("you entered a wrong value")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")  

num1 = input("Enter first number: ")
num2= input("Input Second number: ")

while True:
    if num1.isnumeric() and num2.isnum():
        num1 = int(num1)
        num2 = int(num2)
    else: 
        print("Please enter an Interger")
        continue
    print("Which operation do you want to carryout: \n 1-Addition \n 2-Subtraction \n 3-Multiplication \n 4-Divisiov \n 5-Exit")
    choice = input("Enter your choice from 1 to 4")
    if choice == "1":
        add(num1, num2)
    if choice == "2":
        sub(num1, num2)
        
    if choice == "3":
        mul(num1, num2)
    if choice == "4":
        div(num1, num2)
        
    if choice == "5":
         exit = input("Are you sure you want to exit the program 'yes' or 'no' : ")
         if exit == "yes":
            break
         else:
            continue
    