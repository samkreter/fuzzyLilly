from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt
from memfuncs import MemFunc
from file import File



inputs2 = [
[25.0, 82.0, 24.0, 9233.0, 0.0, 102.0],
[33.0, 86.0, 27.0, 7895.0, 0.0, 106.0],
[34.0, 85.0, 27.0, 8495.0, 2.0, 94.0],
[32.0, 94.0, 26.0, 9960.0, 0.0, 102.0],
[28.0, 121.0, 21.0, 21105.0, 0.0, 188.0],
]


#Trash
#[37, 82, 32, 7126, 0, 102],
#[34.0, 76.0, 30.0, 7129.0, 1.0, 101.0],
#[37.0, 69.0, 31.0, 6849.0, 1.0, 122.0],
#[28.0, 114.0, 24.0, 16515.0, -1.0, 74.0],
#[32.0, 84.0, 26.0, 11245.0, 0.0, 115.0],
#[30.0, 88.0, 24.0, 8921.0, -1.0, 74.0],

#.1
# [32.0, 100.0, 26.0, 9995.0, 2.0, 94.0]
# [33.0, 82.0, 28.0, 7775.0, 0.0, 102.0]
# [32.0, 84.0, 26.0, 8495.0, 0.0, 115.0]

#.2
# [32.0, 84.0, 26.0, 11245.0, 0.0, 115.0]
# [33.0, 86.0, 27.0, 7895.0, 0.0, 106.0]
# [25.0, 82.0, 24.0, 9233.0, 0.0, 102.0]

#5,7





Car_ID = 0
Risk = 1
Value_Loss = 2
Horsepower = 3
City_MPG = 4
Highway_MPG = 5
Price = 6


#Used to name files for printing out the graphs
testA = "alpha"
testE = "extend"
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

    fmemFile = File("fmemFile.csv")

    #import the data from a csv
    car_data = np.genfromtxt('car_data.csv', delimiter=',')

    #call the tree creator module and pass the name of the json file to it
    aTree = DecisionTree('jsonTrees/' + testA + '.json')
    nTree = DecisionTree('jsonTrees/' + testN + '.json')
    eTree = DecisionTree('jsonTrees/' + testE + '.json')



    #iterator = car_data[np.random.randint(car_data.shape[0], size=100), :]
    #iterator = car_data
    iterator = inputs2

    for inputs in iterator:



        #change the inputs for each of the cars in the tree


        #inputs = convertCarData(inputs)
        aTree.changeInputs(inputs)
        nTree.changeInputs(inputs)
        eTree.changeInputs(inputs)


        #get the score for that car

        aScore = aTree.run()
        nScore = nTree.run()
        eScore = eTree.run()

        print("Inputs:",inputs)
        print("ASCORE #######:",aScore)
        print("NSCORE #######:",nScore)
        print("ESCORE #######:",eScore)

        eScore = np.array(eScore)

        f1 = MemFunc('trap',aScore)
        X = np.arange(0,1,.05)

        l1, = plt.plot(X,[f1.memFunc(i) for i in X],c='r',linewidth=2.0,label="AlphaCuts")
        l2, = plt.plot(eScore[:,0],eScore[:,1],c='b',linewidth=2.0,label="Extention Principle")
        l3 = plt.axvline(nScore,c='g',linewidth=2.0,label="Crisp")

        plt.legend(handles=[l1,l2,l3])
        plt.title("Regular Title")
        plt.xlabel("Output Score")
        plt.ylabel("Membership Value")

        #Batch Save Rember to remove input
        #plt.savefig("test.png")


        plt.show()
        break



if __name__ == '__main__':
    main()

