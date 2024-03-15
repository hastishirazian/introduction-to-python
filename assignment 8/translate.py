def read_from_file():
    f = open("assignment 8/translate.txt" , "r")

    temp = f.read().split("\n")
    global words_bank
    words_bank = []

    for i in range(0,len(temp),2):
        my_dict = {"en":temp[i] , "fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def show_menu():
    print("Welcome to my translate!!!!")
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
    new_word=input("Enter the new word you want to add to the translator database:")

    for word in words_bank:
        if new_word==word["fa"] or new_word==word["en"]:
            print("The entered word exists in the database!!!")
            break

    else:
        

############################################################
read_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice:"))

    if choice==1:
        english_to_persian()

    elif choice==2:
        persian_to_english()

    elif choice==3:
        add_word()

    elif choice==4:
        exit()

    else:
        print("The entered value is not allowed!!!!")