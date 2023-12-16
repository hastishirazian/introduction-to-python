input("What is the name of student?")
print("Enter the scores.")

sum = 0
score_number = 0

while 1==1:
    score = (input("score:"))

    if score =="exit":
        print("It ends.")
        break

    else:
        print("Thanx.")
        score = float(score)
        sum+=score
        score_number=score_number+1

avg=sum/score_number
print("The avrage:" , avg)
        