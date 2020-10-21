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



# Fibonacci Sequence Using Recursion


def recur_fibo(n):
    """
    >>> [recur_fibo(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2)


def main():
    limit = int(input("How many terms to include in fibonacci series: "))
    if limit > 0:
        print(f"The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")


if __name__ == "__main__":
    main()
