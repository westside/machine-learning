from numpy import *

def cosine(a, b):

	value = (a[0] * b[0] + a[1] * b[1]) / sqrt(pow(a[0],2) + pow(a[1],2)) *sqrt(pow(b[0],2) + pow(b[1],2))
	return value



a = [3, 3]
b = [1, 1]

result = cosine(a, b)
print "%s" % result