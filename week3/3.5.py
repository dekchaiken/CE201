def is_palinfrome(word):
    if word[-1] == word[0]:
        return True
    return False

word_list = ['refer' , 'dad' , 'mom' ,'noon' , 'level' ,'radar' , 'help']
# print(len(word_list))
for i in range(0,7,1):
    print(f"word : [{word_list[i]}]  is : palindrome : {is_palinfrome(word_list[i])} " )
