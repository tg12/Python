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



import math


class SegmentTree:
    def __init__(self, N):
        self.N = N
        self.st = [
            0 for i in range(0, 4 * N)
        ]  # approximate the overall size of segment tree with array N
        # create array to store lazy update
        self.lazy = [0 for i in range(0, 4 * N)]
        self.flag = [0 for i in range(0, 4 * N)]  # flag for lazy update

    def left(self, idx):
        return idx * 2

    def right(self, idx):
        return idx * 2 + 1

    def build(self, idx, l, r, A):
        if l == r:
            self.st[idx] = A[l - 1]
        else:
            mid = (l + r) // 2
            self.build(self.left(idx), l, mid, A)
            self.build(self.right(idx), mid + 1, r, A)
            self.st[idx] = max(self.st[self.left(idx)],
                               self.st[self.right(idx)])

    # update with O(lg N) (Normal segment tree without lazy update will take
    # O(Nlg N) for each update)
    def update(
        self, idx, l, r, a, b, val
    ):  # update(1, 1, N, a, b, v) for update val v to [a,b]
        if self.flag[idx]:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True

        if r < a or l > b:
            return True
        if l >= a and r <= b:
            self.st[idx] = val
            if l != r:
                self.lazy[self.left(idx)] = val
                self.lazy[self.right(idx)] = val
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
            return True
        mid = (l + r) // 2
        self.update(self.left(idx), l, mid, a, b, val)
        self.update(self.right(idx), mid + 1, r, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
        return True

    # query with O(lg N)
    # query(1, 1, N, a, b) for query max of [a,b]
    def query(self, idx, l, r, a, b):
        if self.flag[idx]:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
        if r < a or l > b:
            return -math.inf
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l + r) // 2
        q1 = self.query(self.left(idx), l, mid, a, b)
        q2 = self.query(self.right(idx), mid + 1, r, a, b)
        return max(q1, q2)

    def showData(self):
        showList = []
        for i in range(1, N + 1):
            showList += [self.query(1, 1, self.N, i, i)]
        print(showList)


if __name__ == "__main__":
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1, 1, N, A)
    print(segt.query(1, 1, N, 4, 6))
    print(segt.query(1, 1, N, 7, 11))
    print(segt.query(1, 1, N, 7, 12))
    segt.update(1, 1, N, 1, 3, 111)
    print(segt.query(1, 1, N, 1, 15))
    segt.update(1, 1, N, 7, 8, 235)
    segt.showData()
