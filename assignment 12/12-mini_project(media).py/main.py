from ACTOR import ACTOR
from CLIP import CLIP
from FILM import FILM
from MEDIA import MEDIA
from SERIES import SERIES

Video = []

def read_form_Datase():
    f = open("assignment 12\Database(movie).txt" , "r")

    for line in Video:
        result = line.split(",")
        my_object = {"name": name, "director": director, "IMDB":IMDB, "URL":URL, "duration":duration, "actor":actor} #list of objects
        Video.append(my_object)

    f.close()

def write_to_database():
    open("assignment 12\Database(movie).txt" , "w")
    file = open("assignment 12\Database(movie).txt", "a")

    for video in video :        
        new_name = Video["name"]
        new_director = Video["director"]
        new_imdb = Video["imdb"]
        new_url = Video["url"]
        new_duration = Video["duration"]
        new_actor = Video["actor"]
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
    file.close()

def show_menu():
    print("1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Show info")
    print("6. Download")
    print("6. Exit")


def add():
    new_name = input("Enter the New Name of your Media: ")
    new_director = input("Enter the Director of your Media: ")
    new_imdb = input("Enter the IMDB score of your Media: ")
    new_url = input("Enter the URL of your Media: ")
    new_duration = input("Enter the Duration of your Media: ")
    new_actor = input("Enter the Actor's of your Media: ")
    new_media = {"name": new_name, "director": new_director, "imdb":new_imdb, "url":new_url, "duration":new_duration, "actor":new_actor}
    Video.append(new_media)
    print("Your Media has added successfully.✅")

def edit():
    user_edit = input("Type the name of your Media for editing: ")
    for Video in Video:
        if Video["name"] == user_edit:
            remove_list = {"name":Video["name"], "director":Video["director"] , "IMDB":Video["IMDB"], "URL":Video["URL"], "duration":Video["duration"], "actor":Video["actor"]}
            Video.remove(remove_list)
            new_name = input("Enter the New Name of your Media: ")
            new_director = input("Enter the Director of your Media: ")
            new_imdb = input("Enter the IMDB score of your Media: ")
            new_url = input("Enter the URL of your Media: ")
            new_duration = input("Enter the Duration of your Media: ")
            new_actor = input("Enter the Actor's of your Media: ")
            new_media = {"type": new_type, "name": new_name, "director": new_director, "imdb":new_imdb, "url":new_url, "duration":new_duration, "actor":new_actor}
            Video.append(new_media)
            print("Your media has been found and edited") 
            print("You Can Also Enter Number -5- for Watching the Last List.")
            break       
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List.")


def remove():
    user_remove = input("Type the name of your Media for editing: ")
    for Video in Video:
        if Video["name"] == user_remove:
            remove_list = {"name":Video["name"], "director":Video["director"] , "IMDB":Video["IMDB"], "URL":Video["URL"], "duration":Video["duration"], "actor":Video["actor"]}
            Video.remove(remove_list)
            print("Your Media was found and it deleted from the List") 
            print("You Can Also Enter Number -5- for Watching the Last List")
            break       
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")

def search():
    user_search = input("Please Type the name of Your Media: ")
    for Video in Video:
        if Video["name"] == user_search:
            print(Video["name"],"\t",Video["director"],"\t",Video["IMDB"],Video["URL"],"\t",Video["duration"],"\t",Video["actor"])
            break
    else:
        print("Your Media is not Valid in Our List, Please Enter the Number -5- for Watching the Last List")


def show():
    print(" Name\t Director\t IMDB\t URL\t Duration\t Actor")
    for Video in Video:
            print(Video["name"],"\t",Video["director"],"\t",Video["imdb"],Video["url"],"\t",Video["duration"],"\t",Video["actor"])

def download():
    user_download = input("Enter the name of your Media: ") 
    for Video in Video:
        if Video["name"] == user_download: 
            media = Media(Video["name"], Video["director"], Video["imdb"], Video["url"], Video["duration"], Video["actor"])
            media.download()
            break
    else:
        print("Media not found.")
###########################################################################################################################

print("Hello👋🏻 \n Welcome to my video media refrence.")
print("Loading...⏳")
print("Data loaded.✅")

read_form_Datase()

while True:

    show_menu()

    choice = int(input("Enter your choice: \n >>>>>> \t"))

    if choice==1:
        Video.add()

    elif choice==2:
        id = int(input("Enter the id for Video:"))
        for Video in VideoS:
            if Video.id == id:
                Video.edit()

    elif choice==3:
        id = int(input("Enter the id for Video:"))
        for Video in VideoS:
            if Video.id == id:
                Video.remove()

    elif choice==4:
        Video.search()

    elif choice==5:
        Video.show_info()

    elif choice==6:
        write_to_database()
        exit()

    else:
        print("The entered value is not allowed!!!!")