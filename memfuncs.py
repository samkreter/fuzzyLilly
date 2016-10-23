import numpy as np



class memFunc():
    """docstring for memFunc"""

    def __init__(self, specs=[]):
        length = len(specs)
        self.specs = specs

        if length == 3:
            self.memberFuncName = "triangle"
            self.memFunc = self.tri
        elif length == 4:
            self.memberFuncName = "trapezoid"
            self.memFunc = self.trap
        else:
            raise Exception("Specs for membership function not correctly passed in")

    def __repr__(self):
        return self.memberFuncName

    def trap(self,input):
        specs = self.specs
        return max(min( (input-specs[0]) / (specs[1] - specs[0]), 1 ,(specs[3] - input)/(specs[3] - specs[2]) ),0)

    def tri(self, input):
        specs = self.specs
        return max(min( (input-specs[0]) / (specs[1] - specs[0]), (specs[2] - input)/(specs[2] - specs[1]) ),0)


def main():
    t = memFunc([1,2,3])
    print(t.memFunc(2))


if __name__ == '__main__':
    main()