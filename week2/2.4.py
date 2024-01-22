def print_say(hi):
    print('HELOO')

def do_twice(func,Values):
    func(Values)
    func(Values)

#do_twice(print_say,'HELLO')

def do_four(func,Values):
    do_twice(print_say,Values)
    do_twice(print_say,Values)

do_four(do_twice,'HELOO')
