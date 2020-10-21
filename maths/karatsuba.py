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



""" Multiply two numbers using Karatsuba algorithm """


def karatsuba(a, b):
    """
    >>> karatsuba(15463, 23489) == 15463 * 23489
    True
    >>> karatsuba(3, 9) == 3 * 9
    True
    """
    if len(str(a)) == 1 or len(str(b)) == 1:
        return (a * b)
    else:
        m1 = max(len(str(a)), len(str(b)))
        m2 = m1 // 2

        a1, a2 = divmod(a, 10**m2)
        b1, b2 = divmod(b, 10**m2)

        x = karatsuba(a2, b2)
        y = karatsuba((a1 + a2), (b1 + b2))
        z = karatsuba(a1, b1)

        return ((z * 10**(2 * m2)) + ((y - z - x) * 10**(m2)) + (x))


def main():
    print(karatsuba(15463, 23489))


if __name__ == "__main__":
    main()
