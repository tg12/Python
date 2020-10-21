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



# Factorial of a number using memoization
result = [-1] * 10
result[0] = result[1] = 1


def factorial(num):
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    'Number should not be negative.'
    >>> [factorial(i) for i in range(5)]
    [1, 1, 2, 6, 24]
    """

    if num < 0:
        return "Number should not be negative."
    if result[num] != -1:
        return result[num]
    else:
        result[num] = num * factorial(num - 1)
        # uncomment the following to see how recalculations are avoided
        # print(result)
        return result[num]


# factorial of num
# uncomment the following to see how recalculations are avoided
# result=[-1]*10
# result[0]=result[1]=1
# print(factorial(5))
# print(factorial(3))
# print(factorial(7))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
