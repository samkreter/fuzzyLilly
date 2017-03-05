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
        print("input: ",input, "specs: ",self.specs,"out:",b)
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

        specs = self.specs

        #used to check for the case where ba or dc are the same causing
        # a divide by zero error when computing the  function
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

        #used to check for the case where b a are the same causing
        # a divide by zero error when computing the  function
        ba = (specs[1] - specs[0])

        if ba == 0:
            ba = 1

        specs = self.specs
        return max(min( (input-specs[0]) / ba , (specs[2] - input)/(specs[2] - specs[1]) ),0)


