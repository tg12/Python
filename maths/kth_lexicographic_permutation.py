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



def kthPermutation(k, n):
    """
        Finds k'th lexicographic permutation (in increasing order) of
        0,1,2,...n-1 in O(n^2) time.

        Examples:
        First permutation is always 0,1,2,...n
        >>> kthPermutation(0,5)
        [0, 1, 2, 3, 4]

        The order of permutation of 0,1,2,3 is [0,1,2,3], [0,1,3,2], [0,2,1,3],
        [0,2,3,1], [0,3,1,2], [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3],
        [1,2,3,0], [1,3,0,2]
        >>> kthPermutation(10,4)
        [1, 3, 0, 2]
    """
    # Factorails from 1! to (n-1)!
    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)
    assert 0 <= k < factorials[-1] * n, "k out of bounds"

    permutation = []
    elements = list(range(n))

    # Find permutation
    while factorials:
        factorial = factorials.pop()
        number, k = divmod(k, factorial)
        permutation.append(elements[number])
        elements.remove(elements[number])
    permutation.append(elements[0])

    return permutation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
