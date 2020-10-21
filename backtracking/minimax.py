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

""" Minimax helps to achieve maximum score in a game by checking all possible moves
    depth is current depth in game tree.
    nodeIndex is index of current node in scores[].
    if move is of maximizer return true else false
    leaves of game tree is stored in scores[]
    height is maximum height of Game tree
"""


def minimax(Depth, nodeIndex, isMax, scores, height):

    if Depth == height:
        return scores[nodeIndex]

    if isMax:
        return max(
            minimax(Depth + 1, nodeIndex * 2, False, scores, height),
            minimax(Depth + 1, nodeIndex * 2 + 1, False, scores, height),
        )
    return min(
        minimax(Depth + 1, nodeIndex * 2, True, scores, height),
        minimax(Depth + 1, nodeIndex * 2 + 1, True, scores, height),
    )


if __name__ == "__main__":

    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)

    print("Optimal value : ", end="")
    print(minimax(0, 0, True, scores, height))
