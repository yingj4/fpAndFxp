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

def errPercentCheck():
    # error checking for the configurations
    error_conf = []
    conf_8_fxp = intToFxp(fpToInt(conf_8_3))
    conf_9_fxp = intToFxp(fpToInt(conf_9_3))
    conf_10_fxp = intToFxp(fpToInt(conf_10_3))
    conf_11_fxp = intToFxp(fpToInt(conf_11_3))
    conf_12_fxp = intToFxp(fpToInt(conf_12_3))
    conf_13_fxp = intToFxp(fpToInt(conf_13_3))
    conf_14_fxp = intToFxp(fpToInt(conf_14_3))
    conf_15_fxp = intToFxp(fpToInt(conf_15_3))
    conf_16_fxp = intToFxp(fpToInt(conf_16_3))
    conf_17_fxp = intToFxp(fpToInt(conf_17_3))
    conf_18_fxp = intToFxp(fpToInt(conf_18_3))
    conf_19_fxp = intToFxp(fpToInt(conf_19_3))
    conf_20_fxp = intToFxp(fpToInt(conf_20_3))
    conf_21_fxp = intToFxp(fpToInt(conf_21_3))
    conf_22_fxp = intToFxp(fpToInt(conf_22_3))
    conf_23_fxp = intToFxp(fpToInt(conf_23_3))
    conf_24_fxp = intToFxp(fpToInt(conf_24_3))
    conf_25_fxp = intToFxp(fpToInt(conf_25_3))

    if conf_8_fxp != conf_8_3:
        error_conf.append((conf_8_fxp - conf_8_3) / conf_8_3)
    else:
        error_conf.append(0.0)
    if conf_9_fxp != conf_9_3:
        error_conf.append((conf_9_fxp - conf_9_3) / conf_9_3)
    else:
        error_conf.append(0.0)
    if conf_10_fxp != conf_10_3:
        error_conf.append((conf_10_fxp - conf_10_3) / conf_10_3)
    else:
        error_conf.append(0.0)
    if conf_11_fxp != conf_11_3:
        error_conf.append((conf_11_fxp - conf_11_3) / conf_11_3)
    else:
        error_conf.append(0.0)
    if conf_12_fxp != conf_12_3:
        error_conf.append((conf_12_fxp - conf_12_3) / conf_12_3)
    else:
        error_conf.append(0.0)
    if conf_13_fxp != conf_13_3:
        error_conf.append((conf_13_fxp - conf_13_3) / conf_13_3)
    else:
        error_conf.append(0.0)
    if conf_14_fxp != conf_14_3:
        error_conf.append((conf_14_fxp - conf_14_3) / conf_14_3)
    else:
        error_conf.append(0.0)
    if conf_15_fxp != conf_15_3:
        error_conf.append((conf_15_fxp - conf_15_3) / conf_15_3)
    else:
        error_conf.append(0.0)
    if conf_16_fxp != conf_16_3:
        error_conf.append((conf_16_fxp - conf_16_3) / conf_16_3)
    else:
        error_conf.append(0.0)
    if conf_17_fxp != conf_17_3:
        error_conf.append((conf_17_fxp - conf_17_3) / conf_17_3)
    else:
        error_conf.append(0.0)
    if conf_18_fxp != conf_18_3:
        error_conf.append((conf_18_fxp - conf_18_3) / conf_18_3)
    else:
        error_conf.append(0.0)
    if conf_19_fxp != conf_19_3:
        error_conf.append((conf_19_fxp - conf_19_3) / conf_19_3)
    else:
        error_conf.append(0.0)
    if conf_20_fxp != conf_20_3:
        error_conf.append((conf_20_fxp - conf_20_3) / conf_20_3)
    else:
        error_conf.append(0.0)
    if conf_21_fxp != conf_21_3:
        error_conf.append((conf_21_fxp - conf_21_3) / conf_21_3)
    else:
        error_conf.append(0.0)
    if conf_22_fxp != conf_22_3:
        error_conf.append((conf_22_fxp - conf_22_3) / conf_22_3)
    else:
        error_conf.append(0.0)
    if conf_23_fxp != conf_23_3:
        error_conf.append((conf_23_fxp - conf_23_3) / conf_23_3)
    else:
        error_conf.append(0.0)
    if conf_24_fxp != conf_24_3:
        error_conf.append((conf_24_fxp - conf_24_3) / conf_24_3)
    else:
        error_conf.append(0.0)
    if conf_25_fxp != conf_25_3:
        error_conf.append((conf_25_fxp - conf_25_3) / conf_25_3)
    else:
        error_conf.append(0.0)

    error_conf_abs = []
    for i in range(len(error_conf)):
        error_conf_abs.append(abs(error_conf[i]))

    print("avg error_conf_abs: " + str(sum(error_conf_abs) / len(error_conf_abs)))
    print("max error_conf_abs: " + str(max(error_conf_abs)))
    print("min error_conf: " + str(min(error_conf)))
    print("max error_conf: " + str(max(error_conf)))

    error_in = []
    for i in range(len(originalChannel_in_3)):
        fxp = intToFxp(fpToInt(originalChannel_in_3[i]))
        if fxp != originalChannel_in_3[i]:
            error_in.append((fxp - originalChannel_in_3[i]) / originalChannel_in_3[i])
        else:
            error_in.append(0.0)

    error_in_abs = []
    for i in range(len(error_in)):
        error_in_abs.append(abs(error_in[i]))

    print("avg error_in_abs: " + str(sum(error_in_abs) / len(error_in_abs)))
    print("max error_in_abs: " + str(max(error_in_abs)))
    print("min error_in: " + str(min(error_in)))
    print("max error_in: " + str(max(error_in)))

    error_out = []
    for i in range(len(originalChannel_out_3)):
        fxp = intToFxp(fpToInt(originalChannel_out_3[i]))
        if fxp != originalChannel_out_3[i]:
            error_out.append((fxp - originalChannel_out_3[i]) / originalChannel_out_3[i])
        else:
            error_out.append(0.0)

    error_out_abs = []
    for i in range(len(error_out)):
        error_out_abs.append(abs(error_out[i]))

    print("avg error_out_abs: " + str(sum(error_out_abs) / len(error_out_abs)))
    print("max error_out_abs: " + str(max(error_out_abs)))
    print("min error_out: " + str(min(error_out)))
    print("max error_out: " + str(max(error_out)))

