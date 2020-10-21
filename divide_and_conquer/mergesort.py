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



def merge(a, b, m, e):
    l = a[b:m + 1]
    r = a[m + 1:e + 1]
    k = b
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        # change sign for Descending order
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1
    return a


def mergesort(a, b, e):
    """
    >>> mergesort([3,2,1],0,2)
    [1, 2, 3]
    >>> mergesort([3,2,1,0,1,2,3,5,4],0,8)
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    """
    if b < e:
        m = (b + e) // 2
        # print("ms1",a,b,m)
        mergesort(a, b, m)
        # print("ms2",a,m+1,e)
        mergesort(a, m + 1, e)
        # print("m",a,b,m,e)
        merge(a, b, m, e)
        return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()
