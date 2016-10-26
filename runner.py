from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt


def convertCarData(data):
    return [data[5],data[3],data[4],data[6],data[1],data[2]]


car_data = np.genfromtxt('car_data.csv', delimiter=',')


dTree = DecisionTree('tree1.json')
scores = []
best = [0,0]

for data in car_data:
    dTree.changeInputs(convertCarData(data))
    score = dTree.run()
    if(score > best[0]):
    	best[0] = score
    	best[1] = data
    scores.append(score)
    print(score)

print(best[0])
print(best[1])

n, bins, patches = plt.hist(scores, normed=1, facecolor='green', alpha=0.75)
plt.show()




