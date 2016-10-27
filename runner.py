from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt


#Just easier to see the parts of the data
Car_ID = 0
Risk = 1
Value_Loss = 2
Horsepower = 3
City_MPG = 4
Highway_MPG = 5
Price = 6



testName = "ZadehBaseTree"
wValue = "wrong-data-convertion"


def convertCarData(data):
    return [data[Highway_MPG],data[Horsepower],data[City_MPG],data[Price],data[Risk],data[Value_Loss]]

def convertCarData2(data):
    return [data[City_MPG],data[Highway_MPG],data[Price],data[Value_Loss],data[Horsepower],data[Risk]]

def printInputs():
    dTree = DecisionTree('jsonTrees/' + testName + '.json')
    dTree.printInputs()

def main():
    car_data = np.genfromtxt('car_data.csv', delimiter=',')


    dTree = DecisionTree('jsonTrees/' + testName + '.json')
    scores = []
    best = [0,0]

    for data in car_data:
        dTree.changeInputs(convertCarData2(data))
        score = dTree.run()
        if(score > best[0]):
        	best[0] = score
        	best[1] = data
        scores.append(score)
        print(score)


    print("best",best[0],best[1])
    n, bins, patches = plt.hist(scores, normed=1, facecolor='green', alpha=0.75)
    plt.title(testName+wValue)
    plt.savefig("graphs/" + testName + wValue + ".png", bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()


