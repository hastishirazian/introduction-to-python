import math

print("Welcome,Choose your operation from the menu.")

print("1.sum")
print("2.sub")
print("3.mul")
print("4.div")
print("5.sin")
print("6.cos")
print("7.tan")
print("8.cot")
print("9.log")
print("10.sqrt")
print("11.factorial")

op = int(input("Please enter the number of operation:"))


if op==1 or op==2 or op==3 or op==4:
    a = float(input("Enter the first number:"))
    b = float(input("Enter thr second number:"))

else:
   a = int(input("Enter the number:")) 

if op == 1:
    result= a+b

elif op == 2:
    result= a-b

elif op == 3:
    result= a*b

elif op == 4:
    if b == 0:
         result="Division is not allowed :("
    else:    
         result= a/b

elif op == 5:
    x=(a*math.pi)/180
    result= math.sin(x)

elif op == 6:
     x=(a*math.pi)/180
     result= math.cos(x)

elif op == 7:
     x=(a*math.pi)/180
     result= math.tan(x)

elif op == 8:
     x=(a*math.pi)/180
     result= math.cos(x)/math.sin(x)

elif op == 9:
     result= math.log(a)

elif op == 10:
     result= math.sqrt(a)

elif op == 11:
     fact=1
     for i in range (1,a+1):
        fact*=i
     result=fact
    
print(result)