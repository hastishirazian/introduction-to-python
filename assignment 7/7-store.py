import qrcode

PRODUCTS = []
###################################################################################### functions
def read_form_Datase():
    f = open("assignment 7\Database.txt" , "r")

    for line in f:
        result = line.split(",")
        my_dict = { "Code": result[0] , "Name": result[1] , "Price": result[2] , "Count": result[3]}
        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    open("assignment 7\Database.txt" , "w")
    file = open("assignment 7\Database.txt", "a")

    for product in PRODUCTS :
        file.write( f"{product['code']},{product['name']},{product['price']},{product['count']}\n")        
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

def add():
    code = input("Enter the code:")
    name = input("Enter the name:")
    price = input("Enter the price:")
    count = input("Enter the count:")

    new_product = {'code': code , 'name': name , 'price': price , 'count': count}
    PRODUCTS.append(new_product)

def Show_list():
    print("Code \t Name \t price \t count")
    for products in PRODUCTS:
        print(products["coede"],"\t",products["Name"],"\t", products["Price"])

def edit():

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

    Show_list()

    
def remove():
    input_remove = int(input("Enter the code of the product:"))

    for product in PRODUCTS:
        if product['code'] == input_remove:
            PRODUCTS.remove(product)
            print("The desired product has been successfully removed!!")
            Show_list()
            break

        else:
            print("Not found!!!")


def search():
    input_search = input('Enter the name or code of the product you want to search:')
    for product in PRODUCTS:
        if input_search == product['name'] or input_search == product['code']:
            print(products["coede"],"\t",products["Name"],"\t", products["Price"])
    else:
        print("Not found!!!!")


def buy():
    read_form_Datase()
    shopping_list = []
    total_price = 0

    while True:
        input_buy= int(input("Enter the code of the product:"))

        for i in range (len(PRODUCTS)):
            if PRODUCTS[i][Code] == input_buy:
                count_buy = int(input("Enter the number of the product you want:"))
                
                if product['Count'] >= count_buy:
                    product["count"] = int(product["count"]) - count_buy
                    user_product = {"product_code" : product["code"] , "product_name" : product["name"] , "product_price" : product["price"] , "product_count" : user_count}
                    shopping_list.append(user_product)
                    print("product added to your shopping cart.")
                    total_price += int(product["price"]) * user_count

                    choice_continue = input("do you want to 'continue' shopping ? or 'quit' ? enter your choice : ")
                    if choice_continue == "continue" :
                         break 
                    elif choice_continue == "quit" :
                         print("code \t name \t price \t count ")
                         for user_product in shopping_list :
                            print(str(user_product["product_code"])  + "\t" + user_product["product_name"] + "\t" + str(user_product["product_price"]) + "\t" + str(user_product["product_count"]) )
                         print("TOTAL PRICE : " , total_price)
                         exit()

                else:
                    print("There is not enough stock!!!")
                    break


            else:
                print("Not found!!!!")


def qrcode():

    input_qrcode= int(input("Enter the code of the product:"))

    for product in PRODUCTS:
        if product['code'] == input_qrcode:
            info ="Code: {product['code']}, Name: {product['Name']}, Price: {product['Price']}, Count: {product['Count']}"
            img = qrcode.make(info)
            img.save("product_qrcode.png")
        else:
            print("Not found!!!!")

######################################################################################

print("Hello👋🏻 \n Welcome to Haste store.")
print("Loading...")
print("Data loaded.")

read_form_Datase()

while True:

    show_menu()

    choice = int(input("Enter your choice: \n >>>>>> \t"))

    if choice==1:
        add()

    elif choice==2:
        edit()

    elif choice==3:
        remove()

    elif choice==4:
        search()

    elif choice==5:
        Show_list()

    elif choice==6:
        buy()

    elif choice==7:
        qrcode()

    elif choice==8:
        write_to_database()
        exit()

    else:
        print("The entered value is not allowed!!!!")
