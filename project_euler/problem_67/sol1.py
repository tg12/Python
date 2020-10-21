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
Problem Statement:
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.
"""
import os


def solution():
    """
    Finds the maximum total in a triangle as described by the problem statement
    above.

    >>> solution()
    7273
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")

    with open(triangle, "r") as f:
        triangle = f.readlines()

    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle)
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a))

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if j != len(a[i - 1]):
                number1 = a[i - 1][j]
            else:
                number1 = 0
            if j > 0:
                number2 = a[i - 1][j - 1]
            else:
                number2 = 0
            a[i][j] += max(number1, number2)
    return max(a[-1])


if __name__ == "__main__":
    print(solution())
