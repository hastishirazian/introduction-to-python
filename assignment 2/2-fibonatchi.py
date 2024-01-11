n = int(input("please enter a number."))

a = 1  #first number
b = 1  #second number
i = 2  #counter

if n==0:
    print("You must choose a number greater than zero")

elif n==1:
    print(a)

elif n==2:
    print(a)
    print(b)

elif n>=3:
    print(a)
    print(b)

    while i<=n:
        a , b = b , a+b
        i=i+1
        print(b)

