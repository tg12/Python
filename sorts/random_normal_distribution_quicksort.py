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



from random import randint
from tempfile import TemporaryFile
import numpy as np


def _inPlaceQuickSort(A, start, end):
    count = 0
    if start < end:
        pivot = randint(start, end)
        temp = A[end]
        A[end] = A[pivot]
        A[pivot] = temp

        p, count = _inPlacePartition(A, start, end)
        count += _inPlaceQuickSort(A, start, p - 1)
        count += _inPlaceQuickSort(A, p + 1, end)
    return count


def _inPlacePartition(A, start, end):

    count = 0
    pivot = randint(start, end)
    temp = A[end]
    A[end] = A[pivot]
    A[pivot] = temp
    newPivotIndex = start - 1
    for index in range(start, end):

        count += 1
        if A[index] < A[end]:  # check if current val is less than pivot value
            newPivotIndex = newPivotIndex + 1
            temp = A[newPivotIndex]
            A[newPivotIndex] = A[index]
            A[index] = temp

    temp = A[newPivotIndex + 1]
    A[newPivotIndex + 1] = A[end]
    A[end] = temp
    return newPivotIndex + 1, count


outfile = TemporaryFile()
p = 100  # 1000 elements are to be sorted


mu, sigma = 0, 1  # mean and standard deviation
X = np.random.normal(mu, sigma, p)
np.save(outfile, X)
print("The array is")
print(X)


outfile.seek(0)  # using the same array
M = np.load(outfile)
r = len(M) - 1
z = _inPlaceQuickSort(M, 0, r)

print(
    "No of Comparisons for 100 elements selected from a standard normal distribution is :"
)
print(z)
