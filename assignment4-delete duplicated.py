print("Enter a list of numbers.")

n = int(input("Please specify the length of the array."))
numbers = []
non_repeated = []
counter = 0

while counter!=n:
    number = input("number:")
    numbers.append(number)
    counter+=1

for number in numbers:
    if number not in non_repeated:
        non_repeated.append(number)


print("The final result by removing duplicate elements:")
print(non_repeated)