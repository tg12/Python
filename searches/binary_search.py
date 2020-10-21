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
This is pure python implementation of binary search algorithm

For doctests run following command:
python -m doctest -v binary_search.py
or
python3 -m doctest -v binary_search.py

For manual testing run:
python binary_search.py
"""
import bisect


def binary_search(sorted_collection, item):
    """Pure implementation of binary search algorithm in Python

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def binary_search_std_lib(sorted_collection, item):
    """Pure implementation of binary search algorithm in Python using stdlib

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None


def binary_search_by_recursion(sorted_collection, item, left, right):
    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    """
    if right < left:
        return None

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(
            sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(
            sorted_collection, item, midpoint + 1, right)


def __assert_sorted(collection):
    """Check if collection is ascending sorted, if not - raises :py:class:`ValueError`

    :param collection: collection
    :return: True if collection is ascending sorted
    :raise: :py:class:`ValueError` if collection is not ascending sorted

    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True

    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be ascending sorted
    """
    if collection != sorted(collection):
        raise ValueError("Collection must be ascending sorted")
    return True


if __name__ == "__main__":
    import sys

    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be ascending sorted to apply binary search")

    target_input = input("Enter a single number to be found in the list:\n")
    target = int(target_input)
    result = binary_search(collection, target)
    if result is not None:
        print("{} found at positions: {}".format(target, result))
    else:
        print("Not found")
