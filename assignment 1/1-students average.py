print("Enter the name and the scores of each student.")

student1=input("student 1:")
score1s1=int (input("score 1:"))
score2s1=int (input("score 2:"))
score3s1=int (input("score 3:"))


student2=input("student 2:")
score1s2=int (input("score 1:"))
score2s2=int (input("score 2:"))
score3s2=int (input("score 3:"))

student3=input("student 3:")
score1s3=int (input("score 1:"))
score2s3=int (input("score 2:"))
score3s3=int (input("score 3:"))

avg1=(score1s1+score2s1+score3s1)/3
avg2=(score1s2+score2s2+score3s2)/3
avg3=(score1s3+score2s3+score3s3)/3

#student 1
if avg1>=17:
    result1="Great :)"

elif 12<=avg1 <17:
    result1="Normal"

elif avg1<12:
    result1="Fail :("

#student 2
if avg2>=17:
    result2="Great :)"

elif 12<=avg2<17:
    result2="Normal"

elif avg2<12:
    result2="Fail :("

#student 3
if avg3>=17:
    result3="Great :)"

elif 12<=avg3<17:
    result3="Normal"

elif avg3<12:
    result3="Fail :("

print("status of student 1:")
print(result1)
print("status of student 2:")
print(result2)
print("status of student 3:")
print(result3)