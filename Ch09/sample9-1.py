import regTrees
from numpy import *

myDat=regTrees.loadDataSet('ex00.txt')
myMat = mat(myDat)
tree = regTrees.createTree(myMat)

print "%s" % tree


myDat1=regTrees.loadDataSet('ex0.txt')
myMat1=mat(myDat1)
tree2 = regTrees.createTree(myMat1) 

print "%s" % tree2