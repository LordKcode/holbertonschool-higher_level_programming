#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = []
    for i in range(len(roman_string) - 1, -1, -1):
        if i == len(roman_string) - 1:
            largestNum = d[roman_string[i]]
        if d[roman_string[i]] < largestNum:
            num.append(largestNum - d[roman_string[i]])
            num.remove(largestNum)
            largestNum = d[roman_string[i]]
        else:
            num.append(d[roman_string[i]])
            largestNum = d[roman_string[i]]
    return sum(num)
