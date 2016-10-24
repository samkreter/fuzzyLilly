from tree import DecisionTree
import numpy as np


def convertCarData(data):
    return [data[5],data[3],data[4],data[6],data[1],data[2]]


car_data = np.genfromtxt('car_data.csv', delimiter=',')


dTree = DecisionTree('tree1.json')
scores = []

for data in car_data:
    dTree.changeInputs(convertCarData(data))
    score = dTree.run()
    scores.append(score)
    print(score)



