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



"""Prime Check."""

import math
import unittest


def prime_check(number):
    """
    Check to See if a Number is Prime.

    A number is prime if it has exactly two dividers: 1 and itself.
    """
    if number < 2:
        # Negatives, 0 and 1 are not primes
        return False
    if number < 4:
        # 2 and 3 are primes
        return True
    if number % 2 == 0:
        # Even values are not primes
        return False

    # Except 2, all primes are odd. If any odd value divide
    # the number, then that number is not prime.
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2)
    return not any(number % i == 0 for i in odd_numbers)


class Test(unittest.TestCase):
    def test_primes(self):
        self.assertTrue(prime_check(2))
        self.assertTrue(prime_check(3))
        self.assertTrue(prime_check(5))
        self.assertTrue(prime_check(7))
        self.assertTrue(prime_check(11))
        self.assertTrue(prime_check(13))
        self.assertTrue(prime_check(17))
        self.assertTrue(prime_check(19))
        self.assertTrue(prime_check(23))
        self.assertTrue(prime_check(29))

    def test_not_primes(self):
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.")
        self.assertFalse(
            prime_check(0),
            "Zero doesn't have any divider, primes must have two")
        self.assertFalse(
            prime_check(1), "One just have 1 divider, primes must have two."
        )
        self.assertFalse(prime_check(2 * 2))
        self.assertFalse(prime_check(2 * 3))
        self.assertFalse(prime_check(3 * 3))
        self.assertFalse(prime_check(3 * 5))
        self.assertFalse(prime_check(3 * 5 * 7))


if __name__ == "__main__":
    unittest.main()
