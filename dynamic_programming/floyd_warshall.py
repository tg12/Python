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



import math


class Graph:
    def __init__(self, N=0):  # a graph with Node 0,1,...,N-1
        self.N = N
        self.W = [
            [math.inf for j in range(0, N)] for i in range(0, N)
        ]  # adjacency matrix for weight
        self.dp = [
            [math.inf for j in range(0, N)] for i in range(0, N)
        ]  # dp[i][j] stores minimum distance from i to j

    def addEdge(self, u, v, w):
        self.dp[u][v] = w

    def floyd_warshall(self):
        for k in range(0, self.N):
            for i in range(0, self.N):
                for j in range(0, self.N):
                    self.dp[i][j] = min(
                        self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def showMin(self, u, v):
        return self.dp[u][v]


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0, 2, 9)
    graph.addEdge(0, 4, 10)
    graph.addEdge(1, 3, 5)
    graph.addEdge(2, 3, 7)
    graph.addEdge(3, 0, 10)
    graph.addEdge(3, 1, 2)
    graph.addEdge(3, 2, 1)
    graph.addEdge(3, 4, 6)
    graph.addEdge(4, 1, 3)
    graph.addEdge(4, 2, 4)
    graph.addEdge(4, 3, 9)
    graph.floyd_warshall()
    graph.showMin(1, 4)
    graph.showMin(0, 3)
