def chop(lst):
    list1 = []
    for i in range(len(lst)-2):
        list1.append(lst[i+1])
    print(list1)
    return None
 
list1 = [1, 3, 5]
list2 = [0, 1, 2, 3, 4, 5]
list3 = [3, 3, 3, 3, 3, 3, 3]
 
chop(list1)
