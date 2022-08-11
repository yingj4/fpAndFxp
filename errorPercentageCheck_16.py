# This is the file to check the error percentage
# The number of fractional bits is 16
from ro_4 import *
from intToFxp_16 import *
from fpToInt_16 import *
from ro_accOut_16 import *
from ro_4 import *

def inputCheck():
    # error percentage checking for the configurations input
    error_conf = []
    conf_8_fxp = intToFxp(fpToInt(conf_8_0))
    conf_9_fxp = intToFxp(fpToInt(conf_9_0))
    conf_10_fxp = intToFxp(fpToInt(conf_10_0))
    conf_11_fxp = intToFxp(fpToInt(conf_11_0))
    conf_12_fxp = intToFxp(fpToInt(conf_12_0))
    conf_13_fxp = intToFxp(fpToInt(conf_13_0))
    conf_14_fxp = intToFxp(fpToInt(conf_14_0))
    conf_15_fxp = intToFxp(fpToInt(conf_15_0))
    conf_16_fxp = intToFxp(fpToInt(conf_16_0))
    conf_17_fxp = intToFxp(fpToInt(conf_17_0))
    conf_18_fxp = intToFxp(fpToInt(conf_18_0))
    conf_19_fxp = intToFxp(fpToInt(conf_19_0))
    conf_20_fxp = intToFxp(fpToInt(conf_20_0))
    conf_21_fxp = intToFxp(fpToInt(conf_21_0))
    conf_22_fxp = intToFxp(fpToInt(conf_22_0))
    conf_23_fxp = intToFxp(fpToInt(conf_23_0))
    conf_24_fxp = intToFxp(fpToInt(conf_24_0))
    conf_25_fxp = intToFxp(fpToInt(conf_25_0))

    if conf_8_fxp != conf_8_0:
        error_conf.append((conf_8_fxp - conf_8_0) / conf_8_0)
    else:
        error_conf.append(0.0)
    if conf_9_fxp != conf_9_0:
        error_conf.append((conf_9_fxp - conf_9_0) / conf_9_0)
    else:
        error_conf.append(0.0)
    if conf_10_fxp != conf_10_0:
        error_conf.append((conf_10_fxp - conf_10_0) / conf_10_0)
    else:
        error_conf.append(0.0)
    if conf_11_fxp != conf_11_0:
        error_conf.append((conf_11_fxp - conf_11_0) / conf_11_0)
    else:
        error_conf.append(0.0)
    if conf_12_fxp != conf_12_0:
        error_conf.append((conf_12_fxp - conf_12_0) / conf_12_0)
    else:
        error_conf.append(0.0)
    if conf_13_fxp != conf_13_0:
        error_conf.append((conf_13_fxp - conf_13_0) / conf_13_0)
    else:
        error_conf.append(0.0)
    if conf_14_fxp != conf_14_0:
        error_conf.append((conf_14_fxp - conf_14_0) / conf_14_0)
    else:
        error_conf.append(0.0)
    if conf_15_fxp != conf_15_0:
        error_conf.append((conf_15_fxp - conf_15_0) / conf_15_0)
    else:
        error_conf.append(0.0)
    if conf_16_fxp != conf_16_0:
        error_conf.append((conf_16_fxp - conf_16_0) / conf_16_0)
    else:
        error_conf.append(0.0)
    if conf_17_fxp != conf_17_0:
        error_conf.append((conf_17_fxp - conf_17_0) / conf_17_0)
    else:
        error_conf.append(0.0)
    if conf_18_fxp != conf_18_0:
        error_conf.append((conf_18_fxp - conf_18_0) / conf_18_0)
    else:
        error_conf.append(0.0)
    if conf_19_fxp != conf_19_0:
        error_conf.append((conf_19_fxp - conf_19_0) / conf_19_0)
    else:
        error_conf.append(0.0)
    if conf_20_fxp != conf_20_0:
        error_conf.append((conf_20_fxp - conf_20_0) / conf_20_0)
    else:
        error_conf.append(0.0)
    if conf_21_fxp != conf_21_0:
        error_conf.append((conf_21_fxp - conf_21_0) / conf_21_0)
    else:
        error_conf.append(0.0)
    if conf_22_fxp != conf_22_0:
        error_conf.append((conf_22_fxp - conf_22_0) / conf_22_0)
    else:
        error_conf.append(0.0)
    if conf_23_fxp != conf_23_0:
        error_conf.append((conf_23_fxp - conf_23_0) / conf_23_0)
    else:
        error_conf.append(0.0)
    if conf_24_fxp != conf_24_0:
        error_conf.append((conf_24_fxp - conf_24_0) / conf_24_0)
    else:
        error_conf.append(0.0)
    if conf_25_fxp != conf_25_0:
        error_conf.append((conf_25_fxp - conf_25_0) / conf_25_0)
    else:
        error_conf.append(0.0)

    error_conf_abs = []
    for i in range(len(error_conf)):
        error_conf_abs.append(abs(error_conf[i]))

    print("Configurations")
    print("avg error_conf_abs: " + str(sum(error_conf_abs) / len(error_conf_abs)))
    print("max error_conf_abs: " + str(max(error_conf_abs)))
    print("min error_conf: " + str(min(error_conf)))
    print("max error_conf: " + str(max(error_conf)))

    # error percentage checking for the input array
    error_in = []
    for i in range(len(originalChannel_in_0)):
        fxp = intToFxp(fpToInt(originalChannel_in_0[i]))
        if fxp != originalChannel_in_0[i]:
            error_in.append((fxp - originalChannel_in_0[i]) / originalChannel_in_0[i])
        else:
            error_in.append(0.0)

    error_in_abs = []
    for i in range(len(error_in)):
        error_in_abs.append(abs(error_in[i]))

    print("Input array")
    print("avg error_in_abs: " + str(sum(error_in_abs) / len(error_in_abs)))
    print("max error_in_abs: " + str(max(error_in_abs)))
    print("min error_in: " + str(min(error_in)))
    print("max error_in: " + str(max(error_in)))

