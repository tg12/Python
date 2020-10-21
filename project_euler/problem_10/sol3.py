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
https://projecteuler.net/problem=10

Problem Statement:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million using Sieve_of_Eratosthenes:

The sieve of Eratosthenes is one of the most efficient ways to find all primes
smaller than n when n is smaller than 10 million.  Only for positive numbers.
"""


def prime_sum(n: int) -> int:
    """ Returns the sum of all the primes below n.

    >>> prime_sum(2_000_000)
    142913828922
    >>> prime_sum(1_000)
    76127
    >>> prime_sum(5_000)
    1548136
    >>> prime_sum(10_000)
    5736396
    >>> prime_sum(7)
    10
    >>> prime_sum(7.1)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> prime_sum(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    IndexError: list assignment index out of range
    >>> prime_sum("seven")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    """
    list_ = [0 for i in range(n + 1)]
    list_[0] = 1
    list_[1] = 1

    for i in range(2, int(n ** 0.5) + 1):
        if list_[i] == 0:
            for j in range(i * i, n + 1, i):
                list_[j] = 1
    s = 0
    for i in range(n):
        if list_[i] == 0:
            s += i
    return s


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(prime_sum(int(input().strip())))
