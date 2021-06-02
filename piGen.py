from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import pandas as pd

bPi = []
rngX = []
rngY = []
rngC = []
midPoints = []
piLow = 3.1415
piHigh = 3.1420



def piCalc(a,b,c,d,e,f):
    insideCircle = []
    outsideCircle = []
    for i in range(a):

        c = np.append(c, rand.uniform(0,b))
        d = np.append(d, rand.uniform(0,b))

        midPoint = sqrt(c[i]**2 + d[i]**2)
        f = np.append(f, midPoint)

        if midPoint < b:

            insideCircle = np.append(insideCircle, midPoint)
            e = np.append(e, 'r')

        else:

            outsideCircle = np.append(outsideCircle, midPoint)
            e = np.append(e, 'c')

    insideCireclePct = (len(insideCircle)/(len(insideCircle)+len(outsideCircle)))
    cPi = (insideCireclePct/(1**2))*4

    if(cPi <= piHigh and cPi >= piLow):
        print("Calculated Pi: " + str(cPi))
        df = pd.DataFrame({'x': c,'y' : d, 'c': e, 'd' : f})
        groups = df.groupby('c')
        for name, group in groups:
            plt.plot(group.x, group.y, marker='o', linestyle='', markersize=12, label=name)

        plt.legend()
        plt.show()    

    return cPi


def trialCounter(a):

    cPi = piCalc(numSamples,rngUpper,rngX,rngY,rngC,midPoints)                 

    if((cPi <= piHigh and cPi >= piLow)):
        print("Exiting...")
    else:
        a = np.append(a, cPi)
        print(len(a))
        trialCounter(a)     

numSamples = int(input("Number of Samples?:"))
rngUpper = int(input("Random Upper Bound?:"))

trialCounter(bPi)