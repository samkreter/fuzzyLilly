import numpy as np


fsize = 10

class MemFunc():
    """Creates the specific membership function and is used to continue the process"""

    def __init__(self, name,specs=[], fMemFunc = False, fNumDiff = .2):

        #Get the specs of how to define the membership functions
        self.specs = specs
        self.memFuncName = name

        if fMemFunc:
            self.fMemFunc = getattr(self,fMemFunc)
            self.fNumDiff = fNumDiff

        self.memFunc = getattr(self,name)


    #The to_string function to show the name of the membership function
    # when trying to print
    def __repr__(self):
        return self.memberFuncName



    def fMem(self,input):

        #Get the fuzzy value of the input
        b = self.fMemFunc(input)

        c = min(1,b + self.fNumDiff)
        a = max(0,b - self.fNumDiff)
        #print("input: ",input, "specs: ",self.specs,"out:",b)
        #print("Fmem:",[a,b,c])
        #Convert it to a fuzzy number
        return [a, b, b, c]




    def gauss(self,input):
        #Find the mean of the specs passed in
        # easy way to convert the same definition of a trap func to a gauss
        mu = np.mean(self.specs)
        sigma = np.std(self.specs)

        return np.exp(-((input - mu) ** 2.) / float(sigma) ** 2.)

    def trap(self,input):
        if(len(self.specs) < 4):
            raise Exception("Not enough specs passed in for the Trapezoid membership function")

        a = self.specs[0]
        b = self.specs[1]
        c = self.specs[2]
        d = self.specs[3]



        if input <= b:
            return self.tri(input, vals=[a, b, b])
        elif input >= c:
            return self.tri(input,vals=[c, c, d])
        else:
            return 0






    def tri(self, input, vals = False):

        if(len(self.specs) < 3):
            raise Exception("Not enough specs passed in for the Triangle membership function")


        if vals:
            a = vals[0]
            b = vals[1]
            c = vals[2]
        else:
            a = self.specs[0]
            b = self.specs[1]
            c = self.specs[2]


        if input == b:
            return 1
        elif a != b and input > a and input < b:
            return (input - a) / float(b - a)

        elif b != c and input > b and input < c:
            return (c - input) / float(c - b)
        else:
            return 0



