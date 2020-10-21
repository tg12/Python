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
Given a array of length n, max_subarray_sum() finds
the maximum of sum of contiguous sub-array using divide and conquer method.

Time complexity : O(n log n)

Ref : INTRODUCTION TO ALGORITHMS THIRD EDITION
(section : 4, sub-section : 4.1, page : 70)

"""


def max_sum_from_start(array):
    """ This function finds the maximum contiguous sum of array from 0 index

    Parameters :
    array (list[int]) : given array

    Returns :
    max_sum (int) : maximum contiguous sum of array from 0 index

    """
    array_sum = 0
    max_sum = float("-inf")
    for num in array:
        array_sum += num
        if array_sum > max_sum:
            max_sum = array_sum
    return max_sum


def max_cross_array_sum(array, left, mid, right):
    """ This function finds the maximum contiguous sum of left and right arrays

    Parameters :
    array, left, mid, right (list[int], int, int, int)

    Returns :
    (int) :  maximum of sum of contiguous sum of left and right arrays

    """

    max_sum_of_left = max_sum_from_start(array[left: mid + 1][::-1])
    max_sum_of_right = max_sum_from_start(array[mid + 1: right + 1])
    return max_sum_of_left + max_sum_of_right


def max_subarray_sum(array, left, right):
    """ Maximum contiguous sub-array sum, using divide and conquer method

    Parameters :
    array, left, right (list[int], int, int) :
    given array, current left index and current right index

    Returns :
    int :  maximum of sum of contiguous sub-array

    """

    # base case: array has only one element
    if left == right:
        return array[right]

    # Recursion
    mid = (left + right) // 2
    left_half_sum = max_subarray_sum(array, left, mid)
    right_half_sum = max_subarray_sum(array, mid + 1, right)
    cross_sum = max_cross_array_sum(array, left, mid, right)
    return max(left_half_sum, right_half_sum, cross_sum)


array = [-2, -5, 6, -2, -3, 1, 5, -6]
array_length = len(array)
print("Maximum sum of contiguous subarray:",
      max_subarray_sum(array, 0, array_length - 1))
