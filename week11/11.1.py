def is_zero(matrix):
    ans_0 = 0
    for i in matrix:
        ans_0 += i.count(0)

    if ans_0 == len(matrix)**2:
        return True
    else:
        return False


