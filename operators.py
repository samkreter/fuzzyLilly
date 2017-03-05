from alphaOps import AlphaOps
from extention import ExtentionOps

#Gloabal w value, bad practice but this easy for now
w = 2

class Ops():

    """Used the generate the correct fuzzy set operation for each node"""
    def printStuff(self):
        print(dir(self))

    def getFunc(self,operator):

        ops = operator.split(":")

        if ops[0] == "alpha":
            return AlphaOps(ops[1]).alphaCuts
        elif ops[0] == "extend":
            return ExtentionOps(ops[1]).extention
        else:
            return getattr(self,ops[0])


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
        # Takes the list of params, maps them to the lambda function thaat
        # will take x to the power of w
        return (min(1,(sum(list(map(lambda x : x ** w,params))))**(1/w)))


    def yintersect(self,params):
        if(len(params) < 2):
            raise Exception("Must provide at lease two params to perform an intersection")

        # does the same mapping as above but subtracts one before the mapping
        return (min(1,(sum(list(map(lambda x : (1-x) ** w,params))))**(1/w)))








