# This is the script to convert from floating point nubmers to 32-bit integers
from ro_4 import *
import numpy as np
from intToFxp import *

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
        fp += 2 ** 16

    fractional = fp % 1
    integral = fp - fractional

    while (integral):
        ret = m[integral % 16] + ret
        integral //= 16

    length = len(ret)
    if length < 4:
        ret = '0' * (4 - length) + ret

    fracBinary = ""
    fracTemp = fractional
    for i in range(16):
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
        if fracStrLength < 4:
            fracStr = '0' * (4 - fracStrLength) + fracStr
        ret += fracStr
    else:
        fracStr = hex(int(fracBinary, 2) + 1)[2:]
        fracStrLength = len(fracStr)
        if fracStrLength < 4:
            fracStr = '0' * (4 - fracStrLength) + fracStr
            ret += fracStr
        elif fracStrLength == 4:
            ret += fracStr
        elif fracStrLength == 5:
            ret = hex(int(ret, 16) + 1)[2:]
            ret += fracStr[1:]
        else:
            return ret

    return ret

def hexToInt(hex):
    ret = 0
    hexToIntDict = {}
    digit = ord('0')
    c = ord('a')
    for i in range(16):
        if i < 10:
            hexToIntDict[chr(digit)] = np.int32(i)
            digit += 1
        else:
            hexToIntDict[chr(c)] = np.int32(i)
            c += 1

    if hex[0] == '0':
        for i in range(8):
            ret += hexToIntDict[hex[i]] * (2 ** (28 - 4 * i))
    elif hex[0] == 'f':
        ret += -2 ** 28
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (28 - 4 * i))
    else:
        return ret

    return ret

def fpToInt(fp):
    return hexToInt(fpToHex(fp))

if __name__ == '__main__':
    conf_8_int = fpToInt(conf_8_0)
    conf_9_int = fpToInt(conf_9_0)
    conf_10_int = fpToInt(conf_10_0)
    conf_11_int = fpToInt(conf_11_0)
    conf_12_int = fpToInt(conf_12_0)
    conf_13_int = fpToInt(conf_13_0)
    conf_14_int = fpToInt(conf_14_0)
    conf_15_int = fpToInt(conf_15_0)
    conf_16_int = fpToInt(conf_16_0)
    conf_17_int = fpToInt(conf_17_0)
    conf_18_int = fpToInt(conf_18_0)
    conf_19_int = fpToInt(conf_19_0)
    conf_20_int = fpToInt(conf_20_0)
    conf_21_int = fpToInt(conf_21_0)
    conf_22_int = fpToInt(conf_22_0)
    conf_23_int = fpToInt(conf_23_0)
    conf_24_int = fpToInt(conf_24_0)
    conf_25_int = fpToInt(conf_25_0)

    print("const int32_t conf_8 = " + str(conf_8_int) + ";\t// 08: cfg_cos_alpha;")
    print("const int32_t conf_9 = " + str(conf_9_int) + ";\t// 09: cfg_sin_alpha;")
    print("const int32_t conf_10 = " + str(conf_10_int) + ";\t// 10: cfg_cos_beta;")
    print("const int32_t conf_11 = " + str(conf_11_int) + ";\t// 11: cfg_sin_beta;")
    print("const int32_t conf_12 = " + str(conf_12_int) + ";\t// 12: cfg_cos_gamma;")
    print("const int32_t conf_13 = " + str(conf_13_int) + ";\t// 13: cfg_sin_gamma;")
    print("const int32_t conf_14 = " + str(conf_14_int) + ";\t// 14: cfg_cos_2_alpha;")
    print("const int32_t conf_15 = " + str(conf_15_int) + ";\t// 15: cfg_sin_2_alpha;")
    print("const int32_t conf_16 = " + str(conf_16_int) + ";\t// 16: cfg_cos_2_beta;")
    print("const int32_t conf_17 = " + str(conf_17_int) + ";\t// 17: cfg_sin_2_beta;")
    print("const int32_t conf_18 = " + str(conf_18_int) + ";\t// 18: cfg_cos_2_gamma;")
    print("const int32_t conf_19 = " + str(conf_19_int) + ";\t// 19: cfg_sin_2_gamma;")
    print("const int32_t conf_20 = " + str(conf_20_int) + ";\t// 20: cfg_cos_3_alpha;")
    print("const int32_t conf_21 = " + str(conf_21_int) + ";\t// 21: cfg_sin_3_alpha;")
    print("const int32_t conf_22 = " + str(conf_22_int) + ";\t// 22: cfg_cos_3_beta;")
    print("const int32_t conf_23 = " + str(conf_23_int) + ";\t// 23: cfg_sin_3_beta;")
    print("const int32_t conf_24 = " + str(conf_24_int) + ";\t// 24: cfg_cos_3_gamma;")
    print("const int32_t conf_25 = " + str(conf_25_int) + ";\t// 25: cfg_sin_3_gamma;")

