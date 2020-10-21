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



LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    message = input("Enter message: ")
    key = input("Enter key [alphanumeric]: ")
    mode = input("Encrypt/Decrypt [e/d]: ")

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encryptMessage(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decryptMessage(key, message)

    print("\n%sed message:" % mode.title())
    print(translated)


def encryptMessage(key, message):
    """
    >>> encryptMessage('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    return translateMessage(key, message, "encrypt")


def decryptMessage(key, message):
    """
    >>> decryptMessage('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    return translateMessage(key, message, "decrypt")


def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[keyIndex])
            elif mode == "decrypt":
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return "".join(translated)


if __name__ == "__main__":
    main()
