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



def maximum_digital_sum(a: int, b: int) -> int:
    """
        Considering natural numbers of the form, a**b, where a, b < 100,
        what is the maximum digital sum?
        :param a:
        :param b:
        :return:
        >>> maximum_digital_sum(10,10)
        45

        >>> maximum_digital_sum(100,100)
        972

        >>> maximum_digital_sum(100,200)
        1872
    """

    # RETURN the MAXIMUM from the list of SUMs of the list of INT converted
    # from STR of BASE raised to the POWER
    return max(
        [
            sum([int(x) for x in str(base ** power)])
            for base in range(a)
            for power in range(b)
        ]
    )


# Tests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
