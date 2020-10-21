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



def dfs(u):
    global g, r, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    for v in g[u]:
        dfs(v)
    stack.append(u)


def dfs2(u):
    global g, r, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    component.append(u)
    for v in r[u]:
        dfs2(v)


def kosaraju():
    global g, r, scc, component, visit, stack
    for i in range(n):
        dfs(i)
    visit = [False] * n
    for i in stack[::-1]:
        if visit[i]:
            continue
        component = []
        dfs2(i)
        scc.append(component)
    return scc


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int, input().strip().split()))

    g = [[] for i in range(n)]  # graph
    r = [[] for i in range(n)]  # reversed graph
    # input graph data (edges)
    for i in range(m):
        u, v = list(map(int, input().strip().split()))
        g[u].append(v)
        r[v].append(u)

    stack = []
    visit = [False] * n
    scc = []
    component = []
    print(kosaraju())
