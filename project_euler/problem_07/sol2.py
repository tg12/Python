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
By listing the first six prime numbers:

    2, 3, 5, 7, 11, and 13

We can see that the 6th prime is 13. What is the Nth prime number?
"""


def isprime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(n):
    """Returns the n-th prime number.

    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    >>> solution(3.4)
    5
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    """
    try:
        n = int(n)
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater or equal to one.")
    primes = []
    num = 2
    while len(primes) < n:
        if isprime(num):
            primes.append(num)
            num += 1
        else:
            num += 1
    return primes[len(primes) - 1]


if __name__ == "__main__":
    print(solution(int(input().strip())))
