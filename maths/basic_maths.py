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



"""Implementation of Basic Math in Python."""
import math


def prime_factors(n):
    """Find Prime Factors."""
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)

    if n > 2:
        pf.append(n)

    return pf


def number_of_divisors(n):
    """Calculate Number of Divisors of an Integer."""
    div = 1

    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div = div * (temp)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        div = div * (temp)

    return div


def sum_of_divisors(n):
    """Calculate Sum of Divisors."""
    s = 1

    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    if temp > 1:
        s *= (2 ** temp - 1) / (2 - 1)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        if temp > 1:
            s *= (i ** temp - 1) / (i - 1)

    return s


def euler_phi(n):
    """Calculte Euler's Phi Function."""
    l = prime_factors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1) / x
    return s


def main():
    """Print the Results of Basic Math Operations."""
    print(prime_factors(100))
    print(number_of_divisors(100))
    print(sum_of_divisors(100))
    print(euler_phi(100))


if __name__ == "__main__":
    main()
