message_ = '“Make it work, make it right, make it fast.”'
author_ = 'Kent Beck' 


def quote(message , author):
    return  message.upper()+'- '+author.lower()

print(quote(message_ , author_))
