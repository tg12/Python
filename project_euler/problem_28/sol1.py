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
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

from math import ceil


def diagonal_sum(n):
    """Returns the sum of the numbers on the diagonals in a n by n spiral
    formed in the same way.

    >>> diagonal_sum(1001)
    669171001
    >>> diagonal_sum(500)
    82959497
    >>> diagonal_sum(100)
    651897
    >>> diagonal_sum(50)
    79697
    >>> diagonal_sum(10)
    537
    """
    total = 1

    for i in range(1, int(ceil(n / 2.0))):
        odd = 2 * i + 1
        even = 2 * i
        total = total + 4 * odd ** 2 - 6 * even

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(diagonal_sum(1001))
    else:
        try:
            n = int(sys.argv[1])
            print(diagonal_sum(n))
        except ValueError:
            print("Invalid entry - please enter a number")
