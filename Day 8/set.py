set1 = set()

set2 = set()

while True:

    
    print("What operation do you want to carry out : ")
    print("1-Insert elements into Set A")
    print("2-Insert Elements into Set B")
    print("3-Unite SetA and SetB")
    print("4-Intersect set A and SetB")
    print("5-Exit")
    choice = input("\n\nPlease Enter your choice!!!: ")
    
    if choice == "1":
        print("You want to add to set 1")
        element1 = input("Enter an element in set 1: ")
        set1.add(element1)
        print(set1)
    if choice == "2":
        print("You want to add to set 2")
        element2 = input("Enter an element in set 2: ")
        set2.add(element2)
        print(set2)
    if choice == "3":
        print("\n\n You want to carryout the union")
        union =  set1 | set2
        print(f"The Inetersection between {set1} & {set2} gives {union}")
    if choice == "4":
        print("\n\n You want to carryout the union")
        intersect =  set1 & set2
        print(f"\n\nThe intersection between {set1} & {set2} gives {intersect}")
        
    if choice == "5": 
        exit = input("Are you sure you want to exit the program 'yes' or 'no' : ")
        
        
        if exit == "yes":
            break
        else:
            continue