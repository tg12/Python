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



"""Convert a Decimal Number to an Octal Number."""

import math

# Modified from:
# https://github.com/TheAlgorithms/Javascript/blob/master/Conversions/DecimalToOctal.js


def decimal_to_octal(num):
    """Convert a Decimal Number to an Octal Number."""
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.pow(10, counter))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        # This formatting removes trailing '.0' from `octal`.
    return "{0:g}".format(float(octal))


def main():
    """Print octal equivelents of decimal numbers."""
    print("\n2 in octal is:")
    print(decimal_to_octal(2))  # = 2
    print("\n8 in octal is:")
    print(decimal_to_octal(8))  # = 10
    print("\n65 in octal is:")
    print(decimal_to_octal(65))  # = 101
    print("\n216 in octal is:")
    print(decimal_to_octal(216))  # = 330
    print("\n512 in octal is:")
    print(decimal_to_octal(512))  # = 1000
    print("\n")


if __name__ == "__main__":
    main()
