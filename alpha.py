from memfuncs import MemFunc
import operator
import numpy as np

def pos1(fNum, alpha):
    return ((fNum[1]-fNum[0]) * alpha + fNum[0])

def pos2(fNum, alpha):
    size = len(fNum)
    return (fNum[size - 1] - (fNum[size - 1]-fNum[size - 2]) * alpha)

def fAdd(a,b,c,d):
   return [a + c, b + d]

def fSub(a,b,c,d):
    return [a - d, b - c]

def fMax(a,b,c,d):
    return [max(a,c), max(b,d)]

def fMin(a,b,c,d):
    return [min(a,c), min(b,d)]

def fMul(a,b,c,d):
    [min(a*c,a*d,b*c,b*d), max(a*c,a*d,b*c,b*d)]

def alphaCutsAdd(fNum1, fNum2, op):

    #The levels of alpha cuts to take
    alphas = [0,.2,.8,1]

    #defiinitions for each of the operations
    operations = {"add": fAdd,
                  "sub": fSub,
                  "mul": fMul,
                  "max": fMax,
                  "min": fMin}

    #List of points collected
    points = []

    #Use the belive equations to get the alpha intervals from the membership functions
    #TRI: [(b-a)alpha + a, c - (c-b)alpha]
    #TRAP: [(b-a)alpha + a, d - (d-c)alpha]

    for alpha in alphas:

        a = pos1(fNum1,alpha)
        b = pos2(fNum1,alpha)
        c = pos1(fNum2,alpha)
        d = pos2(fNum2,alpha)

        if op in operations:
            points.append(operations[op](a,b,c,d))
        else:
            raise ValueError("Operation not avalible")

    #Create a trap membership function, tri is the same but the b and c values are equal
    #Comment out for regular fuzzy sets
    points = [points[0][0],points[3][0],points[3][1],points[0][1]]

    return points




# How big do you want the fuzzy set to be outputted
fsize = 10


#Comput the
def stage0(num,opString):


    mem = MemFunc("trap",[1,2,3,10])

    #Create a fuzzy number from the number that is passed in
    fNum = MemFunc("tri",[num - fsize / 2, num, (num + fsize / 2 )])

    #Collet the new fuzzy set thats created
    newFSet = []

    #That nice trick to be able to quicly add operators
    operators = {"mul": operator.mul,
                 "min": min}


    #Convert the operator string to the actual op
    op = operators[opString]


    #Iterate throught the set
    for i in range(num - fsize // 2, (num + fsize // 2 ) + 1):
        newFSet.append((op(fNum.memFunc(i),mem.memFunc(i)),i))

    #Force it to be traingular
    mems, domain = zip(*newFSet)

    maxIndex = np.argmax(mems)

    for i in range(maxIndex, len(mems)):
        if mems[i] == 0:
            c = domain[i]
            break;
        c = domain[i]

    for i in range(maxIndex,0,-1):
        if mems[i] == 0:
            a = domain[i]
        a = domain[i]

    b = domain[maxIndex]

    print(a,b,c)


    return [a,b,c]


print(stage0(2,"min"))
#print(alphaCutsAdd([1,2,3,4],[2,3,4,5],"sub"))







