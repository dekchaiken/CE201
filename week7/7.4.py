def is_sorted(lst):
    a = lst[0]
    for i in range(len(lst)):
        if a <= lst[i]:
            a = lst[i]
        else:
            return False
    return True
list1 = [1,3,3]
list2 = [0,1,2,3]
list3 = [3,3,3]
list4 = [9,5,2]
list5 = [100,10,1]
list6 = ['a','b','c']
list7 = ['z','z','z']
list8 = ['c','b','a']
 
print(is_sorted(list1))
print(is_sorted(list2))
print(is_sorted(list3))
print(is_sorted(list4))
print(is_sorted(list5))
print(is_sorted(list6))
print(is_sorted(list7))
print(is_sorted(list8))
