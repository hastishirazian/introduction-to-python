import random

words_bank = ["apple" , "grapes" , "mango" , "orange" , "watermelone" , "banana", "cherry" , "kiwi"]

word = random.choice(words_bank)

user_mistakes = 0
correct_chars = []
wrong_chars = []
letters = len(word)

while user_mistakes < 6:
    for i in range(len(word)):

        if word[i] in correct_chars:
            print(word[i] , end=" ")
            letters -= 1
        else:
            print("_ " , end="")

    if user_mistakes<6 and letters==0:
            print("You won!!!🎉")
            break

    user_char = input("Enter your guess:")

    if len(user_char)==1:

        if user_char in word:
            print("✅")
            correct_chars.append(user_char)
        else:
            print("❌")
            wrong_chars.append(user_char)
            user_mistakes+=1
    else:
            print("You're allowed to enter only one letter!!")
        

    if user_mistakes==6:
            print("Game oevr!!!❌")
            break