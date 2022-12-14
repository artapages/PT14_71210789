class Node: 
    def __init__(self,name, value):
        self._name = name 
        self._value = value

class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, name, value):
        node = Node(name, value)
        if name not in self._data.keys():
            setEdge = set()
            listData = [setEdge, node]
            self._data[name] = listData

    def vertex(self):
        print("== Seluruh Node == ")
        for key in self._data.keys():
            print(key,':',self._data[f"{key}"][1]._value)
        print()

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x][0].add(y)
            self._data[y][0].add(x)
        print()

    def edge(self):
        print("== Seluruh Edge == ")
        listEdge = set()
        for key in self._data.keys():
            item = list(self._data[f'{key}'][0])
            for i in range(len(item)):
                if key+item[i] not in listEdge and item[i]+key not in listEdge:
                    listEdge.add(key+item[i])
        listEdge1 = sorted(listEdge)
        for item in listEdge1:
            print(item, end=" ")
        print("\n")
    
    def bfs(self, node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        print('Traversing BFS =',end=' ')
        while queue:
            q = queue.pop(0) 
            print (q, end = " ") 
            for neighbour in self._data[q][0]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print("\n")

graph = Graph()
graph.addVertex("a", 2)
graph.addVertex("b", 2)
graph.addVertex("c", 4)
graph.addVertex("d", 3)
graph.addVertex("e", 4)
graph.addVertex("f", 3)
graph.addVertex("g", 3)
graph.addVertex("h", 3)

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('d', 'e')
graph.addEdge('f', 'h')
graph.addEdge('g', 'f')

graph.vertex()
graph.edge()

graph.bfs('a')