def multiplication_table(m, n):
    for i in range(1 , m+1):
        for j in range(1 , n+1):
            result = (i * j)
            print(result , end="\t")
        print()

m = int(input("Enter m:"))
n = int(input("Enter n:"))
multiplication_table(m, n)