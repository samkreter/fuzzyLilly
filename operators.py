
class Ops():

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


def main():
    t = Operators().getFunc("union")
    print(t(.5,.4))

if __name__ == '__main__':
    main()