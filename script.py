#import matplotlib.pyplot as plt
import math

k = [0.25, 0.025, 0.0025, 0.00025]
peoples = 5500.0
rn = 4.0
n = 1

def rn_1(rn):
    return (rn + k*rn*(peoples-rn))

while(1):
    if math.floor(rn) != math.ceil(rn_1(rn)):
        n += 1
    else:
        break
    rn = rn_1(rn)
    print('numero d dias',math.ceil(rn))

print('numero de dias', n)