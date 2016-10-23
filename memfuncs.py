import numpy as np



class memFunc():
    """docstring for memFunc"""
    def __init__(self, specs=[]):
        length = len(specs)
        if length == 3:
            self.memFunc = self.trap(specs)
        elif length == 4:
            self.memFunc = self.tri(specs)
        else:
            raise Exception("Specs for membership function not correctly passed in")

    def trap(self,specs):
        pass

    def tri(self, specs):
        pass


def tri(specs,input):
    return max(min( (input-specs[0]) / (specs[1] - specs[0]), (specs[2] - input)/(specs[2] - specs[1]) ),0)

def trap(specs,input):
    return max(min( (input-specs[0]) / (specs[1] - specs[0]), 1 ,(specs[3] - input)/(specs[3] - specs[2]) ),0)



def main():
    print(trap([1,2,3,4],3.5))


if __name__ == '__main__':
    main()