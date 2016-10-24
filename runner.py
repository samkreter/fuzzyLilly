from tree import Tree
import numpy as np


my_data = np.genfromtxt('car_data.csv', delimiter=',')


dTree = Tree('tree1.json')

print(dTree.printInputs())

