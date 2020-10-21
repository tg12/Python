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
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approch of suming 'Equally Spaced Abscissas'

method 2:
"Simpson Rule"

"""


def method_2(boundary, steps):
    # "Simpson Rule"
    # int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 3.0) * f(a)
    cnt = 2
    for i in x_i:
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i)
        cnt += 1
    y += (h / 3.0) * f(b)
    return y


def make_points(a, b, h):
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


def f(x):  # enter your function here
    y = (x - 0) * (x - 0)
    return y


def main():
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # define number of steps or resolution
    boundary = [a, b]  # define boundary of integration
    y = method_2(boundary, steps)
    print("y = {0}".format(y))


if __name__ == "__main__":
    main()
