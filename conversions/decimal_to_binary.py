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



"""Convert a Decimal Number to a Binary Number."""


def decimal_to_binary(num):
    """
        Convert a Integer Decimal Number to a Binary Number as str.
        >>> decimal_to_binary(0)
        '0b0'
        >>> decimal_to_binary(2)
        '0b10'
        >>> decimal_to_binary(7)
        '0b111'
        >>> decimal_to_binary(35)
        '0b100011'
        >>> # negatives work too
        >>> decimal_to_binary(-2)
        '-0b10'
        >>> # other floats will error
        >>> decimal_to_binary(16.16) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'float' object cannot be interpreted as an integer
        >>> # strings will error as well
        >>> decimal_to_binary('0xfffff') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'str' object cannot be interpreted as an integer
    """

    if isinstance(num, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if isinstance(num, str):
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
