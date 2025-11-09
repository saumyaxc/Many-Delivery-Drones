import numpy as np
from nearestNeighbor import NearestNeighborDistance as nn

def objectiveFunction(points, labels, centers):
    return float(np.sum((points - centers[labels]) ** 2))

def kmeans(points, k):
    points = np.array(points)
    n = len(points)

    # Step 2
    centers = points[np.random.choice(n, k, replace=False)]

    for j in range(100):

        # Step 3
        expandedPoints = points[:, np.newaxis]
        distances = np.linalg.norm(expandedPoints - centers, axis=2)
        labels = np.argmin(distances, axis=1)

        # Step 4
        newCenters = np.array([
            points[labels == i].mean(axis=0) if np.any(labels == i) else centers[i]
            for i in range(k)
        ])

        # Step 5
        if np.allclose(newCenters, centers):
            break
        centers = newCenters

    clusters = []

    for i in range(k):

        clusterPoints = points[labels == i]
        if len(clusterPoints) == 0:
            continue

        route, dist = nn(clusterPoints)
        route = [r for r in route if r < len(clusterPoints)]
        clusters.append({
            "center": centers[i],
            "route": clusterPoints[route],
            "distance": dist
        })

    kmeansObj = objectiveFunction(points, labels, centers)
    totalDistance = sum(c["distance"] for c in clusters)

    return {"totalDistance": totalDistance, "objective": kmeansObj, "clusters": clusters}