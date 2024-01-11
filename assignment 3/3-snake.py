print("Draw a snake with # and *!!!!")
n = int(input("Enter the length of your snake:"))

for i in range (n):
    if i%2 == 0:
        print("#" , end=" ")
    else:
        print("*" , end=" ")