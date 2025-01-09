# sum of natural number
# n = int(input("Enter  a  number"))

# def findSum(num):
#     sum = 0
#     i = 1
#     while i <= num:
#         sum = sum + i
#         i+=1
#     return sum 
# sum = findSum(n)
# print(sum)


# swap to numbers in a list
arr = []
size = int(input("enter the size of array: "))
i = 0
while i < size:
    ele = input("enter element ") 
    arr.append(ele)
    i+=1
print(arr)
position1 = int(input("enter the first position to swap: "))
position2 = int(input("enter the second position to swap: "))

if position1 >= 0 and position1 <= size and position2 >= 0 and position2 <= size :
    temp = arr[position1]
    arr[position1] = arr[position2]
    arr[position2] = temp
print(arr)