print('Your answer')
max = int(input('Maximun number:'))
i = 0
number = 1
correct = 0
incorrect = 0
score = 0


def fizzbuzz(i): # ต้องมีพารามิเตอร์ เพื่อรับค่ามาคำนวณ
    if i % 3 == 0 and i % 5 == 0:
        return "fb"
    elif i % 3 == 0:
        return "f"
    elif i % 5 == 0:
        return "b"
    else:
        return i


for x in range(1, max+1):
    if incorrect == 3:
        print('You have answered wrong 3 times.')
        break
    num = input(f'{number} : ')
    if num == '0':
        print('The game has stopped.')
        break
    number += 1
    if num == 'f' and fizzbuzz(x) == 'f':
        correct += 1
        score += 1
    elif num == 'b' and fizzbuzz(x) == 'b':
        correct += 1
        score += 1
    elif num == 'fb' and fizzbuzz(x) == 'fb':
        correct += 1
        score += 1
    elif fizzbuzz(x) == x and num.isdigit() == True:
        if int(num) == x: # ต้องให้ num เป็นตัวเลข เพราะว่ารับมาเป็นตัวอักษร
            correct += 1
            score += 1
        else:
            incorrect += 1
            score -= 2
    else:
        incorrect += 1
        score -= 2

print('correct: ', correct)
print('incorrect: ', incorrect)
print('score: ', score)