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
The number of partitions of a number n into at least k parts equals the number of partitions into exactly k parts
plus the number of partitions into at least k-1 parts. Subtracting 1 from each part of a partition of n into k parts
gives a partition of n-k into k parts. These two facts together are used for this algorithm.
"""


def partition(m):
    memo = [[0 for _ in range(m)] for _ in range(m + 1)]
    for i in range(m + 1):
        memo[i][0] = 1

    for n in range(m + 1):
        for k in range(1, m):
            memo[n][k] += memo[n][k - 1]
            if n - k > 0:
                memo[n][k] += memo[n - k - 1][k]

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Enter a number: ").strip())
            print(partition(n))
        except ValueError:
            print("Please enter a number.")
    else:
        try:
            n = int(sys.argv[1])
            print(partition(n))
        except ValueError:
            print("Please pass a number.")
