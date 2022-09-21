#!/usr/bin/python3
def uppercase(str):
    for alpha in range(len(str)):
        if ord(str[alpha]) >= 97 and ord(str[alpha]) < 123:
            letter = 32
        else:
            letter = 0
        print("{c}".format(ord(str[alpha]) - letter), end="")
    print()
