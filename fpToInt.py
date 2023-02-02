# This is the script to convert from floating point nubmers to 32-bit integers
# The number of fractional bits is 21

# from intToFxp_16 import *

def fpToBi(fp, fracBit):
    ret = ""

    if fp < 0:
        fp += 2 ** (32 - fracBit)
    
    fractional = fp % 1
    integral = fp - fractional

    while (integral):
        if integral % 2:
            ret = "1" + ret
        else:
            ret = "0" + ret
        integral //= 2

    length = len(ret)
    if length < (32 - fracBit):
        ret = '0' * ((32 - fracBit) - length) + ret
    
    fracBinary = ""
    fracTemp = fractional
    for i in range(fracBit):
        fracTemp *= 2
        if fracTemp >= 1:
            fracBinary += '1'
            fracTemp -= 1
        else:
            fracBinary += '0'
    
    ret += fracBinary
    return ret

if __name__ == '__main__':
    print(int(fpToBi(0.0, 21), 2))
    print(int(fpToBi(0.5, 21), 2))
    print(int(fpToBi(1.0, 21), 2))
    print(int(fpToBi(2.0, 21), 2))
