class Tree():
    """docstring for DecisionTree"""
    def __init__(self):
        self.root = Node()
        self.bottom = []

    def run(self):
        return self.root.run()


class Node(object):
    """docstring for Node"""
    def __init__(self, operator, params = []):
        self.operator = operator
        self.params = params

    def changeParams(self,params):
        self.params = params

    def run(self):
        items = []
        for param in self.params:
            if isinstance(param,Node):
                items.append(param.run())
            else:
                items.append(param)

        return self.operator(*items)



