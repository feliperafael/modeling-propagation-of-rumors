import matplotlib.pyplot as plt
import numpy as np

k = [0.025, 0.0025, 0.000025, 0.0012]
people = 1500 #number of people in company

def delta(rn,k):
    return  k*rn*(people-rn)

def plot(rns):
    x = np.arange(len((rns)))
    plt.plot(x, rns)
    plt.show()


def rumors(k):
    rns = []
    rn = 4          # number of people who heard rumor
    print("k = ",k, " rn = ", rn)
    days = 0  
    delta_value = 0    
    
    while(1):
        delta_value = delta(rn,k)
        print('delta : ',delta_value)
        if delta_value > 0.1:
            days += 1
        else:
            break
        rn += delta(rn,k)
        rns.append(rn)
        print('day: ', days,' number of people: ',(rn))
    plot(rns)
    print('number of days', days)

    
for i in k:
    rumors(i)