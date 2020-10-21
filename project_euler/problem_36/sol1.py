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
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def is_palindrome(n):
    n = str(n)

    if n == n[::-1]:
        return True
    else:
        return False


def solution(n):
    """Return the sum of all numbers, less than n , which are palindromic in
    base 10 and base 2.

    >>> solution(1000000)
    872187
    >>> solution(500000)
    286602
    >>> solution(100000)
    286602
    >>> solution(1000)
    1772
    >>> solution(100)
    157
    >>> solution(10)
    25
    >>> solution(2)
    1
    >>> solution(1)
    0
    """
    total = 0

    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]):
            total += i
    return total


if __name__ == "__main__":
    print(solution(int(str(input().strip()))))
