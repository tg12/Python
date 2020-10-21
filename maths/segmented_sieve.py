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



"""Segmented Sieve."""

import math


def sieve(n):
    """Segmented Sieve."""
    in_prime = []
    start = 2
    end = int(math.sqrt(n))  # Size of every segment
    temp = [True] * (end + 1)
    prime = []

    while start <= end:
        if temp[start] is True:
            in_prime.append(start)
            for i in range(start * start, end + 1, start):
                if temp[i] is True:
                    temp[i] = False
        start += 1
    prime += in_prime

    low = end + 1
    high = low + end - 1
    if high > n:
        high = n

    while low <= n:
        temp = [True] * (high - low + 1)
        for each in in_prime:

            t = math.floor(low / each) * each
            if t < low:
                t += each

            for j in range(t, high + 1, each):
                temp[j - low] = False

        for j in range(len(temp)):
            if temp[j] is True:
                prime.append(j + low)

        low = high + 1
        high = low + end - 1
        if high > n:
            high = n

    return prime


print(sieve(10 ** 6))
