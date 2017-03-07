from memfuncs import MemFunc
import matplotlib.pyplot as plt
import numpy as np
from file import File

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

        self.opName = op
        #Weird worka round for the complemnt
        if op == "comp":
            self.func = self.comp
        elif op in opDict:
            self.op = opDict[op]
            self.func = self.extention
        else:
            raise ValueError("Invalid Operator")


            #raise ValueError("Do not have that operator in AlphaOps")



    def convertToDomain(self,A):


        mem1 = MemFunc("trap",A)
        newA = []

        for i in np.arange(0,1.05,.05):

            newA.append([i,self.round2(mem1.memFunc(i))])


        return newA


    def round2(self,val):
        val = int(val * 100)
        return (val / 100)


    def round_to_05(self,n):
        correction = 0.5 if n >= 0 else -0.5
        return int( n/.05+correction ) * .05


    def comp(self,A):
        A = A[0]
        if len(A) == 4:
            A = self.convertToDomain(A)

        out = [[],[]]
        for a in A:
            z = self.round_to_05(self.round2(1.0 - a[0]))
            f = a[1]

            try:
                index = out[0].index(z)
                out[1][index] = max(out[1][index],f)
            except ValueError:
                out[0].append(z)
                out[1].append(f)


        out = list(zip(out[0],out[1]))

        out.sort(key=lambda x:x[0])

        out1 = list(zip(*out))

        A = np.array(A)
        #[i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
        plt.title("Compliment")
        plt.plot(out1[0],out1[1],c='y',linewidth=2)
        plt.plot(A[:,0],A[:,1],c='k',linewidth=2)
        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.show()

        print(out)

        return out

    def extention(self, params):


        A = params[0]
        for i in range(1,len(params)):
            B = params[i]

            #Convert a membership function to the right domain the first time
            if len(A) == 4:
                A = self.convertToDomain(A)
            if len(B) == 4:
                B = self.convertToDomain(B)

            # print("A:",A)
            # print("B:",B)


            out = [[],[]]

            for a in A:
                for b in B:
                    z = self.round2(self.op(a[0], b[0]))

                    try:
                        b[1]
                    except:
                        continue

                    f = min(a[1],b[1])

                    try:
                        index = out[0].index(z)
                        out[1][index] = max(out[1][index],f)
                    except ValueError:
                        out[0].append(z)
                        out[1].append(f)




            out = list(zip(out[0],out[1]))

            out.sort(key=lambda x:x[0])


            B = np.array(B)
            A = np.array(A)

            out1 = np.array(list(zip(*out)))
            plt.plot(A[:,0],A[:,1],c='b',linewidth=2)
            plt.plot(B[:,0],B[:,1],c='g',linewidth=2)
            plt.plot(out1[0],out1[1],c='y',linewidth=2)
            plt.xlim([0,1])
            plt.ylim([0,1])
            plt.title(self.opName)
            plt.show()

            A = out


        return A




# e = ExtentionOps("add")
# mem1 = MemFunc('tri',[.2,.2,.4])
# mem2 = MemFunc('tri',[.4,.6,.8])
# #mem2 = lambda x: 1 if x == 1 else 0



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






