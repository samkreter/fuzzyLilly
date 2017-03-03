w = 2

class AlphaOps:

    def __init__(self,op):

        self.op = getattr(self,op)

            #raise ValueError("Do not have that operator in AlphaOps")


    def pos1(self, fNum, alpha):
        return ((fNum[1]-fNum[0]) * alpha + fNum[0])

    def pos2(self, fNum, alpha):
        size = len(fNum)
        return (fNum[size - 1] - (fNum[size - 1]-fNum[size - 2]) * alpha)

    def add(self,a,b,c,d):
       return [a + c, b + d]

    def sub(self,a,b,c,d):
        return [a - d, b - c]

    def max(self,a,b,c,d):
        return [max(a,c), max(b,d)]

    def min(self,a,b,c,d):
        return [min(a,c), min(b,d)]

    def mul(self,a,b,c,d):
        return [min(a*c,a*d,b*c,b*d), max(a*c,a*d,b*c,b*d)]

    #Look into the change here
    def comp(self,a,b):
        return [1-b, 1-a]

########## Yager Ops ####################

#Beta
    def yagerComp(self,a,b):
        return [(1-a)**(1/w), (1-b)**(1/w)]

    def yagerUnion(self,a,b,c,d):
        return [min(1, (a**w + c**w) ** (1/w)),min(1, (b**w + d**w) ** (1/w))]

    def yagerIntersect(self,a,b,c,d):
        return [1 - min(1,((1 - a)**w + (1 - c)**w)), 1 - min(1,((1 - b)**w + (1 - d)**w))]




    def alphaCuts(self, params):

        #The levels of alpha cuts to take
        alphas = [0,.2,.8,1]

        fNum1 = params[0]


        #List of points collected
        points = []

        #Use the belive equations to get the alpha intervals from the membership functions
        #TRI: [(b-a)alpha + a, c - (c-b)alpha]
        #TRAP: [(b-a)alpha + a, d - (d-c)alpha]

        for i in range(1,len(params)):
            fNum2 = params[i]
            for alpha in alphas:

                a = self.pos1(fNum1,alpha)
                b = self.pos2(fNum1,alpha)
                c = self.pos1(fNum2,alpha)
                d = self.pos2(fNum2,alpha)

                points.append(self.op(a,b,c,d))


            #Create a trap membership function, tri is the same but the b and c values are equal
            #Comment out for regular fuzzy sets
            fNum1 = [points[0][0],points[3][0],points[3][1],points[0][1]]
            points = []

        return fNum1

# a = AlphaOps("add").alphaCuts
# print(a([[1,2,3],[1,2,3],[1,2,3]]))
