#!/usr/bin/python3
for d in range(100):
    if d == 99:
        print(d)
    else:
        print("{}".format('0' + str(d) if d < 10 else d), end=", ")
