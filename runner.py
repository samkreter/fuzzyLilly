from tree import DecisionTree
import numpy as np
import matplotlib.pyplot as plt


Car_ID = 0
Risk = 1
Value_Loss = 2
Horsepower = 3
City_MPG = 4
Highway_MPG = 5
Price = 6


def convertCarData(data):
    return [data[Highway_MPG],data[Horsepower],data[City_MPG],data[Price],data[Risk],data[Value_Loss]]


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


n, bins, patches = plt.hist(scores, normed=1, facecolor='green', alpha=0.75)
plt.show()




