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


class Letter:
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        self.bitstring = ""

    def __repr__(self):
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq, left, right):
        self.freq = freq
        self.left = left
        self.right = right


def parse_file(file_path):
    """
    Read the file and build a dict of all letters and their
    frequences, then convert the dict into a list of Letters.
    """
    chars = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars.keys() else 1
    return sorted([Letter(c, f)
                   for c, f in chars.items()], key=lambda l: l.freq)


def build_tree(letters):
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.
    """
    while len(letters) > 1:
        left = letters.pop(0)
        right = letters.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        letters.append(node)
        letters.sort(key=lambda l: l.freq)
    return letters[0]


def traverse_tree(root, bitstring):
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring, and return the list of Letters
    """
    if type(root) is Letter:
        root.bitstring = bitstring
        return [root]
    letters = []
    letters += traverse_tree(root.left, bitstring + "0")
    letters += traverse_tree(root.right, bitstring + "1")
    return letters


def huffman(file_path):
    """
    Parse the file, build the tree, then run through the file
    again, using the list of Letters to find and print out the
    bitstring for each letter.
    """
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = traverse_tree(root, "")
    print(f"Huffman Coding of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            le = list(filter(lambda l: l.letter == c, letters))[0]
            print(le.bitstring, end=" ")
    print()


if __name__ == "__main__":
    # pass the file path to the huffman function
    huffman(sys.argv[1])
