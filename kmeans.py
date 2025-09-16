import numpy as np
import random
import math

epsilon = 1e-6

import random

def firstcenter(points, ncenters):
    centers = []
    centers.append(points[random.randint(0, len(points)-1)])
    while len(centers) < ncenters:
        distances = [min(distance(p, c) for c in centers) for p in points]
        probs = [d**2 for d in distances]
        total = sum(probs)
        probs = [p/total for p in probs]
        r = random.random()
        cum_sum = 0
        for p, prob in zip(points, probs):
            cum_sum += prob
            if r < cum_sum:
                centers.append(p)
                break
    return centers



def distance(point1,point2):
    return math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))

def convergence(oldcenter,newcenter):
    for c_old, c_new in zip(oldcenter, newcenter):
        if distance(c_old, c_new) <epsilon:
            return False
    return True
def center(points,old_center):
    if len(points) == 0:
        return old_center
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)  
    return [x,y]
    
    

def kmeans(points,ncenter):
    centers = firstcenter(points,ncenter)
    optimal = True
    array = [c for c in range(ncenter)]
    while optimal:
        temparray = [[] for _ in range(ncenter)]
        for i in range(0,len(points)):
            if points[i] not in centers:
                distances = [distance(points[i], c) for c in centers]  # distance à définir (ex: euclidienne)
                min_index = distances.index(min(distances))
                temparray[min_index].append(points[i])
        newcenter = [
            center(cluster, old_center=centers[k])
            for k, cluster in enumerate(temparray)
        ]
        optimal = convergence(centers,newcenter)
        centers = newcenter
        array = temparray
    return centers,array

points = [
    [1, 2], [2, 1], [1, 1], 
    [10, 10], [10, 11], [11, 10], 
    [50, 50], [51, 51], [49, 50]
]
ncenter = 3

centers,array= kmeans(points, ncenter)
print(" Centre:")
print(centers)

print("\n Groupe :")
for i, array in enumerate(array):
    print(f"Groupe {i}:", array)
