from tree import Tree,Node,InputNode
from operators import Ops
from memfuncs import MemFunc


inNode = InputNode(memFunc=MemFunc([1,2,3]).memFunc, inData=1.5)
inNode2 = InputNode(memFunc=MemFunc([1,2,3,4]).memFunc, inData=3)

#n1 = Node(Ops().getFunc("union"),[inNode,inNode2])

dTree = Tree(Ops().getFunc("intersect"),[inNode,inNode2])

print(dTree.run())

