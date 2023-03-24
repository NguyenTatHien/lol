import math
class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost
    def __str__(self):
        return f'[{self.u}, {self.v}, {self.cost}]'
    
class Graph:
    def __init__(self, fileName):
        self.directed = False
        self.edgeList = None
        self.verticesList = None
        self.__readGraph(fileName)

    def __readGraph(self, fileName):
        f = open(fileName)
        self.directed = f.readline().strip() == "1"
        edgesList = f.readline()
        f.close()
        self.edgesList = []
        verticesList = set()
        for edge in edgesList:
            edge = edge.strip()
            e = edge.split()
            if len(e) != 3:
                continue
            verticesList.add(e[0])
            verticesList.add(e[1])
            self.edgesList.append(Edge(e[0], e[1], int(e[2])))
        self.verticesList = list(verticesList)
        self.verticesList.sort()

    def __getWeightMatrix(self):
        n = len(self.verticesList)
        maxtrix = [[0 if i == j else math.inf for i in range(n)] for j in range(n)]
        for e in self.edgesList(e.u):
            row = self.__getIndex(e.u)
            col = self.__getIndex(e.v)
            if self.directed:
                maxtrix[row][col] = e.cost
            else:
                maxtrix[row][col] = maxtrix[col][row] = e.cost
        return maxtrix

    def __getIndex(self, u):
        return self.verticesList.index(u)

    def _isConnectedVertex(self, matrix, u, v):
        i = self.__getIndex(u)
        j = self.__getIndex(v)
        return matrix[i][j]

    def __getCost(self, matrix, u, v):
        i = self.__getIndex(u)
        j = self.__getIndex(v)
        return matrix[i][j]

    def __Dijkstra(self, u):
        if not (u in self.verticesList):
            return None, None
        distance = {k: math.inf for k in self.verticesList}
        predecessor = {k: None for k in self.verticesList}
        distance[u] = 0
        T = self.verticesList.copy()
        maxtrix = self.__getWeightMatrix()
        while len(T) > 0:
            u_min = min(T, key = distance.get)
            for v in self.verticesList:
                if u != v and self.__isConnectedVertex(maxtrix, u_min, v):
                    sum = distance[u_min] + self.__getCost(maxtrix, u_min, v)
                    if distance[u_min] != math.inf and distance[v] > sum:
                        distance[v] = sum
                        predecessor[v] = u_min
            T.remove(u_min)
        return distance, predecessor

    def __findPath(self, predecessor, u , v):
        verticesList = [v]
        while True:
            v = predecessor[v]
            if v is None:
                break;
            verticesList.insert(0, v)
        return '->'.join(verticesList)

    def Dijkstra(self, u):
        distance, predecessor = self.__Dijkstra(u)
        if distance is None:
            return False
        verticesList = self.verticesList.copy()
        verticesList.remove(u)
        for v in verticesList:
            print(self.__findPath(predecessor, u, v) + ": " + str(distance[v]))

def main():
    g = Graph("C:\\CODE\\Nam2_HK1\\Cau_Truc_Du_Lieu_Giai_Thuat\\graph.txt")
    g.Dijkstra('0')

if __name__ == "__main__":
    main()