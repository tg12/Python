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



from itertools import accumulate
from bisect import bisect


def fracKnapsack(vl, wt, W, n):
    """
    >>> fracKnapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    """

    r = list(sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True))
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    k = bisect(acc, W)
    return (
        0
        if k == 0
        else sum(vl[:k]) + (W - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
