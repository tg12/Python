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



from math import sqrt
from typing import Tuple


def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]:
    """
    Given the numerical coefficients a, b and c,
    prints the solutions for a quadratic equation, for a*x*x + b*x + c.

    >>> QuadraticEquation(a=1, b=3, c=-4)
    ('1.0', '-4.0')
    >>> QuadraticEquation(5, 6, 1)
    ('-0.2', '-1.0')
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' must not be zero for quadratic equations.")
    delta = b * b - 4 * a * c
    if delta >= 0:
        return str((-b + sqrt(delta)) / (2 * a)
                   ), str((-b - sqrt(delta)) / (2 * a))
    """
    Treats cases of Complexes Solutions(i = imaginary unit)
    Ex.: a = 5, b = 2, c = 1
    Solution1 = (- 2 + 4.0 *i)/2 and Solution2 = (- 2 + 4.0 *i)/ 10
    """
    snd = sqrt(-delta)
    if b == 0:
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}"
    b = -abs(b)
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}"


def main():
    solutions = QuadraticEquation(a=5, b=6, c=1)
    print("The equation solutions are: {} and {}".format(*solutions))
    # The equation solutions are: -0.2 and -1.0


if __name__ == "__main__":
    main()
