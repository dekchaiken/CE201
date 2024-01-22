def duplicate_id():
    a_list = [650109090001, 650109090002, 650109090003, 650109090004, 650109090005]
    a_set = set(a_list)
    duplicate = len(a_list) != len(a_set)
    print(duplicate)

duplicate_id()

'''def duplicate_id():
    udid = [650109090001, 650109090002, 650109090003, 650109090004, 650109090005]
    contains_duplicates = any(udid.count(element) > 1 for element in udid)
    print(contains_duplicates)
duplicate_id()'''

'''l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')
 
 len(your_list) != len((your_list))'''