import random
randnum = random.randint(0, 100)
count = 0
for i in range(5):
    count = count+1
    guess = int(input("Try to guess the number from 0-100 : "))
    if guess == randnum:
        print("คำตอบนั้นถูกต้อง")
        break
    elif guess < randnum:
        print("ตัวเลขที่ทายมีค่าน้อยเกินไป")
    else:
        print("ตัวเลขที่ทายมีค่ามากเกินไป")
if count == 5:
    print("ขอบคุณ")
