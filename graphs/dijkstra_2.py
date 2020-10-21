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



def printDist(dist, V):
    print("\nVertex Distance")
    for i in range(V):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()


def minDist(mdist, vset, V):
    minVal = float("inf")
    minInd = -1
    for i in range(V):
        if (not vset[i]) and mdist[i] < minVal:
            minInd = i
            minVal = mdist[i]
    return minInd


def Dijkstra(graph, V, src):
    mdist = [float("inf") for i in range(V)]
    vset = [False for i in range(V)]
    mdist[src] = 0.0

    for i in range(V - 1):
        u = minDist(mdist, vset, V)
        vset[u] = True

        for v in range(V):
            if (
                (not vset[v])
                and graph[u][v] != float("inf")
                and mdist[u] + graph[u][v] < mdist[v]
            ):
                mdist[v] = mdist[u] + graph[u][v]

    printDist(mdist, V)


if __name__ == "__main__":
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter shortest path source:").strip())
    Dijkstra(graph, V, gsrc)
