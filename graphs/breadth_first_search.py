'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



#!/usr/bin/python
# encoding=utf8

""" Author: OMKAR PATHAK """


class Graph:
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        # Take a list for stoting already visited vertexes
        visited = [False] * len(self.vertex)

        # create a list to store all the vertexes for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            startVertex = queue.pop(0)
            print(startVertex, end=" ")

            # mark all adjacent nodes as visited and print them
            for i in self.vertex[startVertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print("BFS:")
    g.BFS(2)

    # OUTPUT:
    # 0  ->  1 -> 2
    # 1  ->  2
    # 2  ->  0 -> 3
    # 3  ->  3
    # BFS:
    # 2 0 3 1
