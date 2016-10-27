from memfuncs import MemFunc
import json
import matplotlib.pyplot as plt
import numpy as np



labels = ["Car_ID","Risk",'Value_Loss','Horsepower','City_MPG','Highway_MPG','Price']


def boxPlotForData():
    data = np.genfromtxt("car_data.csv",delimiter=',')
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 5))
    colors = ["lightblue","lightgreen","pink","lightgoldenrodyellow", 'lightskyblue','lightsalmon']
    for i in range(6):
        row, col = np.unravel_index(i,(3,2))

        bplot = axes[row][col].boxplot(data[:,i+1],vert=True, notch=True,patch_artist=True)
        bplot['boxes'][0].set_facecolor(colors[i])

        axes[row][col].set_title(labels[i])

    plt.show()


def histForData():
    data = np.genfromtxt("car_data.csv",delimiter=',')
    #plt.hist(data[:,1], facecolor='green')

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 5))


    for i in range(6):
        row, col = np.unravel_index(i,(3,2))
        axes[row][col].hist(data[:,i+1], facecolor='green')
        axes[row][col].set_title(labels[i])


    plt.show()





def plotMemberFuncs():

    with open("jsonTrees/memFuncs1.json") as data_file:
    	data = json.load(data_file)


    memFuncs = []
    for func in data:
    	memFuncs.append(MemFunc(func["memFunc"],func["memFuncSpecs"]))

    colors = ["r","g","b"]

    xaxis = [100000,0]

    for func,color in zip(memFuncs,colors):
        xLow = func.specs[0] - 1
        xHigh = func.specs[-1] + 1

        if xLow < xaxis[0]:
            xaxis[0] = xLow
        if xHigh > xaxis[1]:
            xaxis[1] = xHigh


        x = np.arange(xLow,xHigh,.01)

        y = []
        for i in x:
            y.append(func.memFunc(i));

        plt.plot(x,y,color)
        #plt.axis([xLow, xHigh, -1,2])

    plt.axis([xaxis[0],xaxis[1],-1,2])
    plt.show()


if __name__ == '__main__':
    #histForData()
    #boxPlotForData()
    plotMemberFuncs()

