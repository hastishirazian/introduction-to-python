from actor import Actor
from clip import Clip
from film import Film
from media import Media
from series import Series 
from documentary import Documentary

def show_menu():
    print("1️⃣ Add ")
    print("2️⃣ Edit ")
    print("3️⃣ Delete ")
    print("4️⃣ Search")
    print("5️⃣ Download ")
    print("6️⃣ Show ")
    print("7️⃣ Write to database and Exit")


video = []
def read_from_database():
    file = open("assignment 12/12-mini_project(media).py/data.txt", "r")
    for line in file:
        result = line.split(",")
        my_dic = {"type" : result[0], "name" : result[1], "director" : result[2], "imdb_score" : result[3], "url" : result[4],"duration" : result[5], "actor" : result[6] }     
        video.append(my_dic)
    file.close()


def write_to_database():
     file = open("assignment 12/12-mini_project(media).py/data.txt", "w")
     for i in range(len(video)):
        data = str(video[i]["type"])+','+ str(video[i]["name"])+','+ str(video[i]["director"])+','+ str(video[i]["imdb_score"])+','+ str(video[i]["url"])+','+ str(video[i]["duration"])+','+ str(video[i]["actor"])+'\n'  
        file.write(data)
     file.close()   


def add_media():
    new_type = input("🔶 Enter type of Media:")
    new_name = input("🔶 Enter the Name of Media:")
    new_director = input("🔶 Enter the name of Director:")
    new_imdb_Score = input("🔶 Enter Media's IMDB Score: ")
    new_url = input("🔶 Enter Media's url: ")
    new_duration = input("🔶 Enter Media's duration: ")
    new_actor = input("🔶 Enter the actor's name:")
    new_media ={"type" : new_type, "name" : new_name, "director" : new_director,"imdb_score" : new_imdb_Score ,"url" : new_url, "duration" : new_duration, "actor" : new_actor }   
    video.append(new_media)
    print("🔶 Done ✔ ")
 

def edit_media():
   user_input = input("🔶 Enter the name of Media: ")
   for obj in video:
        if obj['name'] == user_input:
                print(" 1️⃣ Edit Media's type")
                print(" 2️⃣ Edit Name of Media")
                print(" 3️⃣ Edit name of Director")
                print(" 4️⃣ Edit Media's IMDB Score")
                print(" 5️⃣ Edit Media's url")
                print(" 6️⃣ Edit Media's duration")
                print(" 7️⃣ Edit name and lastname of the actor")
                print(" 8️⃣ Exit")

                while True:
                    choice = int(input("🔶 Enter your choice:"))
                    if choice == 1:
                        obj['type'] = input("🔶 Enter new type : ")
                        print('Done ✔')
                    elif choice == 2:
                        obj['name'] = float(input("🔶 Enter new name : "))
                        print('Done ✔')
                    elif choice == 3:
                        obj['director']=int(input("🔶 Enter new director : "))
                        print("Done ✔ ")
                    elif choice == 4:
                        obj['imdb_score']=int(input("🔶 Enter new imdb_score : "))
                        print("Done ✔ ")
                    elif choice == 5:
                        obj['url']=int(input("🔶 Enter new url : "))
                        print("Done ✔ ")
                    elif choice == 6:
                        obj['duration']=int(input("🔶 Enter new duration : "))
                        print("Done ✔ ")                                                
                    elif choice == 7:
                        obj['actor']=int(input("🔶 Enter new actor : "))
                        print("Done ✔ ")                       
                    elif choice == 8:
                        break  
                    else:
                        print('🔶 This Media dose not exist.')

                       
def remove_media():
    user_input = input("🔶 Enter name of media: ")
    for obj in video:
        if obj['name'] == user_input :
            video.remove(obj)
            print("Done ✔ ")
            break
    else:
        print('🔶 This Media dose not exist.')
                  

def search_media():
    user_input = input("🔶 Enter name of media: ")
    for obj in video:
        if obj['name'] == user_input:
            print(obj["type"],"\t\t", obj["name"],"\t\t", obj["director"],"\t\t", obj["imdb_score"], "\t\t", obj["url"], "\t\t", obj["duration"], "\t\t", obj["actor"])
            break
    else:
         print("🔶 This Media dose not exist.")
         
def download():
    user_input = input("🔶 Enter name of media: ") 
    for i in range (len(video)):
        if video[i].name == user_input: 
            video[i].download()
            print("done ✔ ") 
 
  

         
def show_media(): 
    user_input = input("🔶 Enter name of media: ") 
    for obj in video:
        if obj['name'] == user_input:
            print(obj["type"],"\t\t", obj["name"],"\t\t", obj["director"],"\t\t", obj["imdb_score"], "\t\t", obj["url"], "\t\t", obj["duration"], "\t\t", obj["actor"])   

print("🔶 Welcome to Media store")
read_from_database()
print("🔶 Data Loaded... ")

while True:
    show_menu()
    user_choice = int(input("🔶enter your choice: "))
    if user_choice == 1:
        add_media()
    elif user_choice == 2:
        edit_media()
    elif user_choice == 3:
        remove_media()
    elif user_choice == 4:
        search_media()
    elif user_choice == 5:
        download()
    elif user_choice == 6:
        show_media()
    elif user_choice == 7:
        write_to_database()
        exit(0)