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

 The nqueens problem is of placing N queens on a N * N
 chess board such that no queen can attack any other queens placed
 on that chess board.
 This means that one queen cannot have any other queen on its horizontal, vertical and
 diagonal lines.

"""
solution = []


def isSafe(board, row, column):
    """
    This function returns a boolean value True if it is safe to place a queen there considering
    the current state of the board.

    Parameters :
    board(2D matrix) : board
    row ,column : coordinates of the cell on a board

    Returns :
    Boolean Value

    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


def solve(board, row):
    """
    It creates a state space tree and calls the safe function untill it receives a
    False Boolean and terminates that brach and backtracks to the next
    poosible solution branch.
    """
    if row >= len(board):
        """
        If the row number exceeds N we have board with a successful combination
        and that combination is appended to the solution list and the board is printed.

        """
        solution.append(board)
        printboard(board)
        print()
        return
    for i in range(len(board)):
        """
        For every row it iterates through each column to check if it is feesible to place a
        queen there.
        If all the combinations for that particaular branch are successfull the board is
        reinitialized for the next possible combination.
        """
        if isSafe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board):
    """
    Prints the boards that have a successfull combination.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# n=int(input("The no. of queens"))
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
