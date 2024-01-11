print("Please enter the number:")
x = int(input("seconds:"))

hour = x/3600
y = x%3600

minute = y/60
seconds = y%60

#hour can be 
print(" Time:" , int(hour) ,":", int(minute) , ":" , seconds)