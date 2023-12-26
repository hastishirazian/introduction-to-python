print("Please fill an array.")

a=[]

while 1==1:
    number = input("number:")

    if number =="end":
        print("Array is full.")
        break

    else:
        a.append(number)

for i in range (len(a)-1):

    if a[i]<a[i+1] and a[i-1]<a[i]:
        print("Unsorted ascending array❌")
        break

    else:
        print("Sorted ascending array✅")
        break