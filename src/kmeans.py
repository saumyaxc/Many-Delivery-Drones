import numpy as np
# Assuming NearestNeighborDistance (nn) is defined in nearestNeighbor.py
from nearestNeighbor import NearestNeighborDistance as nn 

def objectiveFunction(points, labels, centers):
    # Calculates the Sum of Squared Distances (SSD), the k-means objective.
    return float(np.sum((points - centers[labels]) ** 2))

def kmeans(points, k):
    points = np.array(points)
    n = len(points)

    # Step 2: Initialize centers (randomly select k points)
    centers = points[np.random.choice(n, k, replace=False)]

    for j in range(100):

        # Step 3: Assignment step (assign points to nearest center)
        expandedPoints = points[:, np.newaxis]
        distances = np.linalg.norm(expandedPoints - centers, axis=2)
        labels = np.argmin(distances, axis=1)

        # Step 4: Update step (calculate new centers)
        newCenters = np.array([
            # Calculate the mean of all points assigned to this cluster
            points[labels == i].mean(axis=0) if np.any(labels == i) else centers[i]
            for i in range(k)
        ])

        # Step 5: Check for convergence
        if np.allclose(newCenters, centers):
            break
        centers = newCenters

    clusters = []

    for i in range(k):
        centroid = centers[i]
        clusterPoints = points[labels == i]
        
        if len(clusterPoints) == 0:
            continue

        # CORRECTED: 
        # 1. Pass the specific centroid (centers[i]) to the nn function.
        # 2. Create the combined data array for routing.
        routing_data = np.vstack([centroid, clusterPoints])
        
        # Call NN, which returns indices relative to the routing_data array
        route_indices, dist = nn(clusterPoints, centroid)
        
        # CORRECTED: 
        # Use the indices returned by nn to select coordinates from the combined array.
        # This correctly includes the centroid's coordinates at the start and end (index 0).
        route_coords = routing_data[route_indices]

        clusters.append({
            "center": centroid,
            "route": route_coords,
            "distance": dist
        })

    kmeansObj = objectiveFunction(points, labels, centers)
    totalDistance = sum(c["distance"] for c in clusters)

    return {"totalDistance": totalDistance, "objective": kmeansObj, "clusters": clusters}