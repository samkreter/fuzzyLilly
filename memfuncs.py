

class MemFunc():
    """Creates the specific membership function and is used to continue the process"""

    def __init__(self, name,specs=[]):
        length = len(specs)
        self.specs = specs
        self.memFuncName = name

        self.memFunc = getattr(self,name)


    def __repr__(self):
        return self.memberFuncName


    def trap(self,input):
        if(len(self.specs) < 4):
            raise Exception("Not enough specs passed in for the Trapezoid membership function")

        specs = self.specs

        ba = (specs[1] - specs[0])
        dc = (specs[3] - specs[2])

        if(ba == 0):
            ba = 1
        elif(dc == 0):
            dc = 1

        return max(min( (input-specs[0]) / ba, 1 ,(specs[3] - input)/dc ),0)

    def tri(self, input):

        if(len(self.specs) < 3):
            raise Exception("Not enough specs passed in for the Triangle membership function")

        specs = self.specs
        return max(min( (input-specs[0]) / (specs[1] - specs[0]), (specs[2] - input)/(specs[2] - specs[1]) ),0)


def main():
    t = memFunc([1,2,3])
    print(t.memFunc(2))


if __name__ == '__main__':
    main()