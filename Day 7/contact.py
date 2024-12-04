

book = []

while True:
    contact = input("Enter your contact: ")
    name =  input("Enter you name: ")
    if contact.isnumeric() and not name.isnumeric():
       contact = int(contact)
        
    else:
        print("Please enter the correct contact or name")
        continue
         
    book.append({"name":name, "contact":contact})
    print(book)