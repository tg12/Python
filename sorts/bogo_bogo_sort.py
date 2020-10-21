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
Python implementation of bogobogosort, a "sorting algorithm
designed not to succeed before the heat death of the universe
on any sizable list" - https://en.wikipedia.org/wiki/Bogosort.

Author: WilliamHYZhang
"""

import random


def bogo_bogo_sort(collection):
    """
    returns the collection sorted in ascending order
    :param collection: list of comparable items
    :return: the list sorted in ascending order

    Examples:
    >>> bogo_bogo_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bogo_bogo_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> bogo_bogo_sort([420, 69])
    [69, 420]
    """

    def is_sorted(collection):
        if len(collection) == 1:
            return True

        clone = collection.copy()
        while True:
            random.shuffle(clone)
            ordered = bogo_bogo_sort(clone[:-1])
            if clone[len(clone) - 1] >= max(ordered):
                break

        for i in range(len(ordered)):
            clone[i] = ordered[i]

        for i in range(len(collection)):
            if clone[i] != collection[i]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(bogo_bogo_sort(unsorted))
