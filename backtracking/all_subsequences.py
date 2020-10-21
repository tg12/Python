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
	In this problem, we want to determine all possible subsequences
	of the given sequence. We use backtracking to solve this problem.

	Time complexity: O(2^n),
	where n denotes the length of the given sequence.
"""


def generate_all_subsequences(sequence):
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(sequence, current_subsequence, index):
    """
        Creates a state space tree to iterate through each branch using DFS.
        We know that each state has exactly two children.
        It terminates when it reaches the end of the given sequence.
        """

    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()


"""
remove the comment to take an input from the user

print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence = [3, 1, 2, 4]
generate_all_subsequences(sequence)

sequence = ["A", "B", "C"]
generate_all_subsequences(sequence)
