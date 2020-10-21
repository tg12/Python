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
    This is an implementation of Pigeon Hole Sort.
    For doctests run following command:

    python3 -m doctest -v pigeon_sort.py
    or
    python -m doctest -v pigeon_sort.py

    For manual testing run:
    python pigeon_sort.py
"""


def pigeon_sort(array):
    """
    Implementation of pigeon hole sort algorithm
    :param array: Collection of comparable items
    :return: Collection sorted in ascending order
    >>> pigeon_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pigeon_sort([])
    []
    >>> pigeon_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    if len(array) == 0:
        return array

    # Manually finds the minimum and maximum of the array.
    min = array[0]
    max = array[0]

    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]

    # Compute the variables
    holes_range = max - min + 1
    holes = [0 for _ in range(holes_range)]
    holes_repeat = [0 for _ in range(holes_range)]

    # Make the sorting.
    for i in range(len(array)):
        index = array[i] - min
        if holes[index] != array[i]:
            holes[index] = array[i]
            holes_repeat[index] += 1
        else:
            holes_repeat[index] += 1

    # Makes the array back by replacing the numbers.
    index = 0
    for i in range(holes_range):
        while holes_repeat[i] > 0:
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1

    # Returns the sorted array.
    return array


if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n")
    unsorted = [int(x) for x in user_input.split(",")]
    print(pigeon_sort(unsorted))
