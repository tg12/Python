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



# Program to find whether given string is palindrome or not
def is_palindrome(str):
    start_i = 0
    end_i = len(str) - 1
    while start_i < end_i:
        if str[start_i] == str[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


# Recursive method
def recursive_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[len(str) - 1]:
        return recursive_palindrome(str[1:-1])
    else:
        return False


def main():
    str = "ama"
    print(recursive_palindrome(str.lower()))
    print(is_palindrome(str.lower()))


if __name__ == "__main__":
    main()
