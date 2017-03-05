from memfuncs import MemFunc
import matplotlib.pyplot as plt
import numpy as np

w = 2
INC = .1

class ExtentionOps:

    def __init__(self,op):

        opDict = {'add':np.add,
                  'sub':np.subtract,
                  'div':np.divide,
                  'mul':np.multiply,
                  'max':max,
                  'min':min,
                  'pow':pow}

        if op in opDict:
            self.op = opDict[op]
        else:
            raise ValueError("Invalid Operator")

            #raise ValueError("Do not have that operator in AlphaOps")



    def convertToDomain(self,A):
        mem1 = MemFunc("trap",A)
        newA = []

        for i in np.arange(0,1,.05):

            newA.append([i,self.round2(mem1.memFunc(i))])

        return np.array(newA)

    def round2(self,val):
        val = int(val * 100)
        return val / 100

    def extention(self, params):


        A = params[0]

        for i in range(1,len(params)):
            B = params[i]


            if len(A) == 4:
                A = self.convertToDomain(A)
                B = self.convertToDomain(B)


            out = [[],[]]

            for a in A:
                for b in B:
                    z = self.round2(self.op(a[0], b[0]))
                    f = min(a[1],b[1])

                    try:
                        index = out[0].index(z)
                        out[1][index] = max(out[1][index],f)
                    except ValueError:
                        out[0].append(z)
                        out[1].append(f)


            fNum1 = out

            out = list(zip(out[0],out[1]))

            out.sort(key=lambda x:x[0])

            out = list(zip(*out))



            #[i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]

            plt.plot(out[0],out[1],c='r')
            plt.plot(A[:,0],A[:,1],c='g')
            plt.plot(B[:,0],B[:,1],c='b')
            plt.xlim([0,2])
            plt.ylim([0,1])
            plt.show()

        return fNum1




# e = ExtentionOps("add")
# mem1 = MemFunc('tri',[.2,.4,.6])
# mem2 = MemFunc('tri',[.4,.6,.8])
# #mem2 = lambda x: 1 if x == 1 else 0


# A = [.2,.4,.4,.6]
# B = [.4,.6,.6,.8]
# # A = []
# # B = []

# # for i in np.arange(0,1,.05):

# #     A.append([i,round2(mem1.memFunc(i))])

# #     B.append([i,round2(mem2.memFunc(i))])

# # A = np.array(A)
# # B = np.array(B)

# e.extention([A,B])






