import numpy as np
import math, time

#basic KNN algorithm - used geeksforgeeks for algorithm reference
def euclideanDistance(x, y):
    total = 0
    for i in range(len(x)):
        total += ((x[i]-y[i])**2)
    return math.sqrt(total)

def NearestNeighborDistance (dataPts):

    startTimer = time.time()

    n = len(dataPts)
    visited = [False] * n
    route = [0]
    visited[0] = True
    totalDistance = 0.0
    currIndex = 0

    for step in range(n-1):
        nearestIndex = -1
        nearestDistance = float("inf")

        for j in range(n):
            if not visited[j]:
                d = euclideanDistance(dataPts[currIndex], dataPts[j])
                if d < nearestDistance:
                    nearestDistance = d
                    nearestIndex = j
        
        route.append(nearestIndex)
        visited[nearestIndex] = True
        totalDistance += nearestDistance
        currIndex = nearestIndex

    backToBase = euclideanDistance(dataPts[currIndex], dataPts[0])
    totalDistance += backToBase
    route.append(0)

    route = [x + 1 for x in route]

    endTimer = time.time()

    if totalDistance > 6000:
        print("Warning: Solution is ", totalDistance, "greater than the 6000-meter constraint. ")

    return route, totalDistance