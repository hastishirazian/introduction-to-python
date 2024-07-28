from Actor import Actor
from Clip import Clip
from Film import Film
from Media import Media
from Series import Series

Video = []

def read_from_database():
    file = open("F:/Python/Projects/PyLearn-Course/Assignments-12/Data.txt", "r")
    for line in file:
        result = line.strip().split(",")
        my_dict = {"type": result[0], "name": result[1], "director": result[2], "imdb": result[3], "url": result[4], "duration": result[5], "actor": result[6]}
        Video.append(my_dict)   
    file.close
    
def write_to_database():
    file = open("F:/Python/Projects/PyLearn-Course/Assignments-12/Data.txt", "w")
    for product in Video:
        new_type = product["type"]
        new_name = product["name"]
        new_director = product["director"]
        new_imdb = product["imdb"]
        new_url = product["url"]
        new_duration = product["duration"]
        new_actor = product["actor"]
        file.write(new_type)
        file.write(",")
        file.write(new_name)
        file.write(",")
        file.write(new_director)
        file.write(",")
        file.write(new_imdb)
        file.write(",")
        file.write(new_url)
        file.write(",")
        file.write(new_duration)
        file.write(",")
        file.write(new_actor)
        file.write("\n")
    file.close

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show")
    print("6- Download")
    print("7- Exit")

def add():
    new_type = input("Enter type of your New Media: ")
    new_name = input("Enter the New Name of your Media: ")
    new_director = input("Enter the Director of your Media: ")
    new_imdb = input("Enter the IMDB score of your Media: ")
    new_url = input("Enter the URL of your Media: ")
    new_duration = input("Enter the Duration of your Media: ")
    new_actor = input("Enter the Actor's of your Media: ")
    new_media = {"type": new_type, "name": new_name, "director": new_director, "imdb":new_imdb, "url":new_url, "duration":new_duration, "actor":new_actor}
    Video.append(new_media)
    print("Your Media has added successfully.")

def edit():
    user_edit = input("Type the name of your Media for editing: ")
    for product in Video:
        if product["name"] == user_edit:
            remove_list = {"type":product["type"], "name":product["name"], "director":product["director"] , "imdb":product["imdb"], "url":product["url"], "duration":product["duration"], "actor":product["actor"]}
            Video.remove(remove_list)
            new_type = input("Enter type of your New Media: ")
            new_name = input("Enter the New Name of your Media: ")
            new_director = input("Enter the Director of your Media: ")
            new_imdb = input("Enter the IMDB score of your Media: ")
            new_url = input("Enter the URL of your Media: ")
            new_duration = input("Enter the Duration of your Media: ")
            new_actor = input("Enter the Actor's of your Media: ")
            new_media = {"type": new_type, "name": new_name, "director": new_director, "imdb":new_imdb, "url":new_url, "duration":new_duration, "actor":new_actor}
            Video.append(new_media)
            print("Your Media was found and it Edited to the List") 
            print("You Can Also Enter Number -5- for Watching the Last List")
            break       
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def remove():
    user_remove = input("Type the name of your Media for editing: ")
    for product in Video:
        if product["name"] == user_remove:
            remove_list = {"type":product["type"], "name":product["name"], "director":product["director"] , "imdb":product["imdb"], "url":product["url"], "duration":product["duration"], "actor":product["actor"]}
            Video.remove(remove_list)
            print("Your Media was found and it deleted from the List") 
            print("You Can Also Enter Number -5- for Watching the Last List")
            break       
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def search():
    user_search = input("Please Type the name of Your Media: ")
    for product in Video:
        if product["name"] == user_search:
            print(product["type"],"\t",product["name"],"\t",product["director"],"\t",product["imdb"],product["url"],"\t",product["duration"],"\t",product["actor"])
            break
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def show():
    print("Type\t Name\t Director\t IMDB\t URL\t Duration\t Actor")
    for product in Video:
            print(product["type"],"\t",product["name"],"\t",product["director"],"\t",product["imdb"],product["url"],"\t",product["duration"],"\t",product["actor"])

def download():
    user_download = input("Enter the name of your Media: ") 
    for product in Video:
        if product["name"] == user_download: 
            media = Media(product["name"], product["director"], product["imdb"], product["url"], product["duration"], product["actor"])
            media.download()
            break
    else:
        print("Media not found.")


print("Welcome to the AmirrezA Media shop")
print("Loading...")
read_from_database()
print("Media Loaded.")
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show()
    elif choice == 6:
        download()
    elif choice == 7:
        write_to_database()
        exit(0)
    else:
        print("Your Number is NOT CORRECT, Please Enter a Valid Number")