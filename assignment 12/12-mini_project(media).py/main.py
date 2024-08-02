from mediaclass import Media
from filmclass import Film
from seriesclass import Series
from documentaryclass import Documentary
from clipclass import Clip

MEDIA = []

def read_from_database():
    try:
        with open("assignment 12/12-mini_project(media).py\\movie.txt", "r") as d:
            for line in d:
                res = line.strip().split(",")
                if len(res) == 10:
                    if res[0] == "film":
                        my_obj = Film(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])
                    elif res[0] == "series":
                        my_obj = Series(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8])
                    elif res[0] == "documentary":
                        my_obj = Documentary(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])
                    else:
                        my_obj = Clip(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[9])
                    MEDIA.append(my_obj)
    except FileNotFoundError:
        print("Database file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_database():
    try:
        with open("assignment 12/12-mini_project(media).py\\movie.txt", "w") as d:
            for m in MEDIA:
                if m.type == "film" or m.type == "documentary":
                    d.write(f"{m.type},{m.name},{m.director},{m.imdb_score},{m.url},{m.duration},{m.casts},{m.productionyear},1,---\n")
                elif m.type == "series":
                    d.write(f"{m.type},{m.name},{m.director},{m.imdb_score},{m.url},{m.duration},{m.casts},{m.productionyear},{m.episodnumber},---\n")
                else:
                    d.write(f"{m.type},{m.name},{m.director},{m.imdb_score},{m.url},{m.duration},{m.casts},{m.productionyear},1,{m.genre}\n")
        print("Saved successfully")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Advanced Search")
    print("6-Show list")
    print("7-Show a media's info")
    print("8-Download")
    print("9-Save changes")
    print("10-Exit")
    print()

def add():
    type = input("Enter type of media: ")
    name = input("Enter name of media: ")
    director = input("Enter director of media: ")
    imdb_score = input("Enter IMDB score of media: ")
    url = input("Enter uniform resource locator of media: ")
    duration = input("Enter duration of media: ")
    casts = input("Entre casts of media(separate with |): ")
    production_year = input("Enter production year of media: ")
    if type == "film":
        new_film = Film(type, name, director, imdb_score, url, duration, casts, production_year)
        MEDIA.append(new_film)
    elif type == "documentary":
        new_documentary = Documentary(type, name, director, imdb_score, url, duration, casts, production_year)
        MEDIA.append(new_documentary)
    elif type == "series":
        episod_number = input("Enter number of episodes of series: ")
        new_series = Series(type, name, director, imdb_score, url, duration, casts, production_year, episod_number)
        MEDIA.append(new_series)
    else:
        genre = input("Enter genre of clip:")
        new_clip = Clip(type, name, director, imdb_score, url, duration, casts, production_year, genre)
        MEDIA.append(new_clip)

def edit():
    name = input("Please enter the intended media name:")
    for i in range(len(MEDIA)):
        if MEDIA[i].name == name:
            print("Which field do you want to edit? \n 1-Director \n 2-URL")
            ch = int(input("Enter your choice:"))
            new_data = input("Please enter the new data:")
            if ch == 1:
                MEDIA[i].director = new_data
                print("Successfully edited!")
            elif ch == 2:
                MEDIA[i].url = new_data
                print("Successfully edited!")
            else:
                print("Incorrect choice!!")
            break
    else:
        print("Not found!")

def remove():
    name = input("Please enter the intended media name:")
    for media in MEDIA:
        if media.name == name:
            MEDIA.remove(media)
            print("Successfully removed..")
            break
    else:
        print("Not found!")

def search():
    user_input = input("Type your keyword:")
    for media in MEDIA:
        if media.name == user_input or media.director == user_input:
            print(f"{media.type}\t\t{media.name}\t\t{media.director}\t\t{media.imdb_score}\t\t{media.url}\t\t{media.casts}\t\t{media.productionyear}")
            break
    else:
        print("Not found!")

def advanced_search():
    i = int(input("Enter minimum time(in seconds): "))
    e = int(input("Enter maximum time(in seconds): "))
    n = 0
    for media in MEDIA:
        if i <= int(media.duration) <= e:
            media.showinfo()
            n += 1
    if n == 0:
        print(f"Not found any media with duration between {i} and {e} seconds!")

def show_list():
    print("name \t   director \t    IMDBscore \t duration \t\t casts  \t\t production year ")
    print("----------------------------------------------------------------------------------------------------")
    for media in MEDIA:
        print(f"{media.name}\t\t{media.director}\t\t{media.imdb_score}\t\t{media.duration}\t\t{media.casts}\t\t{media.productionyear.strip()}")
        print("--------------------------------------------------------------------")

###############################################################################################################################################################
read_from_database()
print("Data loaded.")

while True:
    menu()
    choice = int(input("Please enter your choice:"))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        advanced_search()
    elif choice == 6:
        show_list()
    elif choice == 7:
        na = input("\n Please enter media's name: ")
        for m in MEDIA:
            if m.name == na:
                m.download()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print("❌Incorrect input!❌")
