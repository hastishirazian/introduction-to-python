import random

print("Lets play!🎲")

while 1==1:
    computer_choice= random.randint(1,6)
    user_choice= int(input("You:"))
    print("💻:" , computer_choice)

    if computer_choice==6:
        print("Another round as gift!🎉")
        computer_choice= random.randint(1,6)
        user_choice= int(input("You:"))
        print("💻:" , computer_choice)
        print("End game!!!!")
        break
    else:
        print("Next round!")