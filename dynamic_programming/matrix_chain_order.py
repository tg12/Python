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



import sys

"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""


def MatrixChainOrder(array):
    N = len(array)
    Matrix = [[0 for x in range(N)] for x in range(N)]
    Sol = [[0 for x in range(N)] for x in range(N)]

    for ChainLength in range(2, N):
        for a in range(1, N - ChainLength + 1):
            b = a + ChainLength - 1

            Matrix[a][b] = sys.maxsize
            for c in range(a, b):
                cost = (Matrix[a][c] + Matrix[c + 1][b] +
                        array[a - 1] * array[c] * array[b])
                if cost < Matrix[a][b]:
                    Matrix[a][b] = cost
                    Sol[a][b] = c
    return Matrix, Sol


# Print order of matrix with Ai as Matrix
def PrintOptimalSolution(OptimalSolution, i, j):
    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        PrintOptimalSolution(OptimalSolution, i, OptimalSolution[i][j])
        PrintOptimalSolution(OptimalSolution, OptimalSolution[i][j] + 1, j)
        print(")", end=" ")


def main():
    array = [30, 35, 15, 5, 10, 20, 25]
    n = len(array)
    # Size of matrix created from above array will be
    # 30*35 35*15 15*5 5*10 10*20 20*25
    Matrix, OptimalSolution = MatrixChainOrder(array)

    print("No. of Operation required: " + str((Matrix[1][n - 1])))
    PrintOptimalSolution(OptimalSolution, 1, n - 1)


if __name__ == "__main__":
    main()
