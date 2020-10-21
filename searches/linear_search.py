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
This is pure python implementation of linear search algorithm

For doctests run following command:
python -m doctest -v linear_search.py
or
python3 -m doctest -v linear_search.py

For manual testing run:
python linear_search.py
"""


def linear_search(sequence, target):
    """Pure implementation of linear search algorithm in Python

    :param sequence: some sorted collection with comparable items
    :param target: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0

    >>> linear_search([0, 5, 7, 10, 15], 15)
    4

    >>> linear_search([0, 5, 7, 10, 15], 5)
    1

    >>> linear_search([0, 5, 7, 10, 15], 6)

    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = linear_search(sequence, target)
    if result is not None:
        print("{} found at positions: {}".format(target, result))
    else:
        print("Not found")
