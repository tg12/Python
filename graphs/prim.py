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



"""
Prim's Algorithm.

Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm

Create a list to store x the vertices.
G = [vertex(n) for n in range(x)]

For each vertex in G, add the neighbors:
G[x].addNeighbor(G[y])
G[y].addNeighbor(G[x])

For each vertex in G, add the edges:
G[x].addEdge(G[y], w)
G[y].addEdge(G[x], w)

To solve run:
MST = prim(G, G[0])
"""

import math


class vertex:
    """Class Vertex."""

    def __init__(self, id):
        """
        Arguments:
            id - input an id to identify the vertex
        Attributes:
            neighbors - a list of the vertices it is linked to
            edges     - a dict to store the edges's weight
        """
        self.id = str(id)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # [vertex:distance]

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return self.key < other.key

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def addNeighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def addEdge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def prim(graph, root):
    """
    Prim's Algorithm.
    Return a list with the edges of a Minimum Spanning Tree
    prim(graph, graph[0])
    """
    A = []
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    Q = graph[:]
    while Q:
        u = min(Q)
        Q.remove(u)
        for v in u.neighbors:
            if (v in Q) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
    for i in range(1, len(graph)):
        A.append([graph[i].id, graph[i].pi.id])
    return A
