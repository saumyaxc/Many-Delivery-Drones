import os
import math
import numpy as np
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from kmeans import kmeans


def main():
    filename = input("Enter the name of file: ").strip()
    filepath = f"../data/{filename}"

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    coords = np.loadtxt(filepath)
    numNodes = len(coords)

    ready_time = (datetime.now(ZoneInfo("America/Los_Angeles")) + timedelta(minutes=5)).strftime("%I:%M%p").lower()
    print(f"There are {numNodes} nodes: Solutions will be available by {ready_time}\n")

    allSolutions = []

    # Running kmeans for 1–4 drones --> 10 times each
    for num_drones in range(1, 5):
        best_solution = None
        best_distance = float("inf")

        for i in range(10):
            result = kmeans(coords, num_drones)
            if result["total_distance"] < best_distance:
                best_distance = result["total_distance"]
                best_solution = result

        allSolutions.append(best_solution)

        print(f"{num_drones}) If you use {num_drones} drone(s), the total route will be {best_solution['total_distance']:.1f} meters")
        for i, c in enumerate(best_solution["clusters"], 1):
            pad = c["center"]
            print(f"   {i}. Landing Pad {i} should be at [{int(pad[0])},{int(pad[1])}], "
                  f"serving {len(c['route'])} locations, route is {c['distance']:.1f} meters")
        print()

    # # objective funtion results
    # print("Objective Function Values (total distances):")
    # for i, sol in enumerate(allSolutions, 1):
    #     print(f"  {i} drone(s): {sol['total_distance']:.1f} meters")

    choice = int(input("\nSelect number of drones (1–4): "))
    chosen = allSolutions[choice - 1]
    base = filename.replace(".txt", "").split("/")[-1]
    folder = "../solutions/"

    for i, cluster in enumerate(chosen["clusters"], 1):
        dist = int(cluster["distance"])
        out_path = f"{folder}{base}_{i}_solution_{dist}.txt"
        
        coords_to_save = np.array([coords[int(idx)] for idx in cluster["route"]])
        np.savetxt(out_path, coords_to_save, fmt="%.4f") 
        print(f"  Saved {out_path}")


    print("\nAll done. Routes saved in /solutions/ folder.")


if __name__ == "__main__":
    main()
