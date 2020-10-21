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
Comb sort is a relatively simple sorting algorithm originally designed by Wlodzimierz Dobosiewicz in 1980.
Later it was rediscovered by Stephen Lacey and Richard Box in 1991. Comb sort improves on bubble sort.

This is pure python implementation of comb sort algorithm
For doctests run following command:
python -m doctest -v comb_sort.py
or
python3 -m doctest -v comb_sort.py

For manual testing run:
python comb_sort.py
"""


def comb_sort(data):
    """Pure implementation of comb sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> comb_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> comb_sort([])
    []
    >>> comb_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    shrink_factor = 1.3
    gap = len(data)
    swapped = True
    i = 0

    while gap > 1 or swapped:
        # Update the gap value for a next comb
        gap = int(float(gap) / shrink_factor)

        swapped = False
        i = 0

        while gap + i < len(data):
            if data[i] > data[i + gap]:
                # Swap values
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True
            i += 1

    return data


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(comb_sort(unsorted))
