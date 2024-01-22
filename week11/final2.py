def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(num)
    return avg


print("The average of List is", averageOfList([1, 2, 3, -1, -2, -3, 5, 6]))


def averageOfList(numOfList):
    avg = sum(numOfList) / len(numOfList)
    return avg


print("The average of List is", round(averageOfList([30, 20, 30, -15, -24, -35, 53, -60]), 2))