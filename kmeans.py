import numpy as np
import random
import math

epsilon = 1e-6

import random

def firstcenter(points, ncenters):
    center = []
    for i in range(ncenters):
        center.append(points[random.randint(0, len(points)-1)])
    return center


def distance(point1,point2):
    return math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))

def convergence(oldcenter,newcenter):
    if distance(oldcenter[0],oldcenter[1])+distance(newcenter[0],newcenter[1])<epsilon:
        return False
    return True
def center(points):
    x = sum(points[0] for _ in points) / len(points)
    y = sum(points[1] for _ in points) / len(points)    
    return x,y
    
    

def kmeans(points,ncenter):
    center = firstcenter(points,ncenter)
    optimal = True
    while optimal:
        
        optimal = convergence()
    
array = np.array([1,2,3])

point1 = [1,2]
point2 = [1,5]

print(distance(point1,point2))

i = firstcenter(array,1)
print(f"{i}")