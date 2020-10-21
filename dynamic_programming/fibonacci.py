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
This is a pure Python implementation of Dynamic Programming solution to the fibonacci sequence problem.
"""


class Fibonacci:
    def __init__(self, N=None):
        self.fib_array = []
        if N:
            N = int(N)
            self.fib_array.append(0)
            self.fib_array.append(1)
            for i in range(2, N + 1):
                self.fib_array.append(
                    self.fib_array[i - 1] + self.fib_array[i - 2])
        elif N == 0:
            self.fib_array.append(0)
        print(self.fib_array)

    def get(self, sequence_no=None):
        """
        >>> Fibonacci(5).get(3)
        [0, 1, 1, 2, 3, 5]
        [0, 1, 1, 2]
        >>> Fibonacci(5).get(6)
        [0, 1, 1, 2, 3, 5]
        Out of bound.
        >>> Fibonacci(5).get(-1)
        [0, 1, 1, 2, 3, 5]
        []
        """
        if sequence_no is not None:
            if sequence_no < len(self.fib_array):
                return print(self.fib_array[: sequence_no + 1])
            else:
                print("Out of bound.")
        else:
            print("Please specify a value")


if __name__ == "__main__":
    print("\n********* Fibonacci Series Using Dynamic Programming ************\n")
    print("\n Enter the upper limit for the fibonacci sequence: ", end="")
    try:
        N = int(input().strip())
        fib = Fibonacci(N)
        print(
            "\n********* Enter different values to get the corresponding fibonacci "
            "sequence, enter any negative number to exit. ************\n")
        while True:
            try:
                i = int(input("Enter value: ").strip())
                if i < 0:
                    print("\n********* Good Bye!! ************\n")
                    break
                fib.get(i)
            except NameError:
                print("\nInvalid input, please try again.")
    except NameError:
        print("\n********* Invalid input, good bye!! ************\n")

    import doctest

    doctest.testmod()
