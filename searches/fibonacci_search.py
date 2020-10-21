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



# run using python fibonacci_search.py -v

'''
@params
arr: input array
val: the value to be searched
output: the index of element in the array or -1 if not found
return 0 if input array is empty
'''


def fibonacci_search(arr, val):
    """
    >>> fibonacci_search([1,6,7,0,0,0], 6)
    1
    >>> fibonacci_search([1,-1, 5, 2, 9], 10)
    -1
    >>> fibonacci_search([], 9)
    0
    """
    fib_N_2 = 0
    fib_N_1 = 1
    fibNext = fib_N_1 + fib_N_2
    length = len(arr)
    if length == 0:
        return 0
    while (fibNext < len(arr)):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2
    index = -1
    while (fibNext > 1):
        i = min(index + fib_N_2, (length - 1))
        if (arr[i] < val):
            fibNext = fib_N_1
            fib_N_1 = fib_N_2
            fib_N_2 = fibNext - fib_N_1
            index = i
        elif (arr[i] > val):
            fibNext = fib_N_2
            fib_N_1 = fib_N_1 - fib_N_2
            fib_N_2 = fibNext - fib_N_1
        else:
            return i
    if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
        return index + 1
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
