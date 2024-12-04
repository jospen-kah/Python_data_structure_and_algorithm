print("Choose from 1-4  the operation to carryout")
print("1-Push \n 2-Pop\n 3-View \n4- Exit")

cart = []

size = 4

while True:
    choice = input("Enter Your choice: ")
    
    if(choice == "1"):
        if(len(cart) < 4):
            item = input("Enter the Item to push: ")
            cart.append(item)
            print(f"The item {item} has been added ")
        else: 
            print("Sorry Your  Cart is full")
            
    elif(choice == "2"):
        if(len(cart) < 0):
           popped = cart.pop()
           print(f"You item {popped} has been  popped")
        else:
            print("sorry the  cart is Empty")
    elif(choice == "3"):
        print(cart)
    elif(choice == "4"):
        print("Existing the Program")
        break
    else: 
        print("Enter a value between 1 and 4: ")
            