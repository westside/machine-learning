import adaboost
from numpy import *

datMat,classLabels=adaboost.loadSimpData()

print "%s \n %s" % (classLabels, classLabels)

D = mat(ones((5,1))/5)

print "%s" % D

bestStump,minError,bestClasEst = adaboost.buildStump(datMat,classLabels,D)

print "%s" % bestStump
print "%s" % minError
print "%s" % bestClasEst