def outputCheck(baseline, accOut, type):
    # error percentage checking for the output array
    error_out = []

    if type == "all":
        print("The error percentage for all values")
    elif type == "smallFilter":
        print("The error percentage after filtering out small numbers")

    for i in range(0, len(accOut)):
        fxp = intToFxp(accOut[i])
        if type == "all":
            if fxp != baseline[i] and baseline[i] == 0:
                if fxp > 0:
                    error_out.append(9999.99)   # Infinity
                else:
                    error_out.append(-9999.99)  # Negative infinity
            elif fxp != baseline[i] and baseline[i] != 0:
                error_out.append((fxp - baseline[i]) / baseline[i])
            else:
                error_out.append(0.0)
        elif type == "smallFilter":
            if baseline[i] == 0 or baseline[i] == 1e-6 or baseline[i] == -1e-6:
                continue

            if fxp != baseline[i] and baseline[i] != 0:
                error_out.append((fxp - baseline[i]) / baseline[i])
            else:
                error_out.append(0.0)

    error_out_abs = []
    for i in range(len(error_out)):
        error_out_abs.append(abs(error_out[i]))

    print("Output array")
    if accOut is accOut_0:
        print("Block 0")
    elif accOut is accOut_1:
        print("Block 1")
    elif accOut is accOut_2:
        print("Block 2")
    elif accOut is accOut_3:
        print("Block 3")
    print("avg error_out_abs: " + str(sum(error_out_abs) / len(error_out_abs)))
    print("max error_out_abs: " + str(max(error_out_abs)))
    print("min error_out: " + str(min(error_out)))
    print("max error_out: " + str(max(error_out)))
    print(baseline[error_out.index(min(error_out))])
    print(baseline[error_out.index(max(error_out))])

if __name__ == '__main__':
    # inputCheck()

    '''
    Check the error percentage for all the output values
    '''
    outputCheck(baseline_0, accOut_0, "all")
    outputCheck(baseline_1, accOut_1, "all")
    outputCheck(baseline_2, accOut_2, "all")
    outputCheck(baseline_3, accOut_3, "all")

    '''
    Check the error percentage after filtering out 0, 1e-6, and -1e-6
    '''
    outputCheck(baseline_0, accOut_0, "smallFilter")
    outputCheck(baseline_1, accOut_1, "smallFilter")
    outputCheck(baseline_2, accOut_2, "smallFilter")
    outputCheck(baseline_3, accOut_3, "smallFilter")

    print("Input/Output Range")
    print("Input")
    print(min(min(originalChannel_in_0), min(originalChannel_in_1), min(originalChannel_in_2), min(originalChannel_in_3)))
    print(max(max(originalChannel_in_0), max(originalChannel_in_1), max(originalChannel_in_2), max(originalChannel_in_3)))
    print("Output")
    print(min(min(originalChannel_out_0), min(originalChannel_out_1), min(originalChannel_out_2), min(originalChannel_out_3)))
    print(max(max(originalChannel_out_0), max(originalChannel_out_1), max(originalChannel_out_2), max(originalChannel_out_3)))
