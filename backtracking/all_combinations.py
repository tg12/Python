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



# -*- coding: utf-8 -*-

"""
	In this problem, we want to determine all possible combinations of k
	numbers out of 1 ... n. We use backtracking to solve this problem.
	Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!)))
"""


def generate_all_combinations(n: int, k: int) -> [[int]]:
    """
    >>> generate_all_combinations(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """

    result = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(increment, total_number, level, current_list, total_list):
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(
            i + 1,
            total_number,
            level - 1,
            current_list,
            total_list)
        current_list.pop()


def print_all_state(total_list):
    for i in total_list:
        print(*i)


if __name__ == "__main__":
    n = 4
    k = 2
    total_list = generate_all_combinations(n, k)
    print_all_state(total_list)
