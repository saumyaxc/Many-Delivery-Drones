import numpy as np
import math, time

#basic KNN algorithm - used geeksforgeeks for algorithm reference
def euclideanDistance(x, y):
    total = 0
    for i in range(len(x)):
        total += ((x[i]-y[i])**2)
    return math.sqrt(total)

def NearestNeighborDistance (dataPts, centroid): 

    # Combine centroid and delivery points. Centroid is always index 0.
    routing_data = np.vstack([centroid, dataPts])
    
    # CORRECT: n is the total number of points (Centroid + Deliveries)
    n_total = len(routing_data)
    
    # CORRECT: visited array must be the size of n_total
    visited = [False] * n_total 
    
    # Start the route at index 0 (the centroid)
    route = [0]
    visited[0] = True
    totalDistance = 0.0
    currIndex = 0

    # The loop needs to run n_total - 1 times to visit every other point
    for step in range(n_total - 1): 
        nearestIndex = -1
        nearestDistance = float("inf")

        # Inner loop checks every unvisited point, including delivery points
        for j in range(n_total): 
            if not visited[j]:
                d = euclideanDistance(routing_data[currIndex], routing_data[j])
                if d < nearestDistance:
                    nearestDistance = d
                    nearestIndex = j
        
        # If no unvisited point is found (shouldn't happen here, but safe coding)
        if nearestIndex == -1:
             break 
                
        route.append(nearestIndex)
        visited[nearestIndex] = True
        totalDistance += nearestDistance
        currIndex = nearestIndex

    # CORRECT: Closes the loop back to the starting point, the centroid (index 0)
    backToCentroid = euclideanDistance(routing_data[currIndex], routing_data[0])
    totalDistance += backToCentroid
    route.append(0)

    # Note: The 'route = [x + 1 for x in route]' line is no longer necessary or correct 
    # since the indices now refer to the position in routing_data.

    return route, totalDistance