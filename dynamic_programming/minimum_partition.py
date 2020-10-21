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
Partition a set into two subsets such that the difference of subset sums is minimum
"""


def findMin(arr):
    n = len(arr)
    s = sum(arr)

    dp = [[False for x in range(s + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = True

    for i in range(1, s + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i][j - 1]

            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    for j in range(int(s / 2), -1, -1):
        if dp[n][j]:
            diff = s - 2 * j
            break

    return diff
