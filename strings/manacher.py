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



# calculate palindromic length from center with incrementing difference
def palindromic_length(center, diff, string):
    if (
        center - diff == -1
        or center + diff == len(string)
        or string[center - diff] != string[center + diff]
    ):
        return 0
    return 1 + palindromic_length(center, diff + 1, string)


def palindromic_string(input_string):
    """
    Manacher’s algorithm which finds Longest Palindromic Substring in linear time.

    1. first this conver input_string("xyx") into new_string("x|y|x") where odd positions are actual input
        characters.
    2. for each character in new_string it find corresponding length and store,
        a. max_length
        b. max_length's center
    3. return output_string from center - max_length to center + max_length and remove all "|"
    """
    max_length = 0

    # if input_string is "aba" than new_input_string become "a|b|a"
    new_input_string = ""
    output_string = ""

    # append each character + "|" in new_string for range(0, length-1)
    for i in input_string[: len(input_string) - 1]:
        new_input_string += i + "|"
    # append last character
    new_input_string += input_string[-1]

    # for each character in new_string find corresponding palindromic string
    for i in range(len(new_input_string)):

        # get palindromic length from ith position
        length = palindromic_length(i, 1, new_input_string)

        # update max_length and start position
        if max_length < length:
            max_length = length
            start = i

    # create that string
    for i in new_input_string[start - max_length: start + max_length + 1]:
        if i != "|":
            output_string += i

    return output_string


if __name__ == "__main__":
    n = input()
    print(palindromic_string(n))
