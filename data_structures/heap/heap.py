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



#!/usr/bin/python

# This heap class start from here.


class Heap:
    def __init__(self):  # Default constructor of heap class.
        self.h = []
        self.currsize = 0

    def leftChild(self, i):
        if 2 * i + 1 < self.currsize:
            return 2 * i + 1
        return None

    def rightChild(self, i):
        if 2 * i + 2 < self.currsize:
            return 2 * i + 2
        return None

    def maxHeapify(self, node):
        if node < self.currsize:
            m = node
            lc = self.leftChild(node)
            rc = self.rightChild(node)
            if lc is not None and self.h[lc] > self.h[m]:
                m = lc
            if rc is not None and self.h[rc] > self.h[m]:
                m = rc
            if m != node:
                temp = self.h[node]
                self.h[node] = self.h[m]
                self.h[m] = temp
                self.maxHeapify(m)

    def buildHeap(
        self, a
    ):  # This function is used to build the heap from the data container 'a'.
        self.currsize = len(a)
        self.h = list(a)
        for i in range(self.currsize // 2, -1, -1):
            self.maxHeapify(i)

    # This function is used to get maximum value from the heap.
    def getMax(self):
        if self.currsize >= 1:
            me = self.h[0]
            temp = self.h[0]
            self.h[0] = self.h[self.currsize - 1]
            self.h[self.currsize - 1] = temp
            self.currsize -= 1
            self.maxHeapify(0)
            return me
        return None

    def heapSort(self):  # This function is used to sort the heap.
        size = self.currsize
        while self.currsize - 1 >= 0:
            temp = self.h[0]
            self.h[0] = self.h[self.currsize - 1]
            self.h[self.currsize - 1] = temp
            self.currsize -= 1
            self.maxHeapify(0)
        self.currsize = size

    # This function is used to insert data in the heap.
    def insert(self, data):
        self.h.append(data)
        curr = self.currsize
        self.currsize += 1
        while self.h[curr] > self.h[curr / 2]:
            temp = self.h[curr / 2]
            self.h[curr / 2] = self.h[curr]
            self.h[curr] = temp
            curr = curr / 2

    def display(self):  # This function is used to print the heap.
        print(self.h)


def main():
    l = list(map(int, input().split()))
    h = Heap()
    h.buildHeap(l)
    h.heapSort()
    h.display()


if __name__ == "__main__":
    main()
