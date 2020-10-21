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



"""Lower-Upper (LU) Decomposition."""

# lower–upper (LU) decomposition -
# https://en.wikipedia.org/wiki/LU_decomposition
import numpy


def LUDecompose(table):
    # Table that contains our data
    # Table has to be a square array so we need to check first
    rows, columns = numpy.shape(table)
    L = numpy.zeros((rows, columns))
    U = numpy.zeros((rows, columns))
    if rows != columns:
        return []
    for i in range(columns):
        for j in range(i - 1):
            sum = 0
            for k in range(j - 1):
                sum += L[i][k] * U[k][j]
            L[i][j] = (table[i][j] - sum) / U[j][j]
        L[i][i] = 1
        for j in range(i - 1, columns):
            sum1 = 0
            for k in range(i - 1):
                sum1 += L[i][k] * U[k][j]
            U[i][j] = table[i][j] - sum1
    return L, U


if __name__ == "__main__":
    matrix = numpy.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    L, U = LUDecompose(matrix)
    print(L)
    print(U)
