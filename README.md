# Pheromone-Delivery-Drone
## CS 179M Fall 2025 - Dr. Eamonn Keogh

## Overview
A pest, the naval orangeworm, is infesting almonds on an almond farm owned by Mr. Keogh. We want to find a way to mitigate pest damage, as crop losses have increased rapidly.

There are insect surveillance sensors in place to collect information about the insects, but the methods to eliminate them are expensive. The solution found was to use Pheromone-Based Mating Distribution (PBMD), which involves applying pheromone paste with a drone to confuse male insects from finding females. This approach is safer for the environment and more effective.

The problem we are trying to solve is that the drone's current flight time is too high, resulting in wasted battery. Therefore, our goal is to minimize the flight path length, given the list of locations the drone carrying the pheromone paste must visit. We will determine the shortest route that the drone needs to take to complete its task and return to its starting/charging point.

## Execution

1. Run the code by using this command in the terminal &rarr; python main.py
2. When prompted for a file, enter the name of a file of your choice. 
3. The output will list the landing pad locations, nodes visited, and routes for all possible number of drones
4. Then, when prompted, please enter the desired number of drones to be used.
5. The output will be ... 