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



#!/usr/bin/python
# encoding=utf8

"""
This program calculates the nth Fibonacci number in O(log(n)).
It's possible to calculate F(1000000) in less than a second.
"""
import sys


# returns F(n)
def fibonacci(n: int):  # noqa: E999 This syntax is Python 3 only
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _fib(n)[0]


# returns (F(n), F(n-1))
def _fib(n: int):  # noqa: E999 This syntax is Python 3 only
    if n == 0:
        # (F(0), F(1))
        return (0, 1)
    else:
        # F(2n) = F(n)[2F(n+1) − F(n)]
        # F(2n+1) = F(n+1)^2+F(n)^2
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Too few or too much parameters given.")
        exit(1)
    try:
        n = int(args[0])
    except ValueError:
        print("Could not convert data to an integer.")
        exit(1)
    print("F(%d) = %d" % (n, fibonacci(n)))
