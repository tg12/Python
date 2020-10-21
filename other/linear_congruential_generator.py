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



__author__ = "Tobias Carryer"

from time import time


class LinearCongruentialGenerator(object):
    """
    A pseudorandom number generator.
    """

    def __init__(self, multiplier, increment, modulo, seed=int(time())):
        """
        These parameters are saved and used when nextNumber() is called.

        modulo is the largest number that can be generated (exclusive). The most
        efficent values are powers of 2. 2^32 is a common value.
        """
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.seed = seed

    def next_number(self):
        """
        The smallest number that can be generated is zero.
        The largest number that can be generated is modulo-1. modulo is set in the constructor.
        """
        self.seed = (self.multiplier * self.seed +
                     self.increment) % self.modulo
        return self.seed


if __name__ == "__main__":
    # Show the LCG in action.
    lcg = LinearCongruentialGenerator(1664525, 1013904223, 2 << 31)
    while True:
        print(lcg.next_number())
