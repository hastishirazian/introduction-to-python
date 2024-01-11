print("If the entered number is a factorial result, print yes, otherwise, print new")
number = int(input("Enter a number:"))

fact = 1
counter = 1

if number == 0 or number == 1:
    result = ("Yes✅")

if number != 0 or number != 1:
    while (fact <= number):
        fact=(counter + 1)*fact
        counter+=1
        if fact == number:
            result = ("Yes✅")
            break

    else:
            result = ("No❌")

print(result)