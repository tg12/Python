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
import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    message = input("Enter message: ")
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    resp = input("Encrypt/Decrypt [e/d]: ")

    checkValidKey(key)

    if resp.lower().startswith("e"):
        mode = "encrypt"
        translated = encryptMessage(key, message)
    elif resp.lower().startswith("d"):
        mode = "decrypt"
        translated = decryptMessage(key, message)

    print("\n%sion: \n%s" % (mode.title(), translated))


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    if keyList != lettersList:
        sys.exit("Error in the key or symbol set.")


def encryptMessage(key, message):
    """
    >>> encryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translateMessage(key, message, "encrypt")


def decryptMessage(key, message):
    """
    >>> decryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return translateMessage(key, message, "decrypt")


def translateMessage(key, message, mode):
    translated = ""
    charsA = LETTERS
    charsB = key

    if mode == "decrypt":
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)


if __name__ == "__main__":
    main()
