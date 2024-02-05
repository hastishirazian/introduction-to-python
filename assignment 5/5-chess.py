def chess(m , n):

    for i in range(m):
        for j in range(n):
            result = (i+j)

            if ((result % 2) == 0):
                print ("*" , end="\t")
            else:
                print("#" , end="\t")
            
        print()

m = int(input("Enter m:"))
n=  int(input("Enter n:"))
chess( m , n)