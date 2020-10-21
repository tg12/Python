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



def search_in_a_sorted_matrix(mat, m, n, key):
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            print("Key %s found at row- %s column- %s" % (key, i + 1, j + 1))
            return
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    print("Key %s not found" % (key))


def main():
    mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
    x = int(input("Enter the element to be searched:"))
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), x)


if __name__ == "__main__":
    main()
