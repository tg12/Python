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

This is a python implementation for questions involving task assignments between people.
Here Bitmasking and DP are used for solving this.

Question :-
We have N tasks and M people. Each person in M can do only certain of these tasks. Also a person can do only one task and a task is performed only by one person.
Find the total no of ways in which the tasks can be distributed.


"""
from collections import defaultdict


class AssignmentUsingBitmask:
    def __init__(self, task_performed, total):

        self.total_tasks = total  # total no of tasks (N)

        # DP table will have a dimension of (2^M)*N
        # initially all values are set to -1
        self.dp = [[-1 for i in range(total + 1)]
                   for j in range(2 ** len(task_performed))]

        # stores the list of persons for each task
        self.task = defaultdict(list)

        # finalmask is used to check if all persons are included by setting all
        # bits to 1
        self.finalmask = (1 << len(task_performed)) - 1

    def CountWaysUtil(self, mask, taskno):

        # if mask == self.finalmask all persons are distributed tasks, return 1
        if mask == self.finalmask:
            return 1

        # if not everyone gets the task and no more tasks are available, return
        # 0
        if taskno > self.total_tasks:
            return 0

        # if case already considered
        if self.dp[mask][taskno] != -1:
            return self.dp[mask][taskno]

        # Number of ways when we dont this task in the arrangement
        total_ways_util = self.CountWaysUtil(mask, taskno + 1)

        # now assign the tasks one by one to all possible persons and
        # recursively assign for the remaining tasks.
        if taskno in self.task:
            for p in self.task[taskno]:

                # if p is already given a task
                if mask & (1 << p):
                    continue

                # assign this task to p and change the mask value. And
                # recursively assign tasks with the new mask value.
                total_ways_util += self.CountWaysUtil(
                    mask | (1 << p), taskno + 1)

        # save the value.
        self.dp[mask][taskno] = total_ways_util

        return self.dp[mask][taskno]

    def countNoOfWays(self, task_performed):

        # Store the list of persons for each task
        for i in range(len(task_performed)):
            for j in task_performed[i]:
                self.task[j].append(i)

        # call the function to fill the DP table, final answer is stored in
        # dp[0][1]
        return self.CountWaysUtil(0, 1)


if __name__ == "__main__":

    total_tasks = 5  # total no of tasks (the value of N)

    # the list of tasks that can be done by M persons.
    task_performed = [[1, 3, 4], [1, 2, 5], [3, 4]]
    print(
        AssignmentUsingBitmask(task_performed, total_tasks).countNoOfWays(
            task_performed
        )
    )
    """
    For the particular example the tasks can be distributed as
    (1,2,3), (1,2,4), (1,5,3), (1,5,4), (3,1,4), (3,2,4), (3,5,4), (4,1,3), (4,2,3), (4,5,3)
    total 10
    """
