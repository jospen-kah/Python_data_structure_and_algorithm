

print("Choose from 1-4 the operation you wish to carry out:")
print("1 - Push\n2 - Pop\n3 - View the Cart\n4 - Exit")

# Initialize an empty cart
cart = []

# Maximum size of the cart
size = 4

while True:
    # Get user choice
    choice = input("Enter your choice from 1 to 4: ")
    
    if choice == "1":
        # Push an item into the cart
        if len(cart) < size:
            item = input("Enter the item to add: ")
            cart.append(item)
            print(f"'{item}' has been added to the cart.")
        else:
            print("Cart is full! Cannot add more items.")
    
    elif choice == "2":
        # Pop an item from the cart
        if cart:
            removed_item = cart.pop()
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("The cart is empty! Nothing to remove.")
    
    elif choice == "3":
        # View the cart
        if cart:
            print("Items in the cart:", ", ".join(cart))
        else:
            print("The cart is empty.")
    
    elif choice == "4":
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
