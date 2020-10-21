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



def isSumSubset(arr, arrLen, requiredSum):
    """
    >>> isSumSubset([2, 4, 6, 8], 4, 5)
    False
    >>> isSumSubset([2, 4, 6, 8], 4, 14)
    True
    """
    # a subset value says 1 if that subset sum can be formed else 0
    # initially no subsets can be formed hence False/0
    subset = [[False for i in range(requiredSum + 1)]
              for i in range(arrLen + 1)]

    # for each arr value, a sum of zero(0) can be formed by not taking any
    # element hence True/1
    for i in range(arrLen + 1):
        subset[i][0] = True

    # sum is not zero and set is empty then false
    for i in range(1, requiredSum + 1):
        subset[0][i] = False

    for i in range(1, arrLen + 1):
        for j in range(1, requiredSum + 1):
            if arr[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            if arr[i - 1] <= j:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - arr[i - 1]]

    # uncomment to print the subset
    # for i in range(arrLen+1):
    #     print(subset[i])
    print(subset[arrLen][requiredSum])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
