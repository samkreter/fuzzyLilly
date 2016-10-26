from memfuncs import MemFunc
import json
import matplotlib.pyplot as plt
import numpy as np


with open("memFuncs1.json") as data_file:
	data = json.load(data_file)


memFuncs = []
for func in data:
	memFuncs.append(MemFunc(func["memFunc"],func["memFuncSpecs"]))

for func in memFuncs:
    x = np.arange(func.specs[0]-1,func.specs[-1]+1,dtype=int)
    #vfunc = np.vectorize(func.memFunc)
    y = []
    for i in x:
        y.append(func.memFunc(i));
    plt.plot(x,y)
    plt.show()


    print(x)
    print(y)

