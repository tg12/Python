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



# Finding Articulation Points in Undirected Graph
def computeAP(l):
    n = len(l)
    outEdgeCount = 0
    low = [0] * n
    visited = [False] * n
    isArt = [False] * n

    def dfs(root, at, parent, outEdgeCount):
        if parent == root:
            outEdgeCount += 1
        visited[at] = True
        low[at] = at

        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                outEdgeCount = dfs(root, to, at, outEdgeCount)
                low[at] = min(low[at], low[to])

                # AP found via bridge
                if at < low[to]:
                    isArt[at] = True
                # AP found via cycle
                if at == low[to]:
                    isArt[at] = True
            else:
                low[at] = min(low[at], to)
        return outEdgeCount

    for i in range(n):
        if not visited[i]:
            outEdgeCount = 0
            outEdgeCount = dfs(i, i, -1, outEdgeCount)
            isArt[i] = outEdgeCount > 1

    for x in range(len(isArt)):
        if isArt[x]:
            print(x)


# Adjacency list of graph
l = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
computeAP(l)
