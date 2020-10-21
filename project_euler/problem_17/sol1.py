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
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance withBritish
usage.
"""


def solution(n):
    """Returns the number of letters used to write all numbers from 1 to n.
    where n is lower or equals to 1000.
    >>> solution(1000)
    21124
    >>> solution(5)
    19
    """
    # number of letters in zero, one, two, ..., nineteen (0 for zero since it's
    # never said aloud)
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # number of letters in twenty, thirty, ..., ninety (0 for numbers less than
    # 20 due to inconsistency in teens)
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    count = 0

    for i in range(1, n + 1):
        if i < 1000:
            if i >= 100:
                # add number of letters for "n hundred"
                count += ones_counts[i // 100] + 7

                if i % 100 != 0:
                    # add number of letters for "and" if number is not multiple
                    # of 100
                    count += 3

            if 0 < i % 100 < 20:
                # add number of letters for one, two, three, ..., nineteen
                # (could be combined with below if not for inconsistency in
                # teens)
                count += ones_counts[i % 100]
            else:
                # add number of letters for twenty, twenty one, ..., ninety
                # nine
                count += ones_counts[i % 10]
                count += tens_counts[(i % 100 - i % 10) // 10]
        else:
            count += ones_counts[i // 1000] + 8
    return count


if __name__ == "__main__":
    print(solution(int(input().strip())))
