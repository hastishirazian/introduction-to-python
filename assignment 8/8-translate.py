def read_from_file():
    f = open("assignment 8/translate.txt" , "r")
    global words_bank
    global temp
    temp = f.read().split("\n")
    words_bank = []

    for i in range(0,len(temp),2):
        my_dict = {"en":temp[i] , "fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def show_menu():
    print("1.Translate English to persian")
    print("2.Translate persian to English")
    print("3.Add a new word to database")
    print("4.Exit")

def persian_to_english():
    user_input = input("Enter your persian text:")
    user_words = user_input.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                print(word["en"])
                break
        else:
            print(user_word)


def english_to_persian():
    user_input = input("Enter your english text:")
    user_words = user_input.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                print(word["fa"])
                break
        else:
            print(user_word)

def add_word():
    print("In which language do you want to add a new word?")
    print("1. English")
    print("2. persian")

    add_choice = int(input("Enter your choice:"))

    if add_choice==1:
        new_word = input("Enter the english word you want to add to the database:")

        for word in words_bank:
            if new_word==word["en"]:
                print("The entered word already exists in the database!!!")
                break

        else:
            translated_word = input("persian translation of the word:")

            my_dict = {"en":new_word , "fa":translated_word}
            words_bank.append(my_dict)
            print("The new word was successfully added to the database✅")

    elif add_choice==2:
        new_word = input("Enter the persian word you want to add to the database:")

        for word in words_bank:
            if new_word==word["fa"]:
                print("The entered word already exists in the database!!!")
                break

        else:
            translated_word = input("English translation of the word:")
            my_dict = {"en":translated_word , "fa":new_word}
            words_bank.append(my_dict)
            print("The new word was successfully added to the database✅")
############################################################ functions
read_from_file() 
print("Welcome to my translate!!!!")
    
while True:
    show_menu()
 
    choice = int(input("Enter your choice:"))

    if choice==1:
        english_to_persian()

    elif choice==2:
        persian_to_english()

    elif choice==3:
        add_word()
        read_from_file()
    elif choice==4:
        exit()

    else:
        print("The entered value is not allowed!!!!")