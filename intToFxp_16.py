# This is the script to convert from 32-bit integers to fixed point numbers
# The number of fractional bits is 16
import numpy as np

def intToHex(integer):
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

    if integer >= 0:
        while integer:
            ret = m[integer % 16] + ret
            integer //= 16
        length = len(ret)
        if length < 8:
            ret = '0' * (8 - length) + ret
    else:
        n = integer + 2 ** 32

        while n:
            ret = m[n % 16] + ret
            n //= 16

    return ret

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

    if hex[0] == '0':
        for i in range(8):
            ret += hexToIntDict[hex[i]] * (2 ** (12 - 4 * i))
    elif hex[0] == 'f':
        ret += -1.0 * (2 ** 12)
        for i in range(1, 8):
            ret += hexToIntDict[hex[i]] * (2 ** (12 - 4 * i))
    else:
        return ret

    return ret

def intToFxp(integer):
    return hexToFxp(intToHex(integer))

def compute(audio_in):
    conf_8_int = np.int32(39413)  # 08: cfg_cos_alpha
    conf_9_int = np.int32(60968)  # 09: cfg_sin_alpha
    conf_10_int = np.int32(-46013)  # 10: cfg_cos_beta
    conf_11_int = np.int32(-56152)  # 11: cfg_sin_beta
    conf_12_int = np.int32(-35750)  # 12: cfg_cos_gamma
    conf_13_int = np.int32(-22125)  # 13: cfg_sin_gamma
    conf_14_int = np.int32(-39414)  # 14: cfg_cos_2_alpha
    conf_15_int = np.int32(57035)  # 15: cfg_sin_2_alpha
    conf_16_int = np.int32(-15211)  # 16: cfg_cos_2_beta
    conf_17_int = np.int32(10276)  # 17: cfg_sin_2_beta
    conf_18_int = np.int32(27688)  # 18: cfg_cos_2_gamma
    conf_19_int = np.int32(-48707)  # 19: cfg_sin_2_gamma
    conf_20_int = np.int32(-42691)  # 20: cfg_cos_3_alpha
    conf_21_int = np.int32(-11292)  # 21: cfg_sin_3_alpha
    conf_22_int = np.int32(48018)  # 22: cfg_cos_3_beta
    conf_23_int = np.int32(23121)  # 23: cfg_sin_3_beta
    conf_24_int = np.int32(-53190)  # 24: cfg_cos_3_gamma
    conf_25_int = np.int32(22878)  # 25: cfg_sin_3_gamma

    conf_8 = intToFxp(conf_8_int)
    conf_9 = intToFxp(conf_9_int)
    conf_10 = intToFxp(conf_10_int)
    conf_11 = intToFxp(conf_11_int)
    conf_12 = intToFxp(conf_12_int)
    conf_13 = intToFxp(conf_13_int)
    conf_14 = intToFxp(conf_14_int)
    conf_15 = intToFxp(conf_15_int)
    conf_16 = intToFxp(conf_16_int)
    conf_17 = intToFxp(conf_17_int)
    conf_18 = intToFxp(conf_18_int)
    conf_19 = intToFxp(conf_19_int)
    conf_20 = intToFxp(conf_20_int)
    conf_21 = intToFxp(conf_21_int)
    conf_22 = intToFxp(conf_22_int)
    conf_23 = intToFxp(conf_23_int)
    conf_24 = intToFxp(conf_24_int)
    conf_25 = intToFxp(conf_25_int)

    print("float conf_8_f = " + str(conf_8) + ";")
    print("float conf_9_f = " + str(conf_9) + ";")
    print("float conf_10_f = " + str(conf_10) + ";")
    print("float conf_11_f = " + str(conf_11) + ";")
    print("float conf_12_f = " + str(conf_12) + ";")
    print("float conf_13_f = " + str(conf_13) + ";")
    print("float conf_14_f = " + str(conf_14) + ";")
    print("float conf_15_f = " + str(conf_15) + ";")
    print("float conf_16_f = " + str(conf_16) + ";")
    print("float conf_17_f = " + str(conf_17) + ";")
    print("float conf_18_f = " + str(conf_18) + ";")
    print("float conf_19_f = " + str(conf_19) + ";")
    print("float conf_20_f = " + str(conf_20) + ";")
    print("float conf_21_f = " + str(conf_21) + ";")
    print("float conf_22_f = " + str(conf_22) + ";")
    print("float conf_23_f = " + str(conf_23) + ";")
    print("float conf_24_f = " + str(conf_24) + ";")
    print("float conf_25_f = " + str(conf_25) + ";")

    sinBetaSq = conf_11 * conf_11
    sinBetaCb = conf_11 * conf_11 * conf_11
    fSqrt3 = 1.7320508
    fSqrt3_2 = 1.2247448
    fSqrt15 = 3.8729833
    fSqrt5_2 = 1.5811388
    fxp025 = 0.25
    fxp050 = 0.5
    fxp075 = 0.75
    fxp00625 = 0.0625
    fxp0125 = 0.125

    output = [0.0] * 128

    '''
    enum ChannelNames
    {
        kW,
        kY, kZ, kX,
        kV, kT, kR, kS, kU,
        kQ, kO, kM, kK, kL, kN, kP
    };
    '''

    for i in range(0, 128, 16):
        # Rotate Order 1
        # kY = 1, kZ = 2, kX = 3
        valueY = -audio_in[i + 3] * conf_9 + audio_in[i + 1] * conf_8
        valueZ = audio_in[i + 2]
        valueX = audio_in[i + 3] * conf_8 + audio_in[i + 1] * conf_9

        vY = valueY
        vZ = valueX * conf_11 + valueZ * conf_10
        vX = valueX * conf_10 + valueZ * conf_11

        output[i + 1] = -vX * conf_13 + vY * conf_12
        output[i + 2] = vZ
        output[i + 3] = vX * conf_12 + vY * conf_13

        # Rotate Order 2
        # kV = 4, kT = 5, kR = 6, kS = 7, kU = 8
        valueV = -audio_in[i + 8] * conf_15 + audio_in[i + 4] * conf_14
        valueT = -audio_in[i + 7] * conf_9 + audio_in[i + 5] * conf_8
        valueR = audio_in[i + 6]
        valueS = audio_in[i + 7] * conf_8 + audio_in[i + 5] * conf_9
        valueU = audio_in[i + 8] * conf_14 + audio_in[i + 4] * conf_15

        vV = -conf_11 * valueT + conf_10 * valueV
        vT = -conf_10 * valueT + conf_11 * valueV
        vR = (fxp075 * conf_16 + fxp025) * valueR + (fxp050 * fSqrt3 * sinBetaSq) * valueU + (
                    fSqrt3 * conf_11 * conf_10) * valueS
        vS = conf_16 * valueS - fSqrt3 * conf_10 * conf_11 * valueR + conf_10 * conf_11 * valueU
        vU = (fxp025 * conf_16 + fxp075) * valueU - conf_10 * conf_11 * valueS + fxp050 * fSqrt3 * sinBetaSq * valueR

        output[i + 4] = -vU * conf_19 + vV * conf_18
        output[i + 5] = -vS * conf_13 + vT * conf_12
        output[i + 6] = vR
        output[i + 7] = vS * conf_12 + vT * conf_13
        output[i + 8] = vU * conf_18 + vV * conf_19

        # Rotate Order 3
        # kQ = 9, kO = 10, kM = 11, kK = 12, kL = 13, kN = 14, kP = 15
        valueQ = -audio_in[i + 15] * conf_21 + audio_in[i + 9] * conf_20
        valueO = -audio_in[i + 14] * conf_15 + audio_in[i + 10] * conf_14
        valueM = -audio_in[i + 13] * conf_9 + audio_in[i + 11] * conf_8
        valueK = audio_in[i + 12]
        valueL = audio_in[i + 13] * conf_8 + audio_in[i + 11] * conf_9
        valueN = audio_in[i + 14] * conf_14 + audio_in[i + 10] * conf_15
        valueP = audio_in[i + 15] * conf_20 + audio_in[i + 9] * conf_21

        vQ = fxp0125 * valueQ * (
                    5 + 3 * conf_16) - fSqrt3_2 * valueO * conf_10 * conf_11 + fxp025 * fSqrt15 * valueM * sinBetaSq
        vO = valueO * conf_16 - fSqrt5_2 * valueM * conf_10 * conf_11 + fSqrt3_2 * valueQ * conf_10 * conf_11
        vM = fxp0125 * valueM * (
                    3 + 5 * conf_16) - fSqrt5_2 * valueO * conf_10 * conf_11 + fxp025 * fSqrt15 * valueQ * sinBetaSq
        vK = fxp025 * valueK * conf_10 * (
                    -1 + 15 * conf_16) + fxp050 * fSqrt15 * valueN * conf_10 * sinBetaSq + fxp050 * fSqrt5_2 * valueP * sinBetaCb + fxp0125 * fSqrt3_2 * valueL * (
                         conf_11 + 5 * conf_23)
        vL = fxp00625 * valueL * (conf_10 + 15 * conf_22) + fxp025 * fSqrt5_2 * valueN * (
                    1 + 3 * conf_16) * conf_11 + fxp025 * fSqrt15 * valueP * conf_10 * sinBetaSq - fxp0125 * fSqrt3_2 * valueK * (
                         conf_11 + 5 * conf_23)
        vN = fxp0125 * valueN * (5 * conf_10 + 3 * conf_22) + fxp025 * fSqrt3_2 * valueP * (
                    3 + conf_16) * conf_11 + fxp050 * fSqrt15 * valueK * conf_10 * sinBetaSq + fxp0125 * fSqrt5_2 * valueL * (
                         conf_11 - 3 * conf_23)
        vP = fxp00625 * valueP * (15 * conf_10 + conf_22) - fxp025 * fSqrt3_2 * valueN * (
                    3 + conf_16) * conf_11 + fxp025 * fSqrt15 * valueL * conf_10 * sinBetaSq - fxp050 * fSqrt5_2 * valueK * sinBetaCb

        output[i + 9] = -vP * conf_25 + vQ * conf_24
        output[i + 10] = -vN * conf_19 + vO * conf_18
        output[i + 11] = -vL * conf_13 + vM * conf_12
        output[i + 12] = vK
        output[i + 13] = vL * conf_12 + vM * conf_13
        output[i + 14] = vN * conf_18 + vO * conf_19
        output[i + 15] = vP * conf_24 + vQ * conf_25

    return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputInt = np.array([0, 46956, 20486, -7767, 8080, -15972, 48876, -61539, 17530, 6186, 55830, 1599, -17846, -46806, -22604, -48556, \
	0, 14640, -6849, 39524, -39538, 49604, -62424, 30140, 39773, 57357, 30140, -20913, 1893, 5786, 6343, -39217, \
	0, 31444, 59546, -24019, -39073, 52264, 10492, -53281, 4469, -21024, -14012, -17243, -37146, 19890, 14424, -2648, \
	0, 39511, 45462, 1795, -55876, 31378, 2549, -48556, 31496, -8206, 12537, -6489, -35705, -32139, -1967, 4338, \
	0, -8546, 52, 18920, -23613, -62404, 4194, -41072, 14693, 16495, 11429, -10211, -25297, -55149, -14956, 51098, \
	0, 42283, -45751, -5604, 44479, 5767, -45574, 21889, -8278, -39728, 2824, 58903, -17204, 1644, -25900, -16666, \
	0, 35730, -60104, 14955, -60195, -9982, 45278, -25055, -52849, 63714, 144, -28004, 20289, 57271, -8363, -2471, \
	0, -603, -17682, 63740, -17636, 62023, 17897, 29314, 17137, 43312, -2255, 23802, 5426, 9083, 20270, 2097], dtype = np.int32)

    outputInt = np.array([0, -34519, -47810, 12544, 67691, -41491, -52565, 5253, -15552, -39352, -23718, -20251, -95005, 14864, 33952, -12760, \
    0, 8373, -27227, 20559, -84367, -675, 25144, -11761, -56951, 10040, -12294, 116, -30892, 15657, 2782, -19321, \
    0, -43239, -54495, 19574, 2178, -34299, -5258, 6577, -53470, 20580, 44490, -2974, -11615, -3359, -12250, 24679, \
    0, -34170, -64338, 28282, -12197, -36253, -42777, 10233, -56617, -22730, 24930, -12662, -42978, 1135, 32743, 5401, \
    0, 11577, -2974, 9014, 23693, -559, -104591, 1797, 13873, -37102, 28600, -4373, -26764, 3208, 61310, -26930, \
    0, -12007, 1306, -17954, -7669, 20787, 43619, -39543, -3618, -5218, -23187, 6950, -32588, -16500, 6610, 35079, \
    0, 3242, 6013, -14474, 3569, 13586, -35038, 49086, 44199, 57690, 1437, 31054, 16639, 14147, -32750, -39608, \
    0, 28706, -19949, 26343, -33510, -23263, 63536, 24505, -30473, 4608, -14731, 9331, 26619, -11471, 13574, 13357], dtype=np.int32)

    length = len(inputInt)
    audio_in = [0.0] * length
    audio_out = [0.0] * length
    for i in range(length):
        audio_in[i] = intToFxp(inputInt[i])
        audio_out[i] = intToFxp(outputInt[i])

    # print(audio_in)
    # print(audio_out)
    output = compute(audio_in)
    # print(output)

    print("float audio_in[128] = {")
    for i in range(0, 128, 16):
        print(str(audio_in[i]) + ", " + str(audio_in[i + 1]) + ", " + str(audio_in[i + 2]) + ", " + str(audio_in[i + 3]) + ", " + \
              str(audio_in[i + 4]) + ", " + str(audio_in[i + 5]) + ", " + str(audio_in[i + 6]) + ", " + str(audio_in[i + 7]) + ", " + \
              str(audio_in[i + 8]) + ", " + str(audio_in[i + 9]) + ", " + str(audio_in[i + 10]) + ", " + str(audio_in[i + 11]) + ", " + \
              str(audio_in[i + 12]) + ", " + str(audio_in[i + 13]) + ", " + str(audio_in[i + 14]) + ", " + str(audio_in[i + 15]) + ", ")
    print("};")

    print("float audio_out[128] = {")
    for i in range(0, 128, 16):
        print(str(audio_out[i]) + ", " + str(audio_out[i + 1]) + ", " + str(audio_out[i + 2]) + ", " + str(audio_out[i + 3]) + ", " + \
              str(audio_out[i + 4]) + ", " + str(audio_out[i + 5]) + ", " + str(audio_out[i + 6]) + ", " + str(audio_out[i + 7]) + ", " + \
              str(audio_out[i + 8]) + ", " + str(audio_out[i + 9]) + ", " + str(audio_out[i + 10]) + ", " + str(audio_out[i + 11]) + ", " + \
              str(audio_out[i + 12]) + ", " + str(audio_out[i + 13]) + ", " + str(audio_out[i + 14]) + ", " + str(audio_out[i + 15]) + ", ")
    print("};")

    error = 0
    for i in range(length):
        if output[i] - audio_out[i] > 1e-4 or output[i] - audio_out[i] < -1e-4:
            error += 1

    print(error)
