
# print(f.read())
# writing to the file
# first method by appending to an existing file
f = open("hello.txt", "w")
f.write("\nThe Fear of the lord is the beginning of wisdom")

# reading the edited file
f = open("hello.txt", "r")
print(f.read())
f.close()