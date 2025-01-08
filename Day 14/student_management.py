database = []
# name = input("enter the student name: ")
# level = input("Enter the level: ")
print(database)


while True   :
    print("Select Your Choice")
    print("1- Add a student and level \n 2- Update a level \n 3- Delete a student and Level \n 4- View all the students and their levels \n 5-Exit")
    choice = input("Enter your choice: ")
    if choice == "1"  or choice == "2" or choice =="3"  or choice =="4" or choice =="5":
        if choice == "1":
                    name = input("Enter the student name: ")
                    level = input("Enter your level : ")
                    database.append( {"name": name,"level": level} )
                  
                    
                    
        elif choice == "2":
                    level = input("Enter the level you wish to update: ")
                    name1 = input("Enter the name of the student to update the level : ")
                    for entry in database:
                        if entry["name"] == name1:  
                            print(f"Found: {entry}")
                            entry["level"] = level
                            print(f"the level has been updated to level ${level}")
                      
                            break
                        else:
                         print("Name not found")
                                            
                    
        elif choice == "3": 
                    name = input("Enter the name to delete: ")
                    level = input("Enter the Level to delete: ")
                    database.remove({"name": name, "level": level})
                    print(f" The student {name} with level {level} has been deleted")
                 
        elif choice == "4":
            print(database)
        elif choice == "5":
            exit = input("Are you sure you want to exit, \n Enter Yes or No: ")
            if exit == "yes":
                break 
            else: 
                continue
            p
                    
                    
                    


