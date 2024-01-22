lab = int(input("กรอกคะแนน Lab : "))
mid = int(input("กรอกคะแนน Midterm : "))
final = int(input("กรอกคะแนน Final : "))
x = int(lab+mid+final)
if x <= 100 and x >= 80:
    print("คะแนนของคุณคือ "+str(x)+" ได้เกรด A")
elif x <= 79 and x >= 70:
    print("คะแนนของคุณคือ "+str(x)+" ได้เกรด B")
elif x <= 69 and x >= 60:
    print("คะแนนของคุณคือ "+str(x)+" ได้เกรด C")
elif x <= 59 and x >= 50:
    print("คะแนนของคุณคือ "+str(x)+" ได้เกรด D")
elif x <= 49 and x >= 0:
    print("คะแนนของคุณคือ "+str(x)+" ได้เกรด F")
elif x >= 101:
    print("Error : Value must be less than or equal to 100.")
elif x < 0:
    print("Error : Value must be greater than or equal to 0.")
else:
    ()
