import regression
import matplotlib.pyplot as plt
from numpy import *
xArr,yArr=regression.loadDataSet('ex0.txt')

#regression.lwlr(xArr[0],xArr,yArr,1.0)
#a = regression.lwlr(xArr[0],xArr,yArr,0.001)
yHat1 = regression.lwlrTest(xArr, xArr, yArr,1)
yHat2 = regression.lwlrTest(xArr, xArr, yArr,0.01)
yHat3 = regression.lwlrTest(xArr, xArr, yArr,0.003)
#print("yHat1 : %s" % (yHat1))

xMat=mat(xArr)
srtInd = xMat[:,1].argsort(0)
#print("srtInd : %s" % (srtInd))

xSort=xMat[srtInd][:,0,:]
#print("xSort : %s" % (xSort))

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(xSort[:,1],yHat1[srtInd])
ax1.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0] , s=2, c='red')

ax2 = fig.add_subplot(312)
ax2.plot(xSort[:,1],yHat2[srtInd])
ax2.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0] , s=2, c='red')

ax3 = fig.add_subplot(313)
ax3.plot(xSort[:,1],yHat3[srtInd])
ax3.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0] , s=2, c='red')
plt.show()