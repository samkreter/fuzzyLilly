import pandas as pd
import matplotlib.pyplot as plt
from extention import ExtentionOps
from memfuncs import MemFunc

df = pd.read_csv("fmemFile.csv")

#print(df.head())



e = ExtentionOps("add")
#e.convertToDomain()


for row in df.itertuples():
    A = e.convertToDomain([row[2],row[3],row[3],row[4]])
    print(A)
    plt.plot(A[:,0],A[:,1],c='g',linewidth=2)
    plt.show()
    t = input()


X = np.arange(0,1.1,.1)

for row in df.itertuples():
    m1 = MemFunc("tri",row[2],row[3],row[4])
    plt.plot(X,[m1.memFunc(i) for i in X ],c='g')
    plt.show()
    t = input()


#
# plt.plot(B[:,0],B[:,1],c='b')
# plt.xlim([0,2])
# plt.ylim([0,1])
#



# A = []
# B = []

# for i in np.arange(0,1,.05):

#     A.append([i,e.round2(mem1.memFunc(i))])

#     B.append([i,e.round2(mem2.memFunc(i))])

# A = np.array(A)
# B = np.array(B)



# #A = [.2,.4,.4,.6]
# # B = [.4,.6,.6,.8]

# print("########")
# #p = e.comp(A)
# t = e.extention([A,B])
# #print(e.extention([p,t]))
