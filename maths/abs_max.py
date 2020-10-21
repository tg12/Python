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



from typing import List


def abs_max(x: List[int]) -> int:
    """
    >>> abs_max([0,5,1,11])
    11
    >>> abs_max([3,-10,-2])
    -10
    """
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def abs_max_sort(x):
    """
    >>> abs_max_sort([0,5,1,11])
    11
    >>> abs_max_sort([3,-10,-2])
    -10
    """
    return sorted(x, key=abs)[-1]


def main():
    a = [1, 2, -11]
    assert abs_max(a) == -11
    assert abs_max_sort(a) == -11


if __name__ == "__main__":
    main()
