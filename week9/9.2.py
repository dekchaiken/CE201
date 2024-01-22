num = int(input())
score = 0
fail = 0
answer_t = 0
answer_f = 0
print(f"Maximum number: {num}")
print("your answer")
for i in range(1, num + 1):
    if answer_f == 3:
        print("You have answered wrong 3 times.")
        break
    a = input(f"{i} : ")
    if a == '0':
        print("The game has stopped.")
        break
    if a == 'f' and i % 3 == 0:
        score += 1
        answer_t += 1
    elif a == 'b' and i % 5 == 0:
        score += 1
        answer_t += 1
    elif a == 'fb' and i % 3 == 0 and i % 5 == 0:
        score += 1
        answer_t += 1
    elif a.isdigit() == True and i % 3 != 0 and i % 5 != 0:
        if int(a) == i:
            score += 1
            answer_t += 1
        else:
            answer_f += 1
            score -= 2
    else:
        answer_f += 1
        score -= 2

print(f"Correct : {answer_t} times")
print(f"Incorrect : {answer_f} times")
print(f"Score : {score}")