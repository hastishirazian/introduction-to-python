class Media():

    #properties
    def __init__(self , name , director , IMDB ,URL , duration , casts):
        self.name = name
        self.director = director
        self.IMDB_score = IMDB
        self.URL = URL
        self.duration = duration
        self.casts = casts

    #methods
    def show_info():
        ...
    
    def download():
        ...

    def add():
        add_name = input("Enter the name::")
        add_director = input("Enter the director's name:")
        add_IMDB = input("Enter the IMDB:")
        add_URL = input("Enter the url:")
        add_durtion =input("Enter the duration:")
        add_casts = input("Enter the cast:")

        add_new_media = media(result[0] , result[1] , result[2] , result[3] , result[4] , result[5])
        MEDIA.append(add_new_media)    

    def edit():
        print("1. Name")
        print("2. director's name")
        print("3. IMDB")
        print("4. url")
        print("5. duration")
        print("6. cast")


        print("Which part of the media information do you want to edit?")
        choice = int(input("Enter the code of the part:"))

        for i in range (len(MOVIES)):
            if PRODUCTS[i]["code"] == input_code:
                if input_edit== 1:
                    new_name = input("Enter the new name for product:")
                    PRODUCTS[i]['name'] = new_name
                    print("Information updated successfully!!!!")
                elif input_edit== 2:
                    new_price= input("Enter the new price for product:")
                    PRODUCTS[i]['price'] = new_price
                    print("Information updated successfully!!!!")
                elif input_edit== 3:
                    new_count = input("Enter the new count for product:")
                    PRODUCTS[i]['count'] = new_count
                    print("Information updated successfully!!!!")
            else:
                print("product not found!!!!")
        show_list()


    def remove():
        ...

    def search():
        ...


class Film(Media):
    def __init__():
        super().__init__()


class Series(Media):
    def __init__():
        super().__init__()
    

class Documentary(Media):
    def __init__():
        super().__init__()
    

class Clip(Media):
    ...
##############################################################################################################################
MOVIES = []

def read_form_Datase():
    f = open("assignment 12\Database(movie).txt" , "r")

    for line in f:
        result = line.split(",")
        my_object = Product(result[0] , result[1] , result[2] , result[3]) #list of objects
        PRODUCTS.append(my_object)

    f.close()

def write_to_database():
    open("assignment 12\Database(movie).txt" , "w")
    file = open("assignment 12\Database(movie).txt", "a")

    for product in PRODUCTS :
        file.write("{product['code']},{product['name']},{product['price']},{product['count']}\n")        
    file.close()

def show_menu():
    print("1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Show info")
    print("6. Exit")
###########################################################################################################################

print("Hello👋🏻 \n Welcome to my video media refrence.")
print("Loading...⏳")
print("Data loaded.✅")

read_form_Datase()

while True:

    show_menu()

    choice = int(input("Enter your choice: \n >>>>>> \t"))

    if choice==1:
        Product.add()

    elif choice==2:
        id = int(input("Enter the id for product:"))
        for product in PRODUCTS:
            if product.id == id:
                product.edit()

    elif choice==3:
        id = int(input("Enter the id for product:"))
        for product in PRODUCTS:
            if product.id == id:
                product.remove()

    elif choice==4:
        Product.search()

    elif choice==5:
        Product.show_info()

    elif choice==6:
        write_to_database()
        exit()

    else:
        print("The entered value is not allowed!!!!")