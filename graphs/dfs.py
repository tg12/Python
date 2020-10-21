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



"""pseudo-code"""

"""
DFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
for every edge (s, v):
    if v unexplored:
        DFS(G, v)
"""


def dfs(graph, start):
    """The DFS function simply calls itself recursively for every unvisited child of its argument. We can emulate that
     behaviour precisely using a stack of iterators. Instead of recursively calling with a node, we'll push an iterator
      to the node's children onto the iterator stack. When the iterator at the top of the stack terminates, we'll pop
       it off the stack."""
    explored, stack = set(), [start]
    while stack:
        # one difference from BFS is to pop last element here instead of first
        # one
        v = (stack.pop())

        if v in explored:
            continue

        explored.add(v)

        for w in graph[v]:
            if w not in explored:
                stack.append(w)
    return explored


G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs(G, "A"))
