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
    disjoint set
    Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class Node:
    def __init__(self, data):
        self.data = data


def make_set(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x


def union_set(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    raise ValueError(f"{node.data} is not in {sets}")


def test_disjoint_set():
    """
    >>> test_disjoint_set()
    """
    vertex = [Node(i) for i in range(6)]
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    for node0 in vertex:
        for node1 in vertex:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)


if __name__ == "__main__":
    test_disjoint_set()
