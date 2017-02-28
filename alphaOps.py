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
        [min(a*c,a*d,b*c,b*d), max(a*c,a*d,b*c,b*d)]

    def alphaCuts(self, params):

        #The levels of alpha cuts to take
        alphas = [0,.2,.8,1]

        fNum1 = params[0]
        fNum2 = params[1]

        #List of points collected
        points = []

        #Use the belive equations to get the alpha intervals from the membership functions
        #TRI: [(b-a)alpha + a, c - (c-b)alpha]
        #TRAP: [(b-a)alpha + a, d - (d-c)alpha]

        for alpha in alphas:

            a = self.pos1(fNum1,alpha)
            b = self.pos2(fNum1,alpha)
            c = self.pos1(fNum2,alpha)
            d = self.pos2(fNum2,alpha)

            points.append(self.op(a,b,c,d))


        #Create a trap membership function, tri is the same but the b and c values are equal
        #Comment out for regular fuzzy sets
        points = [points[0][0],points[3][0],points[3][1],points[0][1]]

        return points

# a = AlphaOps("ad").alphaCuts
# print(a([[1,2,3],[1,2,3]]))
