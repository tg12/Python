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
	The sum-of-subsetsproblem states that a set of non-negative integers, and a value M,
	determine all possible subsets of the given set whose summation sum equal to given M.

	Summation of the chosen numbers must be equal to given number M and one number can
	be used only once.
"""


def generate_sum_of_subsets_soln(nums, max_sum):
    result = []
    path = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(
        nums,
        max_sum,
        num_index,
        path,
        result,
        remaining_nums_sum)
    return result


def create_state_space_tree(
        nums,
        max_sum,
        num_index,
        path,
        result,
        remaining_nums_sum):
    """
        Creates a state space tree to iterate through each branch using DFS.
        It terminates the branching of a node when any of the two conditions
        given below satisfy.
        This algorithm follows depth-fist-search and backtracks when the node is not branchable.

        """
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for num_index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            num_index + 1,
            path + [nums[num_index]],
            result,
            remaining_nums_sum - nums[num_index],
        )


"""
remove the comment to take an input from the user

print("Enter the elements")
nums = list(map(int, input().split()))
print("Enter max_sum sum")
max_sum = int(input())

"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = generate_sum_of_subsets_soln(nums, max_sum)
print(*result)
