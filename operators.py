


class Ops():
    """Used the generate the correct fuzzy set operation for each node"""
    def printStuff(self):
        print(dir(self))

    def getFunc(self,operator):
        return getattr(self,operator)

    def compliment(self, x):
        return 1 - x[0]

    def intersect(self, params):
        return min(*params)

    def union(self, params):
        return max(*params)

