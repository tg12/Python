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



# -*- coding: utf-8 -*-
"""
        In mathematics, the Lucas–Lehmer test (LLT) is a primality test for Mersenne numbers.
        https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test

        A Mersenne number is a number that is one less than a power of two.
        That is M_p = 2^p - 1
        https://en.wikipedia.org/wiki/Mersenne_prime

        The Lucas–Lehmer test is the primality test used by the
        Great Internet Mersenne Prime Search (GIMPS) to locate large primes.
"""


# Primality test 2^p - 1
# Return true if 2^p - 1 is prime
def lucas_lehmer_test(p: int) -> bool:
    """
    >>> lucas_lehmer_test(p=7)
    True

    >>> lucas_lehmer_test(p=11)
    False

    # M_11 = 2^11 - 1 = 2047 = 23 * 89
    """

    if p < 2:
        raise ValueError("p should not be less than 2!")
    elif p == 2:
        return True

    s = 4
    M = (1 << p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    return s == 0


if __name__ == "__main__":
    print(lucas_lehmer_test(7))
    print(lucas_lehmer_test(11))
