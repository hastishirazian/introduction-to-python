print("Please enter the number:")
x = int(input("seconds:"))

hour = x//3600
y = x%3600

minute = y//60
seconds = y%60

#hour can be a number between 1 to 24
#minute can be a number between 0 to 6
#second can be a number between 0 to 60

print(" Time:" , hour ,":", minute , ":" , seconds)
