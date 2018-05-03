#import matplotlib.pyplot as plt
import math

k = [0.25, 0.025, 0.0025, 0.00025, 0.000012]
peoples = 5500.0
rn = 4

def rn_1(rn,k):
    return (rn + k*rn*(peoples-rn))


def rumors(k,rn):
    print("k = ",k, " rn = ", rn)
    n = 1    
    while(1):
        if rn_1(rn,k) -rn > 1:
            n += 1
        else:
            break
        rn = rn_1(rn,k)
        print(n,' - numero d pessoas',math.ceil(rn))
    
    print('numero de dias', n)
   
for i in k:
    rumors(i,rn)