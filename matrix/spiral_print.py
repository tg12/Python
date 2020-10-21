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
This program print the matix in spiral form.
This problem has been solved through recursive way.

      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii)column of all the row should be equal
"""


def checkMatrix(a):
    # must be
    if isinstance(a, list) and len(a) > 0:
        if isinstance(a[0], list):
            prevLen = 0
            for i in a:
                if prevLen == 0:
                    prevLen = len(i)
                    result = True
                elif prevLen == len(i):
                    result = True
                else:
                    result = False
        else:
            result = True
    else:
        result = False
    return result


def spiralPrint(a):

    if checkMatrix(a) and len(a) > 0:

        matRow = len(a)
        if isinstance(a[0], list):
            matCol = len(a[0])
        else:
            for dat in a:
                print(dat),
            return

        # horizotal printing increasing
        for i in range(0, matCol):
            print(a[0][i]),
        # vertical printing down
        for i in range(1, matRow):
            print(a[i][matCol - 1]),
        # horizotal printing decreasing
        if matRow > 1:
            for i in range(matCol - 2, -1, -1):
                print(a[matRow - 1][i]),
        # vertical printing up
        for i in range(matRow - 2, 0, -1):
            print(a[i][0]),
        remainMat = [row[1: matCol - 1] for row in a[1: matRow - 1]]
        if len(remainMat) > 0:
            spiralPrint(remainMat)
        else:
            return
    else:
        print("Not a valid matrix")
        return


# driver code
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
spiralPrint(a)
