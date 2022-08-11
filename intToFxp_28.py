# This is the script to convert from 32-bit integers to fixed point numbers
# The number of fractional bits is 28

from intToFxp_16 import intToHex
from ro_4 import *
import numpy as np

def hexToFxp(hex):
    ret = 0.0
    hexToIntDict = {}
    digit = ord('0')
    c = ord('a')
    for i in range(16):
        if i < 10:
            hexToIntDict[chr(digit)] = float(i)
            digit += 1
        else:
            hexToIntDict[chr(c)] = float(i)
            c += 1

    if ord(hex[0]) >= ord('0') and ord(hex[0]) <= ord('7'):
        for i in range(8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == '8':
        ret += -1 * (2 ** 3)
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == '9':
        ret += (-1 * (2 ** 3) +(2 ** 0))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'a':
        ret += (-1 * (2 ** 3) + (2 ** 1))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'b':
        ret += (-1 * (2 ** 3) + (2 ** 1) + (2 ** 0))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'c':
        ret += (-1 * (2 ** 3) + (2 ** 2))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'd':
        ret += (-1 * (2 ** 3) + (2 ** 2) + (2 ** 0))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'e':
        ret += (-1 * (2 ** 3) + (2 ** 2) + (2 ** 1))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    elif hex[0] == 'f':
        ret += (-1 * (2 ** 3) + (2 ** 2) + (2 ** 1) +  (2 ** 0))
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (0 - 4 * i))
    else:
        return ret

    return ret

def intToFxp(integer):
    return hexToFxp(intToHex(integer))

if __name__ == '__main__':
    print(intToFxp(724775))
    print(intToFxp(75967))
    print(intToFxp(74625))
    print(intToFxp(48855))
    print(intToFxp(128849))
    print(intToFxp(0))
    print(intToFxp(-8053))
    print(intToFxp(0))
    print(intToFxp(-59055))
    print(intToFxp(28454))
