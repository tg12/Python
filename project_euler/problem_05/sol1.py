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
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible(divisible with no
remainder) by all of the numbers from 1 to N?
"""


def solution(n):
    """Returns the smallest positive number that is evenly divisible(divisible
    with no remainder) by all of the numbers from 1 to n.

    >>> solution(10)
    2520
    >>> solution(15)
    360360
    >>> solution(20)
    232792560
    >>> solution(22)
    232792560
    >>> solution(3.4)
    6
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
    i = 0
    while True:
        i += n * (n - 1)
        nfound = 0
        for j in range(2, n):
            if i % j != 0:
                nfound = 1
                break
        if nfound == 0:
            if i == 0:
                i = 1
            return i


if __name__ == "__main__":
    print(solution(int(input().strip())))
