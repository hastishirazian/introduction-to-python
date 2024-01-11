import random

print("Fill an array with non-repeating random numbers.")
n = int(input("Please specify the length of the array."))

array = []
counter = 0

while counter!=n:
    print = ("number:")
    number = random.randint(0,n)
    if number not in array:
        array.append(number)
        counter+=1


print(array)