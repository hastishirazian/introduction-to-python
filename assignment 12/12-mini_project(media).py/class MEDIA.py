class MEDIA():

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

        add_new_media = media(result[0] , result[1] , result[2] , result[3] , result[4] , result[5]) #list of objects
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

        if choice == 1:
            print("Which movie name you wanna edit? /t enter the name.")
            input_name = input()
            for i in range (len(MOVIES)):
                if [i]["name"] == input_name:
                        new_name = input("Enter the new name for movie:")
                        PRODUCTS[i]['name'] = new_name
                        print("Information updated successfully!!!!")
        elif choice == 2:
                    elif input_edit== 2:
                        new_price= input("Enter the new price for product:")
                        PRODUCTS[i]['price'] = new_price
                        print("Information updated successfully!!!!")
        elif choice ==3:
                    elif input_edit== 3:
                        new_count = input("Enter the new count for product:")
                        PRODUCTS[i]['count'] = new_count
                        print("Information updated successfully!!!!")
        elif choice == 4:
            ...
        elif choice == 5:
            ...
        elif choice == 6:
            ...
        else:
            print("product not found!!!!")

            show_list()


    def remove():
        ...

    def search():
        ...