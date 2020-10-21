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



# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from sympy import diff
from decimal import Decimal


def NewtonRaphson(func, a):
    """ Finds root from the point 'a' onwards by Newton-Raphson method """
    while True:
        c = Decimal(a) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))

        a = c

        # This number dictates the accuracy of the answer
        if abs(eval(func)) < 10 ** -15:
            return c


# Let's Execute
if __name__ == "__main__":
    # Find root of trigonometric function
    # Find value of pi
    print("sin(x) = 0", NewtonRaphson("sin(x)", 2))

    # Find root of polynomial
    print("x**2 - 5*x +2 = 0", NewtonRaphson("x**2 - 5*x +2", 0.4))

    # Find Square Root of 5
    print("x**2 - 5 = 0", NewtonRaphson("x**2 - 5", 0.1))

    # Exponential Roots
    print("exp(x) - 1 = 0", NewtonRaphson("exp(x) - 1", 0))
