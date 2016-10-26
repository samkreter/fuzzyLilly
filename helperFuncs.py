from memfuncs import MemFunc
import json
import matplotlib.pyplot as plt
import numpy as np


# Car ID
#  Risk
#  Value Loss
#  Horsepower
#  City MPG
#  Highway MPG
#  Price



def boxPlotForData():
    data = np.genfromtxt("car_data.csv",delimiter=',')
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 5))
    colors = ["lightblue","lightgreen","pink","lightgoldenrodyellow", 'lightskyblue','lightsalmon']
    for i in range(6):
        row, col = np.unravel_index(i,(3,2))

        bplot = axes[row][col].boxplot(data[:,i+1],vert=True, notch=True,patch_artist=True)
        bplot['boxes'][0].set_facecolor(colors[i])

    plt.show()


def histForData():
    data = np.genfromtxt("car_data.csv",delimiter=',')
    #plt.hist(data[:,1], facecolor='green')

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 5))


    for i in range(6):
        row, col = np.unravel_index(i,(3,2))
        axes[row][col].hist(data[:,i+1], facecolor='green')



    plt.show()





def plotMemberFuncs():

    with open("memFuncs1.json") as data_file:
    	data = json.load(data_file)


    memFuncs = []
    for func in data:
    	memFuncs.append(MemFunc(func["memFunc"],func["memFuncSpecs"]))

    for func in memFuncs:
        xLow = func.specs[0] - 1
        xHigh = func.specs[-1] + 1

        x = np.arange(xLow,xHigh,.01)
        #vfunc = np.vectorize(func.memFunc)

        y = []
        for i in x:
            y.append(func.memFunc(i));

        plt.plot(x,y)
        plt.axis([xLow, xHigh, -1,2])
        plt.show()


if __name__ == '__main__':
    histForData()
    boxPlotForData()


