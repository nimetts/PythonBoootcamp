# 🚇 Metro Network and Pathfinding Algorithm

This project models a metro network and implements pathfinding algorithms to find the optimal routes between stations. The system offers two primary algorithms:
- **Breadth-First Search (BFS)** for finding the route with the least number of transfers.
- **A* Algorithm** for finding the fastest route based on travel time.

Additionally, the project visualizes the metro network and highlights the paths found by these algorithms using the `matplotlib` and `networkx` libraries.

## 📋 Features
- **Metro Network Representation**: The metro network consists of stations connected by bidirectional links with a specified travel time and distance.
- **Pathfinding Algorithms**:
  - **BFS**: Finds the path with the minimum number of transfers (nodes).
  - **A\* Algorithm**: Finds the fastest route based on travel time, considering a heuristic function.
- **Visualization**: The network is visualized using `networkx` and `matplotlib`, with routes highlighted for easy comparison.

## 🧑‍💻 Requirements
- Python 3.x
- `heapq` (for A* algorithm)
- `deque` (for BFS algorithm)
- `matplotlib` (for visualizing the network)
- `networkx` (for creating and handling the graph)

You can install the required libraries using the following command:

```bash
pip install matplotlib networkx
```

## 🏗️ Classes and Functions

### 1. `Istasyon` Class
Represents a metro station.

- `__init__(self, isim)`: Initializes the station with a name.
- `__str__(self)`: Returns the station name.
- `__repr__(self)`: Returns the station name for easier display.

### 2. `MetroAgi` Class
Represents the entire metro network and includes methods for adding stations, connecting them, and performing pathfinding.

#### Methods:
- `istasyon_ekle(self, isim)`: Adds a station to the network if it doesn't already exist.
- `baglantı_ekle(self, isim1, isim2, sure, mesafe)`: Adds a bidirectional connection between two stations with a specified travel time (`sure`) and distance (`mesafe`).
- `en_az_aktarma_bul(self, baslangic_isim, bitis_isim)`: Uses BFS to find the path with the least number of transfers from the start station (`baslangic_isim`) to the destination station (`bitis_isim`).
- `en_hizli_rota_bul(self, baslangic_isim, bitis_isim)`: Uses the A* algorithm to find the fastest route from the start station (`baslangic_isim`) to the destination station (`bitis_isim`).
- `gorsellestir(self, en_az_aktarma, en_hizli_rota)`: Visualizes the metro network using `matplotlib` and `networkx`, highlighting the least-transfer path (`en_az_aktarma`) and the fastest path (`en_hizli_rota`).

## 🚀 Example Usage

### Step 1: Create a Metro Network
```python
metro_agi = MetroAgi()

# Add connections between stations
metro_agi.baglantı_ekle('A', 'B', 2, 5)
metro_agi.baglantı_ekle('B', 'C', 3, 10)
metro_agi.baglantı_ekle('A', 'C', 7, 20)
metro_agi.baglantı_ekle('C', 'D', 1, 2)
metro_agi.baglantı_ekle('B', 'D', 5, 15)
```

### Step 2: Find the Optimal Routes
```python
# Find the least-transfer path using BFS
en_az_aktarma = metro_agi.en_az_aktarma_bul('A', 'D')
print("En Az Aktarmalı Rota (BFS):", en_az_aktarma)

# Find the fastest path using A*
en_hizli_rota = metro_agi.en_hizli_rota_bul('A', 'D')
print("En Hızlı Rota (A*):", en_hizli_rota)
```

### Step 3: Visualize the Network
```python
# Visualize the metro network with highlighted paths
metro_agi.gorsellestir(en_az_aktarma, en_hizli_rota)
```

## 📊 Example Output

1. **BFS Route (Least Transfers)**: The console will display the path with the fewest number of transfers.
   ```text
   En Az Aktarmalı Rota (BFS): ['A', 'B', 'D']
   ```

2. **A* Route (Fastest Path)**: The console will display the path with the shortest travel time.
   ```text
   En Hızlı Rota (A*): ['A', 'C', 'D']
   ```

3. **Visualization**: The metro network will be visualized, with the least-transfer path shown in green and the fastest path shown in red.

## 🧠 Explanation of the Algorithms

### BFS (Breadth-First Search)
BFS is used to find the shortest path in terms of the number of nodes (stations). It explores all neighboring nodes level by level, ensuring that the first time it reaches the destination station, it has found the least number of transfers.

### A* Algorithm
The A* algorithm is used to find the path that minimizes the total travel time. It combines the actual cost from the start station (`g_value`) and a heuristic estimate to the destination station (`f_value`). In this example, the heuristic is set to zero, meaning that the algorithm only considers travel time.

## 🔧 Future Improvements
- **Heuristic Function for A***: Implement a more sophisticated heuristic based on real-world distances or estimated times.
- **User Interface**: Add a GUI to interact with the metro network and visualize the results in real-time.
- **Error Handling**: Improve the robustness of the code by handling edge cases, such as no available path between stations.
