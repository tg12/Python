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



def median(nums):
    """
    Find median of a list of numbers.

    >>> median([0])
    0
    >>> median([4,1,3,2])
    2.5

    Args:
        nums: List of nums

    Returns:
        Median.
    """
    sorted_list = sorted(nums)
    med = None
    if len(sorted_list) % 2 == 0:
        mid_index_1 = len(sorted_list) // 2
        mid_index_2 = (len(sorted_list) // 2) - 1
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2)
    else:
        mid_index = (len(sorted_list) - 1) // 2
        med = sorted_list[mid_index]
    return med


def main():
    print("Odd number of numbers:")
    print(median([2, 4, 6, 8, 20, 50, 70]))
    print("Even number of numbers:")
    print(median([2, 4, 6, 8, 20, 50]))


if __name__ == "__main__":
    main()
