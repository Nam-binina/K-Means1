import numpy as np
import random

def firstcenter(points,ncenters):
    center = []
    for i in range(0,ncenters):
        center.append(random.randint(0,len(points)))
    return center
array = np.array([1,2,3])

i = firstcenter(array,1)
print(f"{i}")