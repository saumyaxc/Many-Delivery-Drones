import matplotlib.pyplot as plt

def visualization(filename, clusters):
    """
    Visualizes all drone routes in one plot exactly as they are saved to text files.

    Parameters:
        filename (str): Base name for the output file
        clusters (list): List of cluster dictionaries from kmeans, each containing:
                         'route': array of coordinates [[x1, y1], ...]
                         'distance': total distance of this cluster
                         'center': coordinates of landing pad [x, y]
    """
    width, height = 12, 12
    dpi = 1920 / min(width, height)
    plt.figure(figsize=(width, height), dpi=dpi)

    colors = ['b', 'g', 'c', 'm', 'y', 'k']  # colors for routes

    for i, cluster in enumerate(clusters):
        route = cluster['route']  # use the same order saved in the text file
        center = cluster['center']

        x = route[:, 0]
        y = route[:, 1]

        color = colors[i % len(colors)]
        # Plot route exactly in saved order
        plt.plot(x, y, 'o-', color=color, label=f"Drone {i+1} (Dist: {cluster['distance']:.1f} m)")

        # Plot the landing pad as a red triangle
        plt.plot(center[0], center[1], 'r^', markersize=10)
        plt.text(center[0] + 0.5, center[1] + 0.5, str(i+1), color='red', fontsize=12)

    # Plot settings
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Drone Routes for All Clusters")
    plt.legend()
    plt.grid(True)

    img_file = f"{filename}_OVERALL_SOLUTION.jpeg"
    plt.savefig(img_file, bbox_inches="tight")
    plt.close()
    print(f"==> Visualization saved as {img_file}")
