#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for m in list_num:
        if max_list > m:
            to_sub += m

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for ro_num in list_keys:
            if ro_num == ch:
                if rom_num.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_num.get(ch)]
                else:
                    list_num.append(rom_num.get(ch))

                last_rom = rom_num.get(ch)

    num += to_subtract(list_num)

    return (num)