if __name__ == '__main__':
    # Error percentage checking
    # errPercentCheck()

    # FP to Int generation
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

    print("int32_t audio_in[128] = {")
    for i in range(0, 128, 16):
        print(str(fpToInt(originalChannel_in_0[i])) + ', ' + str(fpToInt(originalChannel_in_0[i + 1])) + ', ' + str(fpToInt(originalChannel_in_0[i + 2])) + ', ' + str(fpToInt(originalChannel_in_0[i + 3])) + ', ' + \
              str(fpToInt(originalChannel_in_0[i + 4])) + ', ' + str(fpToInt(originalChannel_in_0[i + 5])) + ', ' + str(fpToInt(originalChannel_in_0[i + 6])) + ', ' + str(fpToInt(originalChannel_in_0[i + 7])) + ', ' + \
              str(fpToInt(originalChannel_in_0[i + 8])) + ', ' + str(fpToInt(originalChannel_in_0[i + 9])) + ', ' + str(fpToInt(originalChannel_in_0[i + 10])) + ', ' + str(fpToInt(originalChannel_in_0[i + 11])) + ', ' + \
              str(fpToInt(originalChannel_in_0[i + 12])) + ', ' + str(fpToInt(originalChannel_in_0[i + 13])) + ', ' + str(fpToInt(originalChannel_in_0[i + 14])) + ', ' + str(fpToInt(originalChannel_in_0[i + 15])) + ', ')
    print("};")

    print("int32_t audio_out[128] = {")
    for i in range(0, 128, 16):
        print(str(fpToInt(originalChannel_out_0[i])) + ', ' + str(fpToInt(originalChannel_out_0[i + 1])) + ', ' + str(fpToInt(originalChannel_out_0[i + 2])) + ', ' + str(fpToInt(originalChannel_out_0[i + 3])) + ', ' + \
              str(fpToInt(originalChannel_out_0[i + 4])) + ', ' + str(fpToInt(originalChannel_out_0[i + 5])) + ', ' + str(fpToInt(originalChannel_out_0[i + 6])) + ', ' + str(fpToInt(originalChannel_out_0[i + 7])) + ', ' + \
              str(fpToInt(originalChannel_out_0[i + 8])) + ', ' + str(fpToInt(originalChannel_out_0[i + 9])) + ', ' + str(fpToInt(originalChannel_out_0[i + 10])) + ', ' + str(fpToInt(originalChannel_out_0[i + 11])) + ', ' + \
              str(fpToInt(originalChannel_out_0[i + 12])) + ', ' + str(fpToInt(originalChannel_out_0[i + 13])) + ', ' + str(fpToInt(originalChannel_out_0[i + 14])) + ', ' + str(fpToInt(originalChannel_out_0[i + 15])) + ', ')
    print("};")

