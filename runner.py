from tree import Tree
import numpy as np


def convertCarData(data):
    return [data[5],data[3],data[4],data[6],data[1],data[2]]



car_data = np.genfromtxt('car_data.csv', delimiter=',')




dTree = Tree('tree1.json')

for data in car_data:
    dTree.changeInputs(convertCarData(data))
    print(dTree.run())


