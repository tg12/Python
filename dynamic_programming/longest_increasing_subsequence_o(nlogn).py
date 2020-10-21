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



#############################
# Author: Aravind Kashyap
# File: lis.py
# comments: This programme outputs the Longest Strictly Increasing Subsequence in O(NLogN)
#           Where N is the Number of elements in the list
#############################


def CeilIndex(v, l, r, key):
    while r - l > 1:
        m = (l + r) / 2
        if v[m] >= key:
            r = m
        else:
            l = m

    return r


def LongestIncreasingSubsequenceLength(v):
    if len(v) == 0:
        return 0

    tail = [0] * len(v)
    length = 1

    tail[0] = v[0]

    for i in range(1, len(v)):
        if v[i] < tail[0]:
            tail[0] = v[i]
        elif v[i] > tail[length - 1]:
            tail[length] = v[i]
            length += 1
        else:
            tail[CeilIndex(tail, -1, length - 1, v[i])] = v[i]

    return length


if __name__ == "__main__":
    v = [2, 5, 3, 7, 11, 8, 10, 13, 6]
    print(LongestIncreasingSubsequenceLength(v))
