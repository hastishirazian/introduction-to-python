print("Enter a list of numbers.")

n = int(input("Length of the array:"))
numbers = []
counter = 0

while counter!=n:
    number = input("number:")
    numbers.append(number)
    counter+=1

numbers.reverse()

print(numbers)