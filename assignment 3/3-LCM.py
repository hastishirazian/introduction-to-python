print("Eter two numbers:")

num1 = int(input("number 1:"))
num2 = int(input("number 2:"))

if num1>num2:
    n = num2
else:
    n = num1

for i in range(1 , n+1):

    if (num1%i == 0) or (num2%i == 1):
        GCD = n

# through the formula, we get the LCD by using the GCD
LCM = (num1*num2)/GCD

print("The lowest common denominator is:" , LCM)
