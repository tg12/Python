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



from typing import Tuple, List


def n31(a: int) -> Tuple[List[int], int]:
    """
    Returns the Collatz sequence and its length of any postiver integer.
    >>> n31(4)
    ([4, 2, 1], 3)
    """

    if not isinstance(a, int):
        raise TypeError("Must be int, not {0}".format(type(a).__name__))
    if a < 1:
        raise ValueError(
            "Given integer must be greater than 1, not {0}".format(a))

    path = [a]
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        path += [a]
    return path, len(path)


def main():
    num = 4
    path, length = n31(num)
    print(
        "The Collatz sequence of {0} took {1} steps. \nPath: {2}".format(
            num, length, path
        )
    )


if __name__ == "__main__":
    main()
