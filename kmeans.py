import numpy as np
import random
import math

def firstcenter(points,ncenters):
    center = []
    for i in range(0,ncenters):
        center.append(random.randint(0,len(points)))
    return center

def distance(point1,point2):
    return math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))
    
array = np.array([1,2,3])

point1 = [1,2]
point2 = [1,5]

print(distance(point1,point2))

i = firstcenter(array,1)
print(f"{i}")