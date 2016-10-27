
w = 2

class Ops():

    """Used the generate the correct fuzzy set operation for each node"""
    def printStuff(self):
        print(dir(self))

    def getFunc(self,operator):
        return getattr(self,operator)

    #Zadeh Operators#########################
    def compliment(self, x):
        return 1 - x[0]

    def intersect(self, params):
        return min(*params)

    def union(self, params):
        return max(*params)


    #boudned sum operations##################
    def bunion(self,params):
        return min(1,sum(params))

    def bintersect(self,params):
        return max(0,(sum(params) - 1))

    #Yager Operations##########################
    def ycompliment(self,x):
        return (1 - x[0]**w)**(1/w)

    def yunion(self,params):
        if(len(params) < 2):
            raise Exception("Must provide at lease two params to perform an union")
        return (min(1,(sum(list(map(lambda x : x ** w,params))))**(1/w)))


    def yintersect(self,params):
        if(len(params) < 2):
            raise Exception("Must provide at lease two params to perform an intersection")
        return (min(1,(sum(list(map(lambda x : (1-x) ** w,params))))**(1/w)))








