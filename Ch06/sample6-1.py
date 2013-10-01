import svmMLiA
from numpy import *
import matplotlib.pyplot as plt

dataArr,labelArr = svmMLiA.loadDataSet('testSet.txt')

print "dataArr %s"  % dataArr
print "%s"  % labelArr


#b,alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)

#print " b: %s, alphas: %s" % (b, alphas)

fig = plt.figure()
ax = fig.add_subplot(111)

xArr = mat(dataArr)[:, 0];
yArr = mat(dataArr)[:, 1];

ax.scatter(xArr[:, 0].flatten().A[0], yArr[:,0].flatten().A[0])

ws = ws = zeros((100,1)); 
# yHat=xCopy*ws
# ax.plot(xCopy[:,1],yHat)
ax.plot([-2,10], [-8, 6])
plt.show()

