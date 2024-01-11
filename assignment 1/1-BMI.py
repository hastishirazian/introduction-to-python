a= float(input("please enter your weight:"))
b= float(input("please enter your height:"))
#The unit of measurement for height is "meters" and for weight is "kilograms".

bmi= a/b**b

if bmi<18.5:
    result= "under weight"

elif 18.5<= bmi <=24.9:
    result= "normal weight"

elif 25<= bmi <=29.9:
    result= "over weight"

elif 30<= bmi <=34.9:
    result= "obesity"

elif 35<= bmi <=39.9:
    result= "extreme obesity"

elif 40<bmi:
    result= "not in the range."


print("Your BMI is:",bmi)
print("status:", result)