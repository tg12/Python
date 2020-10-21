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



"""Password generator allows you to generate a random password of length N."""
from random import choice
from string import ascii_letters, digits, punctuation


def password_generator(length=8):
    """
    >>> len(password_generator())
    8
    >>> len(password_generator(length=16))
    16
    >>> len(password_generator(257))
    257
    >>> len(password_generator(length=0))
    0
    >>> len(password_generator(-1))
    0
    """
    chars = tuple(ascii_letters) + tuple(digits) + tuple(punctuation)
    return "".join(choice(chars) for x in range(length))


# ALTERNATIVE METHODS
# ctbi= characters that must be in password
# i= how many letters or characters the password length will be
def alternative_password_generator(ctbi, i):
    # Password generator = full boot with random_number, random_letters, and
    # random_character FUNCTIONS
    pass  # Put your code here...


def random_number(ctbi, i):
    pass  # Put your code here...


def random_letters(ctbi, i):
    pass  # Put your code here...


def random_characters(ctbi, i):
    pass  # Put your code here...


def main():
    length = int(
        input("Please indicate the max length of your password: ").strip())
    print("Password generated:", password_generator(length))
    print("[If you are thinking of using this passsword, You better save it.]")


if __name__ == "__main__":
    main()
