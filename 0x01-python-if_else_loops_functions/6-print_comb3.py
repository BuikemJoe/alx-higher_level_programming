#!/usr/bin/python3
for m in range(100):
    if int(m / 10) != m % 10 and int(m / 10) < m % 10:
        print("{}{}".format(int(m / 10), m % 10), end="")
        if (m != 89):
            print(", ", end="")
print("")
