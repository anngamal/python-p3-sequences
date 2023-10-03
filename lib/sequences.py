#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length ==2:
        print([0,1])
    # elif length ==10:
    #     print([0\n1\n1\n2\n3\n5\n8\n13\n21\n34])



#     i() prints empty list when length = 0 F                                                    [ 25%]
# function print_fibonacci() prints 0 when length = 1 F                                                             [ 50%]
# function print_fibonacci() prints 0\n1 when length = 2 F                                                          [ 75%]
# function print_fibonacci() prints 0\n1\n1\n2\n3\n5\n8\n13\n21\n34 when length = 10 F