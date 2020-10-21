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



"""Queue represented by a python list"""


class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item):
        self.entries.append(item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        # self.front-=1
        # self.entries = self.entries[self.front:]
        self.entries = self.entries[1:]
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    """Enqueues {@code item}
    @return item at front of self.entries"""

    def front(self):
        return self.entries[0]

    """Returns the length of this.entries"""

    def size(self):
        return self.length
