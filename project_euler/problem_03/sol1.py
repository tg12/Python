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
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor
of a given number N?

e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
"""
import math


def isprime(no):
    if no == 2:
        return True
    elif no % 2 == 0:
        return False
    sq = int(math.sqrt(no)) + 1
    for i in range(3, sq, 2):
        if no % i == 0:
            return False
    return True


def solution(n):
    """Returns the largest prime factor of a given number n.

    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    >>> solution(3.4)
    3
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
    maxNumber = 0
    if isprime(n):
        return n
    else:
        while n % 2 == 0:
            n = n / 2
        if isprime(n):
            return int(n)
        else:
            n1 = int(math.sqrt(n)) + 1
            for i in range(3, n1, 2):
                if n % i == 0:
                    if isprime(n / i):
                        maxNumber = n / i
                        break
                    elif isprime(i):
                        maxNumber = i
            return maxNumber


if __name__ == "__main__":
    print(solution(int(input().strip())))
