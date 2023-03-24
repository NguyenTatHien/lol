import math
import sys
class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]
    def inketqua(cung, L, a):
        print ("đỉnh nguồn xuất phát từ: ")
        for nut in range(cung.x):
            print (a," đến đỉnh ",nut, "độ dài đường đi là: ", L[nut])
    def duongdinhonhat(cung, L, P):
        min = sys.maxsize
        for x in range(cung.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x
        return min_index
    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x
        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            P[u] = True
            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + cung.graph[u][x]:
                    L[x] = L[u] + cung.graph[u][x]
        cung.inketqua(L, a)

g = Graph(8)
g.graph = [[0,6,0,0,0,5,0,0],
            [6,0,7,10,9,18,0,0],
            [0,7,0,1,0,11,0,0],
            [0,10,1,0,3,9,3,0],
            [0,9,0,3,0,0,6,7],
            [5,18,11,9,0,0,9,0],
            [0,0,0,3,6,9,0,14],
            [0,0,0,0,7,0,14,0]]
g.timduongdi(0)