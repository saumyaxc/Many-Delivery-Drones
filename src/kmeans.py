import numpy as np
from random import randint
from nearestNeighbor import NearestNeighborDistance as nn
from nearestNeighbor import euclideanDistance as ed


def kmeans(points, k):
    
    points = np.array(points)
    n = len(points)

    # Step 2
    centroids = points[[randint(0, n - 1) for m in range(k)]]

    for j in range(100):

        # Step 3
        dists = np.linalg.norm(points[:, None] - centroids[None, :], axis=2)
        labels = np.argmin(dists, axis=1)

        # Step 4 
        new_centroids = np.array([
            points[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])

        # Step 5
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids

    clusters = []
    total_distance = 0

    for i in range(k):

        cluster_points = points[labels == i]

        if len(cluster_points) == 0:
            continue
        
        route, dist = nn(cluster_points)
        total_distance += dist
        clusters.append({
            "center": centroids[i],
            "route": route,
            "distance": dist
        })

    return {"total_distance": total_distance, "clusters": clusters}