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
Sieve of Eratosthones

The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or equal to a given value.
Illustration: https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks Dmitry (https://github.com/LizardWizzard) for finding the problem
"""


import math


def sieve(n):
    """
    Returns a list with all prime numbers up to n.

    >>> sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> sieve(10)
    [2, 3, 5, 7]
    >>> sieve(9)
    [2, 3, 5, 7]
    >>> sieve(2)
    [2]
    >>> sieve(1)
    []
    """

    l = [True] * (n + 1)
    prime = []
    start = 2
    end = int(math.sqrt(n))

    while start <= end:
        # If start is a prime
        if l[start] is True:
            prime.append(start)

            # Set multiples of start be False
            for i in range(start * start, n + 1, start):
                if l[i] is True:
                    l[i] = False

        start += 1

    for j in range(end + 1, n + 1):
        if l[j] is True:
            prime.append(j)

    return prime


if __name__ == "__main__":
    print(sieve(int(input("Enter n: ").strip())))
