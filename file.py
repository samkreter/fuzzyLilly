class File:

    def __init__(self,name="results.csv"):
        self.name = name

    def writeA(self,val,op="a"):
        with open(self.name,op) as f:
            f.write(','.join(map(str,val)) + '\n')