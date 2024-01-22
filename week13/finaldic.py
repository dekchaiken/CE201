def averrage_neg(num):
    newnum = 0
    averrage = 0
 
    for i in num:
        if i < 0:
            newnum += i
            averrage += 1
    ans = newnum/averrage
    return ans
 
averrage_neg([1, 2, 3, -1, -2, -3, 5, 6])