from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt
from memfuncs import MemFunc

Car_ID = 0
Risk = 1
Value_Loss = 2
Horsepower = 3
City_MPG = 4
Highway_MPG = 5
Price = 6


#Used to name files for printing out the graphs
testF = "alpha"
testN = "ZadehBaseTree"
wValue = "-w2"


#convert the data to the correct order for the base tree
def convertCarData(data):
    return [data[Highway_MPG],data[Horsepower],data[City_MPG],data[Price],data[Risk],data[Value_Loss]]


#conver the data to the correct oder for the newly generated tree
def convertCarData2(data):
    return [data[City_MPG],data[Highway_MPG],data[Price],data[Value_Loss],data[Horsepower],data[Risk]]

#prints the order of the inputs stored in the tree
def printInputs():
    dTree = DecisionTree('jsonTrees/' + testName + '.json')
    dTree.printInputs()


def main():
    #import the data from a csv
    car_data = np.genfromtxt('car_data.csv', delimiter=',')

    #call the tree creator module and pass the name of the json file to it
    fTree = DecisionTree('jsonTrees/' + testF + '.json')
    nTree = DecisionTree('jsonTrees/' + testN + '.json')





    for data in car_data[np.random.randint(car_data.shape[0], size=20), :]:
        inputs = convertCarData(data)
        #change the inputs for each of the cars in the tree
        fTree.changeInputs(inputs)
        nTree.changeInputs(inputs)

        #get the score for that car
        fScore = fTree.run()
        nScore = nTree.run()

        print("Inputs:",inputs)
        print("FSCORE #######:",fScore)
        print("NSCORE #######:",nScore)


        f1 = MemFunc('trap',fScore)
        X = np.arange(0,1,.05)

        plt.plot(X,[f1.memFunc(i) for i in X])
        plt.show()
        t = input()



if __name__ == '__main__':
    main()

