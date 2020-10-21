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
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
import os


# Precomputes a list of the 100 first triangular numbers
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)]


def solution():
    """
    Finds the amount of triangular words in the words file.

    >>> solution()
    162
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    wordsFilePath = os.path.join(script_dir, "words.txt")

    words = ""
    with open(wordsFilePath, "r") as f:
        words = f.readline()

    words = list(map(lambda word: word.strip(
        '"'), words.strip("\r\n").split(",")))
    words = list(
        filter(
            lambda word: word in TRIANGULAR_NUMBERS,
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words),
        )
    )
    return len(words)


if __name__ == "__main__":
    print(solution())
