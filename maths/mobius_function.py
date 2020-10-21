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
Refrences: https://en.wikipedia.org/wiki/M%C3%B6bius_function
References: wikipedia:square free number
python/black : True
flake8 : True
"""

from maths.prime_factors import prime_factors
from maths.is_square_free import is_square_free


def mobius(n: int) -> int:
    """
    Mobius function
    >>> mobius(24)
    0
    >>> mobius(-1)
    1
    >>> mobius('asd')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> mobius(10**400)
    0
    >>> mobius(10**-400)
    1
    >>> mobius(-1424)
    1
    >>> mobius([1, '2', 2.0])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    """
    factors = prime_factors(n)
    if is_square_free(factors):
        return -1 if len(factors) % 2 else 1
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
