import numpy as np


fsize = 10

class MemFunc():
    """Creates the specific membership function and is used to continue the process"""

    def __init__(self, name,specs=[], fMemFunc = False, stage0Op = False):

        #Get the specs of how to define the membership functions
        self.specs = specs
        self.memFuncName = name

        if fMemFunc and stage0Op:
            self.fMemFunc = getattr(self,fMemFunc)
            self.stage0Op = stage0Op

        self.memFunc = getattr(self,name)


    #The to_string function to show the name of the membership function
    # when trying to print
    def __repr__(self):
        return self.memberFuncName


    def fuzzyMem(self,input):

        #Create a fuzzy number from the number that is passed in
        fNum = MemFunc("tri",[input - fsize / 2, input, (input + fsize / 2 )])

        #Collet the new fuzzy set thats created
        newFSet = []

        #That nice trick to be able to quicly add operators
        operators = {"mul": np.multiply,
                     "min": min}


        #Convert the operator string to the actual op
        # Weird thing to do but its a little safer than just letting the user
        # pass in a random op, at least for now
        op = operators[self.stage0Op]


        #Iterate throught the set
        for i in range(input - fsize // 2, (input + fsize // 2 ) + 1):
            newFSet.append((op(fNum.memFunc(i),self.fMemFunc(i)),i))

        return newFSet



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


