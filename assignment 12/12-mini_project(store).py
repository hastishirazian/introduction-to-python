import qrcode

class product():
    def __init__(self , i , n , p , c):
        self.id = ...
        self.name = ...
        self.price = ...
        self.count = ...

    @staticmethod
    def add():

        code = input("Enter the code:")
        name = input("Enter the name:")
        price = input("Enter the price:")
        count = input("Enter the count:")

        new_product = Product(code , name , price ,  count)
        PRODUCTS.append(new_product)

    def edit(self):
        print("1. Name")
        print("2. Price")
        print("3. Count")
        input_edit = int(input("Which part of the product information do you want to edit?"))

        input_code = int(input("Enter the code of the product:"))

        for i in range (len(PRODUCTS)):
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

    @staticmethod
    def search():
        ...

    def show(self):
        ...

    @staticmethod
    def show_list(self):
        ...

    def remove(self):
        ...

    def buy(self):
        ...


PRODUCTS = []

def read_form_Datase():
    f = open("assignment 12\Database.txt" , "r")

    for line in f:
        result = line.split(",")
        my_object = Product(result[0] , result[1] , result[2] , result[3]) #list of objects
        PRODUCTS.append(my_object)

    f.close()

def write_to_database():
    open("assignment 12\Database.txt" , "w")
    file = open("assignment 12\Database.txt", "a")

    for product in PRODUCTS :
        file.write("{product['code']},{product['name']},{product['price']},{product['count']}\n")        
    file.close()

def show_menu():
    print("1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Show list")
    print("6. Buy")
    print("7. QR code")
    print("8. Exit")

######################################################################################

print("Hello👋🏻 \n Welcome to Haste store.")
print("Loading...")
print("Data loaded.")

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
                product.edit()

    elif choice==4:
        Product.search()

    elif choice==5:
        Product.Show_list()

    elif choice==6:
        buy()

    elif choice==7:
        make_qrcode()

    elif choice==8:
        write_to_database()
        exit()

    else:
        print("The entered value is not allowed!!!!")