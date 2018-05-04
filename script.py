import matplotlib.pyplot as plt
import numpy as np

k = [0.25, 0.025, 0.0025, 0.00025, 0.000012]
people = 5500.0 #number of people in company
rn = 4          # number of people who heard rumor
rns = []

def rn_1(rn,k):
    return (rn + k*rn*(people-rn))

def plot(rns):
    x = np.arange(len((rns)))
    plt.plot(x, rns)
    plt.show()


def rumors(k,rn):
    print("k = ",k, " rn = ", rn)
    days = 1    
    while(1):
        if rn_1(rn,k) -rn > 1:
            days += 1
        else:
            break
        rn = rn_1(rn,k)
        rns.append(rn)
        print('day: ', days,' number of people: ',(rn))
    plot(rns)
    print('number of days', days)
   
for i in k:
    rumors(i,rn)