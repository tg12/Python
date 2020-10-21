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
Author: https://github.com/bhushan-borole
"""
"""
The input graph for the algorithm is:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

graph = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]


class Node:
    def __init__(self, name):
        self.name = name
        self.inbound = []
        self.outbound = []

    def add_inbound(self, node):
        self.inbound.append(node)

    def add_outbound(self, node):
        self.outbound.append(node)

    def __repr__(self):
        return "Node {}: Inbound: {} ; Outbound: {}".format(
            self.name, self.inbound, self.outbound
        )


def page_rank(nodes, limit=3, d=0.85):
    ranks = {}
    for node in nodes:
        ranks[node.name] = 1

    outbounds = {}
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    for i in range(limit):
        print("======= Iteration {} =======".format(i + 1))
        for j, node in enumerate(nodes):
            ranks[node.name] = (1 - d) + d * sum(
                [ranks[ib] / outbounds[ib] for ib in node.inbound]
            )
        print(ranks)


def main():
    names = list(input("Enter Names of the Nodes: ").split())

    nodes = [Node(name) for name in names]

    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(names[ri])
                nodes[ri].add_outbound(names[ci])

    print("======= Nodes =======")
    for node in nodes:
        print(node)

    page_rank(nodes)


if __name__ == "__main__":
    main()
