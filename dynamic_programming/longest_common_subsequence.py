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
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


def longest_common_subsequence(x: str, y: str):
    """
    Finds the longest common subsequence between two strings. Also returns the
    The subsequence found

    Parameters
    ----------

    x: str, one of the strings
    y: str, the other string

    Returns
    -------
    L[m][n]: int, the length of the longest subsequence. Also equal to len(seq)
    Seq: str, the subsequence found

    >>> longest_common_subsequence("programming", "gaming")
    (6, 'gaming')
    >>> longest_common_subsequence("physics", "smartphone")
    (2, 'ph')
    >>> longest_common_subsequence("computer", "food")
    (1, 'o')
    """
    # find the length of strings

    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                match = 1
            else:
                match = 0

            L[i][j] = max(L[i - 1][j], L[i][j - 1], L[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            match = 1
        else:
            match = 0

        if L[i][j] == L[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif L[i][j] == L[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return L[m][n], seq


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_ln = 4
    expected_subseq = "GTAB"

    ln, subseq = longest_common_subsequence(a, b)
##    print("len =", ln, ", sub-sequence =", subseq)
    import doctest

    doctest.testmod()
