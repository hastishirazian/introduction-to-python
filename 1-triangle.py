print("Please enter the size of each side.")

a = int(input("side 1:"))
b = int(input("side 2:"))
c = int(input("side 3:"))

if a+b>c and a+c>b and b+c>a :
    print("It can be drawn")

else:
    print("It cannot be drawn")



