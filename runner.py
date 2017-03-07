from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


#Just easier to see the parts of the data
Car_ID = 0
Risk = 1
Value_Loss = 2
Horsepower = 3
City_MPG = 4
Highway_MPG = 5
Price = 6


#Used to name files for printing out the graphs
testName = "ZadehBaseTree"
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
    dTree = DecisionTree('jsonTrees/' + testName + '.json')

    scores = []
    #track the best score and data
    best = [0,0]
    test = []


    for data in car_data:

        #change the inputs for each of the cars in the tree
        dTree.changeInputs(convertCarData(data))
        #get the score for that car
        score = dTree.run()


        #check if its the highest
        if(score > best[0]):
        	best[0] = score
        	best[1] = data
        #add it to the list of scores
        scores.append(score)
        test.append([score,data.tolist()])


    #print("best",best[0],best[1])

    test = sorted(test,key=lambda x: x[0],reverse=True)

    pprint(test[0:3])

    #create a normilized histagram of the scores
    n, bins, patches = plt.hist(scores, normed=1, facecolor='green', alpha=0.75)
    plt.title(testName+wValue)
    #save the image to a file
    plt.savefig("graphs/" + testName + wValue + ".png", bbox_inches='tight')
    #show the image
    plt.show()


if __name__ == '__main__':
    main()


