#!/usr/bin/python3

m = 0
for s in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(s - m)), end="")
    m = 32 if m == 0 else 0
