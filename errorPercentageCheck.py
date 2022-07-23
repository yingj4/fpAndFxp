# This is the file to check the error percentage
from ro_4 import *
from intToFxp import *
from fpToInt import *
from ro_accOut import *

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

def outputCheck(accOut):
    # error percentage checking for the output array
    error_out = []
    for i in range(0, len(accOut)):
        fxp = intToFxp(accOut[i])
    if fxp != baseline[i]:
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

if __name__ == '__main__':
    # inputCheck()
    outputCheck(accOut_0)
    outputCheck(accOut_1)
    outputCheck(accOut_2)
    outputCheck(accOut_3)
