#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        my_list = [5]
        x = 0
        ret = 0
        for x >= my_list:
            print("number of elements: {}".format(my_list[]), end="")
            ret += 1
    except(IndexError):
        print("Out of range")
