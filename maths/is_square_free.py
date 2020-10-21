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
References: wikipedia:square free number
python/black : True
flake8 : True
"""
from typing import List


def is_square_free(factors: List[int]) -> bool:
    """
    # doctest: +NORMALIZE_WHITESPACE
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.
    >>> is_square_free([1, 1, 2, 3, 4])
    False

    These are wrong but should return some value
    it simply checks for repition in the numbers.
    >>> is_square_free([1, 3, 4, 'sd', 0.0])
    True

    >>> is_square_free([1, 0.5, 2, 0.0])
    True
    >>> is_square_free([1, 2, 2, 5])
    False
    >>> is_square_free('asd')
    True
    >>> is_square_free(24)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return len(set(factors)) == len(factors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
