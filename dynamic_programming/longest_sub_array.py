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
Auther  : Yvonne

This is a pure Python implementation of Dynamic Programming solution to the longest_sub_array problem.

The problem is  :
Given an array, to find the longest and continuous sub array and get the max sum of the sub array in the given array.
"""


class SubArray:
    def __init__(self, arr):
        # we need a list not a string, so do something to change the type
        self.array = arr.split(",")
        print(("the input array is:", self.array))

    def solve_sub_array(self):
        rear = [int(self.array[0])] * len(self.array)
        sum_value = [int(self.array[0])] * len(self.array)
        for i in range(1, len(self.array)):
            sum_value[i] = max(
                int(self.array[i]) + sum_value[i - 1], int(self.array[i])
            )
            rear[i] = max(sum_value[i], rear[i - 1])
        return rear[len(self.array) - 1]


if __name__ == "__main__":
    whole_array = input("please input some numbers:")
    array = SubArray(whole_array)
    re = array.solve_sub_array()
    print(("the results is:", re))
