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
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.
"""


def solution(array):
    """Returns the first ten digits of the sum of the array elements.

    >>> import os
    >>> sum = 0
    >>> array = []
    >>> with open(os.path.dirname(__file__) + "/num.txt","r") as f:
    ...     for line in f:
    ...         array.append(int(line))
    ...
    >>> solution(array)
    '5537376230'
    """
    return str(sum(array))[:10]


if __name__ == "__main__":
    n = int(input().strip())

    array = []
    for i in range(n):
        array.append(int(input().strip()))
    print(solution(array))
