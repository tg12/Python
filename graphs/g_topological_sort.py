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



# Author: Phyllipe Bezerra (https://github.com/pmba)

clothes = {
    0: "underwear",
    1: "pants",
    2: "belt",
    3: "suit",
    4: "shoe",
    5: "socks",
    6: "shirt",
    7: "tie",
    8: "clock",
}

graph = [[1, 4], [2, 4], [3], [], [], [4], [2, 7], [3], []]

visited = [0 for x in range(len(graph))]
stack = []


def print_stack(stack, clothes):
    order = 1
    while stack:
        cur_clothe = stack.pop()
        print(order, clothes[cur_clothe])
        order += 1


def dfs(u, visited, graph):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v, visited, graph)

    stack.append(u)


def top_sort(graph, visited):
    for v in range(len(graph)):
        if not visited[v]:
            dfs(v, visited, graph)


if __name__ == "__main__":
    top_sort(graph, visited)
    print(stack)
    print_stack(stack, clothes)
