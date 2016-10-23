
class Ops():

    def printStuff(self):
        print(dir(self))

    def getFunc(self,operator):
        return getattr(self,operator)

    def compliment(self, x):
        return 1 - x

    def intersection(self, x, y):
        return min(x,y)

    def union(self, x, y):
        return max(x,y)


def main():
    t = Operators().getFunc("union")
    print(t(.5,.4))

if __name__ == '__main__':
    main()