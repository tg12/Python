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



# Divide and Conquer algorithm
def find_max(nums, left, right):
    """
    find max value in list
    :param nums: contains elements
    :param left: index of first element
    :param right: index of last element
    :return: max in nums

    >>> nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    >>> find_max(nums, 0, len(nums) - 1) == max(nums)
    True
    """
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  # the middle
    left_max = find_max(nums, left, mid)  # find max in range[left, mid]
    # find max in range[mid + 1, right]
    right_max = find_max(nums, mid + 1, right)

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert find_max(nums, 0, len(nums) - 1) == 10
