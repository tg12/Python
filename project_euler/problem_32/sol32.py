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
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
import itertools


def isCombinationValid(combination):
    """
    Checks if a combination (a tuple of 9 digits)
    is a valid product equation.

    >>> isCombinationValid(('3', '9', '1', '8', '6', '7', '2', '5', '4'))
    True

    >>> isCombinationValid(('1', '2', '3', '4', '5', '6', '7', '8', '9'))
    False

    """
    return (
        int("".join(combination[0:2])) * int("".join(combination[2:5]))
        == int("".join(combination[5:9]))
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5]))
        == int("".join(combination[5:9]))
    )


def solution():
    """
    Finds the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital

    >>> solution()
    45228
    """

    return sum(
        set(
            [
                int("".join(pandigital[5:9]))
                for pandigital in itertools.permutations("123456789")
                if isCombinationValid(pandigital)
            ]
        )
    )


if __name__ == "__main__":
    print(solution())
