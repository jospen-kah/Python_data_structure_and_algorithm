# # Multiplication table Generator
text = input("enter you number: ")

if text.isnumeric():
#Using while loop
    n = 0;
    while n <= 12:
        table = n * int(text);
        print(f" {text} x {n} = {table}")
        n = n+1;

    # Using for Loop
    # i = 0;  
    # for i in range(0, 13):  
    
    #     table = i * text
    #     print(f" {i} x {text} = {i*text}")
            
    #     i = i+1;
else: 
    print("you entered  a non numeric number ")
    

    
