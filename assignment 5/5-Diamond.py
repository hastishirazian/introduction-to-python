def diamond(row):
    for i in range(1 , row+1):
        print((row- i) * " " + i * " *")

    for j in range(1 , row):
        print( j * " " + (row - j) * " *" )


row = int(input("Enter row:"))
diamond(row)