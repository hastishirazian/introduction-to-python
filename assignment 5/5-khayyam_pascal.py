def kayyam_pascal(rows):

    a = []

    for i in range(rows):
        row = [1] * (i + 1)

        if (i > 1):
            for j in range(1, i):
                row[j] = a[i - 1][j - 1] + a[i - 1][j]
    
        a.append(row)
    return a


rows = int(input("Enter the number of rows:"))

kayyam_pascal(rows)
for row in kayyam_pascal(rows):
    print(row)















# n = int(input("Enter n:"))
# kayyam_pascal(n)