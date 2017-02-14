import json

#import the created helper functions
from operators import Ops
from memfuncs import MemFunc


class DecisionTree():
    """Takes in a json file of the tree structure then generates the tree"""

    def __init__(self,filename):
        #parse the json file into a data structure
        with open(filename) as data_file:
            data = json.load(data_file)

        self.inputs = []
        #Call the recursive function to create the tree from the json file
        self.root = self.createNodes(data)


    #recusive function that creates each node in the tree
    def createNodes(self,baseNode):
        params = []

        #loop through all the params that go into each node
        for node in baseNode['params']:
            #if its an input, create the input and track its location
            if node['type'] == "Input":
                InNode = InputNode(memFunc=MemFunc(node['memFunc'],node['memFuncSpecs']).memFunc, inData=node['input'],name=node['name'])
                self.inputs.append(InNode)
                params.append(InNode)
            #otherwise recusivly call the function on its paramters
            else:
                params.append(self.createNodes(node))

        #once all paramaters are craeted, created the node and return it
        return Node(Ops().getFunc(baseNode['op']),params)

    #Change the tracked inputs to go through multiple samples
    def changeInputs(self,params):
        for inp,num in zip(self.inputs,params):
            inp.inData = num

    #print the order that the inputs are stored
    def printInputs(self):
        for inp in self.inputs:
            print(inp.name)

    #Run the tree and get all the scores
    def run(self):
        return self.root.run()


#Class to hold each of the input nodes
class InputNode():
    def __init__(self,memFunc,inData,name):
        self.memFunc = memFunc
        self.inData = inData
        self.name = name

    def setInput(self, inData):
        self.inData = inData

    def run(self):
        #return the datapiont passed through the membership function
        return self.memFunc(self.inData)


#Class to hold each of the operator nodes
class Node():
    """docstring for Node"""
    def __init__(self, operator, params = []):
        self.operator = operator
        self.params = params

    def changeParams(self,params):
        self.params = params

    def run(self):
        items = []
        #get the values of all params for the node
        for param in self.params:
            items.append(param.run())

        #return the operator for the node
        return self.operator(items)



