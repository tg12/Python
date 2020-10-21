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
You are given a tree(a simple connected graph with no cycles). The tree has N
nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest
such that each connected component of the forest contains an even number of
nodes.

Constraints
2 <= 2 <= 100

Note: The tree input will be such that it can always be decomposed into
components containing an even number of nodes.
"""
# pylint: disable=invalid-name
from collections import defaultdict


def dfs(start):
    """DFS traversal"""
    # pylint: disable=redefined-outer-name
    ret = 1
    visited[start] = True
    for v in tree.get(start):
        if v not in visited:
            ret += dfs(v)
    if ret % 2 == 0:
        cuts.append(start)
    return ret


def even_tree():
    """
    2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8
    On removing edges (1,3) and (1,6), we can get the desired result 2.
    """
    dfs(1)


if __name__ == "__main__":
    n, m = 10, 9
    tree = defaultdict(list)
    visited = {}
    cuts = []
    count = 0
    edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1),
             (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    even_tree()
    print(len(cuts) - 1)
