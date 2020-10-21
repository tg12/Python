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



# Eulerian Path is a path in graph that visits every edge exactly once.
# Eulerian Circuit is an Eulerian Path which starts and ends on the same
# vertex.
# time complexity is O(V+E)
# space complexity is O(VE)


# using dfs for finding eulerian path traversal
def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    for v in graph[u]:
        if not visited_edge[u][v]:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path


# for checking in graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)]
                    for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)


def main():
    G1 = {1: [2, 3, 4], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [4]}
    G2 = {1: [2, 3, 4, 5], 2: [1, 3], 3: [1, 2], 4: [1, 5], 5: [1, 4]}
    G3 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2, 5], 5: [4]}
    G4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    G5 = {
        1: [],
        2: []
        # all degree is zero
    }
    max_node = 10
    check_euler(G1, max_node)
    check_euler(G2, max_node)
    check_euler(G3, max_node)
    check_euler(G4, max_node)
    check_euler(G5, max_node)


if __name__ == "__main__":
    main()
