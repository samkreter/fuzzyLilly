import json

from operators import Ops
from memfuncs import MemFunc

class Tree():
    """docstring for DecisionTree"""
    def __init__(self,filename):
        with open(filename) as data_file:
            data = json.load(data_file)

        self.inputs = []
        self.root = self.createNodes(data)


    def createNodes(self,baseNode):
        params = []

        for node in baseNode['params']:
            if node['type'] == "Input":
                InNode = InputNode(memFunc=MemFunc(node['memFunc']).memFunc, inData=node['input'])
                self.inputs.append(InNode)
                params.append(InNode)
            else:
                params.append(self.createNodes(node))

        return Node(Ops().getFunc(baseNode['op']),params)

    def changeInputs(self,params):
        for inp,num in zip(self.inputs,params):
            inp.inData = num

    def run(self):
        return self.root.run()


class InputNode():
    def __init__(self,memFunc,inData):
        self.memFunc = memFunc
        self.inData = inData

    def setInput(self, inData):
        self.inData = inData

    def run(self):
        return self.memFunc(self.inData)


class Node():
    """docstring for Node"""
    def __init__(self, operator, params = []):
        self.operator = operator
        self.params = params

    def changeParams(self,params):
        self.params = params

    def run(self):
        items = []
        for param in self.params:
            items.append(param.run())

        return self.operator(*items)



