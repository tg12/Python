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



""" Convert Base 10 (Decimal) Values to Hexadecimal Representations """

# set decimal value for each hexadecimal digit
values = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


def decimal_to_hexadecimal(decimal):
    """
        take integer decimal value, return hexadecimal representation as str beginning with 0x
        >>> decimal_to_hexadecimal(5)
        '0x5'
        >>> decimal_to_hexadecimal(15)
        '0xf'
        >>> decimal_to_hexadecimal(37)
        '0x25'
        >>> decimal_to_hexadecimal(255)
        '0xff'
        >>> decimal_to_hexadecimal(4096)
        '0x1000'
        >>> decimal_to_hexadecimal(999098)
        '0xf3eba'
        >>> # negatives work too
        >>> decimal_to_hexadecimal(-256)
        '-0x100'
        >>> # floats are acceptable if equivalent to an int
        >>> decimal_to_hexadecimal(17.0)
        '0x11'
        >>> # other floats will error
        >>> decimal_to_hexadecimal(16.16) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # strings will error as well
        >>> decimal_to_hexadecimal('0xfffff') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        AssertionError
        >>> # results are the same when compared to Python's default hex function
        >>> decimal_to_hexadecimal(-256) == hex(-256)
        True
    """
    assert type(decimal) in (int, float) and decimal == int(decimal)
    hexadecimal = ""
    negative = False
    if decimal < 0:
        negative = True
        decimal *= -1
    while decimal > 0:
        decimal, remainder = divmod(decimal, 16)
        hexadecimal = values[remainder] + hexadecimal
    hexadecimal = "0x" + hexadecimal
    if negative:
        hexadecimal = "-" + hexadecimal
    return hexadecimal


if __name__ == "__main__":
    import doctest

    doctest.testmod()
