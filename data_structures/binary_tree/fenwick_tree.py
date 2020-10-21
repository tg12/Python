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



class FenwickTree:
    def __init__(self, SIZE):  # create fenwick tree with size SIZE
        self.Size = SIZE
        self.ft = [0 for i in range(0, SIZE)]

    def update(self, i, val):  # update data (adding) in index i in O(lg N)
        while i < self.Size:
            self.ft[i] += val
            i += i & (-i)

    def query(self, i):  # query cumulative data from index 0 to i in O(lg N)
        ret = 0
        while i > 0:
            ret += self.ft[i]
            i -= i & (-i)
        return ret


if __name__ == "__main__":
    f = FenwickTree(100)
    f.update(1, 20)
    f.update(4, 4)
    print(f.query(1))
    print(f.query(3))
    print(f.query(4))
    f.update(2, -5)
    print(f.query(1))
    print(f.query(3))
