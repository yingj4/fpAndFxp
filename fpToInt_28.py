# This is the script to convert from floating point nubmers to 32-bit integers
# The number of fractional bits is 28
from ro_4 import *
from fpToInt_16 import hexToInt

def fpToHex(fp):
    m = dict.fromkeys(range(16), 0)

    digit = ord('0')
    c = ord('a')

    for i in range(16):
        if i < 10:
            m[i] = chr(digit)
            digit += 1
        else:
            m[i] = chr(c)
            c += 1

    ret = ""

    if fp < 0:
        fp += 2 ** 4

    fractional = fp % 1
    integral = fp - fractional

    while (integral):
        ret = m[integral % 16] + ret
        integral //= 16

    length = len(ret)
    if length < 1:
        ret = '0' * (1 - length) + ret

    fracBinary = ""
    fracTemp = fractional
    for i in range(28):
        fracTemp *= 2
        if fracTemp >= 1:
            fracBinary += '1'
            fracTemp -= 1
        else:
            fracBinary += '0'

    fracTemp *= 2
    if fracTemp < 1:
        fracStr = hex(int(fracBinary, 2))[2:]
        fracStrLength = len(fracStr)
        if fracStrLength < 7:
            fracStr = '0' * (7 - fracStrLength) + fracStr
        ret += fracStr
    else:
        fracStr = hex(int(fracBinary, 2) + 1)[2:]
        fracStrLength = len(fracStr)
        if fracStrLength < 7:
            fracStr = '0' * (7 - fracStrLength) + fracStr
            ret += fracStr
        elif fracStrLength == 7:
            ret += fracStr
        elif fracStrLength == 8:
            ret = hex(int(ret, 16) + 1)[2:]
            ret += fracStr[1:]
        else:
            return ret

    return ret

def fpToInt(fp):
    return hexToInt(fpToHex(fp))

if __name__ == '__main__':
    # print(fpToInt(conf_8_1))
    # print(fpToInt(conf_9_1))
    # print(fpToInt(conf_10_1))
    # print(fpToInt(conf_11_1))
    print(fpToInt(1.0))
    print(fpToInt(0.5))
    print(fpToInt(2.0))
    print(fpToInt(0.0))
