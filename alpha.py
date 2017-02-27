

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
    return [max(a,c),max(b,d)]

def fMin(a,b,c,d):
    return [min(a,c),min(b,d)]

def alphaCutsAdd(fNum1, fNum2, op):

    alphas = [0,.2,.8,1]

    operations = {"add": fAdd,
                  "sub": fSub,
                  "max": fMax,
                  "min": fMin}

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


print(alphaCutsAdd([1,2,3,4],[1,2,3,4],"min"))

