import numpy as np

def fast_modular_exponentiation(n, exp, mod):
    binary = []
    result = 1

    while exp > 0:
        binary.append(exp & 1)
        exp = exp >> 1

    array = np.zeros(len(binary),dtype='int64')
    array[0] = n%mod

    for i in range(len(array)):
        if array[i] == 0:
            array[i] = (array[i-1]*array[i-1])%mod

    for i in range(len(binary)):
        if binary[i] == 1:
            result = result*array[i]

    return result%mod

if fast_modular_exponentiation(234,141,391) == 13:
    print("pass")
if fast_modular_exponentiation(347, 141, 391) == 6:
    print("pass")