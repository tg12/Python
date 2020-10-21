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



"""Newton's Method."""

# Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method


# function is the f(x) and function1 is the f'(x)
def newton(function, function1, startingInt):
    x_n = startingInt
    while True:
        x_n1 = x_n - function(x_n) / function1(x_n)
        if abs(x_n - x_n1) < 10 ** -5:
            return x_n1
        x_n = x_n1


def f(x):
    return (x ** 3) - (2 * x) - 5


def f1(x):
    return 3 * (x ** 2) - 2


if __name__ == "__main__":
    print(newton(f, f1, 3))
