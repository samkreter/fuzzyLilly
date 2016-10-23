class Tree():
    """docstring for DecisionTree"""
    def __init__(self,operator,params,inputs=[]):
        self.root = Node(operator,params)
        self.inputs = inputs

    def changeInputs(self,params):
        for inp,num in zip(self.inputs,params):
            inp.inData = num

    def run(self):
        return self.root.run()


class InputNode():
    # check if the reference will hold
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



