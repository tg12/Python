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
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest increasing subsequence of a given sequence.

The problem is  :
Given an ARRAY, to find the longest and increasing sub ARRAY in that given ARRAY and return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return [10, 22, 33, 41, 60, 80] as output
"""


def longestSub(ARRAY):  # This function is recursive

    ARRAY_LENGTH = len(ARRAY)
    if (
        ARRAY_LENGTH <= 1
    ):  # If the array contains only one element, we return it (it's the stop condition of recursion)
        return ARRAY
        # Else
    PIVOT = ARRAY[0]
    isFound = False
    i = 1
    LONGEST_SUB = []
    while not isFound and i < ARRAY_LENGTH:
        if ARRAY[i] < PIVOT:
            isFound = True
            TEMPORARY_ARRAY = [
                element for element in ARRAY[i:] if element >= ARRAY[i]]
            TEMPORARY_ARRAY = longestSub(TEMPORARY_ARRAY)
            if len(TEMPORARY_ARRAY) > len(LONGEST_SUB):
                LONGEST_SUB = TEMPORARY_ARRAY
        else:
            i += 1

    TEMPORARY_ARRAY = [element for element in ARRAY[1:] if element >= PIVOT]
    TEMPORARY_ARRAY = [PIVOT] + longestSub(TEMPORARY_ARRAY)
    if len(TEMPORARY_ARRAY) > len(LONGEST_SUB):
        return TEMPORARY_ARRAY
    else:
        return LONGEST_SUB


# Some examples

print(longestSub([4, 8, 7, 5, 1, 12, 2, 3, 9]))
print(longestSub([9, 8, 7, 6, 5, 7]))
