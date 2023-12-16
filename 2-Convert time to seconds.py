print("Please enter the time.")

Converted_hour= 0
Converted_minute= 0
Converted_time= 0

x = int(input("hour:"))
#hour can be a number between 1 to 24
y = int(input("minute:"))
#minute can be a number between 0 to 60
z = int(input("second:"))
#second can be a number between 0 to 60

print("Time:" , x ,":", y ,":", z ,)

Converted_hour = (x*3600)
Converted_minute= (y*60)

Converted_time= Converted_hour +Converted_minute +z
print("Converted time is:" , Converted_time)