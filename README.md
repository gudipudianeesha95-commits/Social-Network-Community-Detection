# Social Network Community Detection

## 1. Introduction

Social Network Community Detection is a Python-based project that identifies groups or communities in a social network.

In this project, users are represented as nodes and their connections are represented as edges. The project uses NetworkX to create and analyze the social network graph.

## 2. Objectives

- Create a social network graph.
- Represent users as nodes.
- Represent connections as edges.
- Detect communities in the network.
- Perform parallel processing of nodes.
- Visualize the detected communities.

## 3. Technologies Used

- Python
- NetworkX
- Matplotlib
- NumPy
- Pandas
- ThreadPoolExecutor

## 4. Project Structure

Social-Network-Community-Detection/

│

├── data/

├── results/

│   └── community_graph.png

├── src/

│   ├── main.py

│   ├── graph.py

│   ├── community.py

│   ├── visualization.py

│   ├── parallel.py

│   └── __init__.py

├── tests/

├── venv/

├── README.md

└── .gitignore

## 5. Working

The project works in the following steps:

1. Create the social network graph.
2. Add users and their connections.
3. Analyze the graph.
4. Detect communities using the greedy modularity method.
5. Process nodes using parallel processing.
6. Generate a graph visualization.
7. Save the visualization in the results folder.

## 6. Community Detection

The project uses NetworkX's greedy modularity community detection algorithm.

The sample network contains 7 users and 9 connections.

The detected communities are displayed in the terminal.

## 7. Parallel Processing

ThreadPoolExecutor is used to process multiple nodes using multiple worker threads.

This demonstrates the use of parallel processing in the project.

## 8. Output

The program displays:

- Number of users
- Number of connections
- Detected communities
- Parallel processing results

A graph visualization is also generated and saved as:

results/community_graph.png

## 9. How to Run

Activate the virtual environment and run:

python src\main.py

## 10. Conclusion

This project demonstrates how graph-based techniques can be used to identify communities in a social network.

It also demonstrates graph visualization and parallel processing using Python.
