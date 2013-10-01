from collections import *
import math
def buildVector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2= Counter(iterable2)
    all_items = set(counter1.keys()).union( set(counter2.keys()) )
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1,n2 in zip(v1, v2) )
    magnitude1 = math.sqrt (sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt (sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)


l1 = "Julie loves me more than Linda loves me".split()
l2 = "Jane likes me more than Julie loves me or".split()


v1,v2= buildVector(l1, l2)
print (cosim(v1, v2))