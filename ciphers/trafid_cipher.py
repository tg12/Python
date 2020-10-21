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



# https://en.wikipedia.org/wiki/Trifid_cipher


def __encryptPart(messagePart, character2Number):
    one, two, three = "", "", ""
    tmp = []

    for character in messagePart:
        tmp.append(character2Number[character])

    for each in tmp:
        one += each[0]
        two += each[1]
        three += each[2]

    return one + two + three


def __decryptPart(messagePart, character2Number):
    tmp, thisPart = "", ""
    result = []

    for character in messagePart:
        thisPart += character2Number[character]

    for digit in thisPart:
        tmp += digit
        if len(tmp) == len(messagePart):
            result.append(tmp)
            tmp = ""

    return result[0], result[1], result[2]


def __prepare(message, alphabet):
    # Validate message and alphabet, set to upper and remove spaces
    alphabet = alphabet.replace(" ", "").upper()
    message = message.replace(" ", "").upper()

    # Check length and characters
    if len(alphabet) != 27:
        raise KeyError("Length of alphabet has to be 27.")
    for each in message:
        if each not in alphabet:
            raise ValueError(
                "Each message character has to be included in alphabet!")

    # Generate dictionares
    numbers = (
        "111",
        "112",
        "113",
        "121",
        "122",
        "123",
        "131",
        "132",
        "133",
        "211",
        "212",
        "213",
        "221",
        "222",
        "223",
        "231",
        "232",
        "233",
        "311",
        "312",
        "313",
        "321",
        "322",
        "323",
        "331",
        "332",
        "333",
    )
    character2Number = {}
    number2Character = {}
    for letter, number in zip(alphabet, numbers):
        character2Number[letter] = number
        number2Character[number] = letter

    return message, alphabet, character2Number, number2Character


def encryptMessage(message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    message, alphabet, character2Number, number2Character = __prepare(
        message, alphabet)
    encrypted, encrypted_numeric = "", ""

    for i in range(0, len(message) + 1, period):
        encrypted_numeric += __encryptPart(
            message[i: i + period], character2Number)

    for i in range(0, len(encrypted_numeric), 3):
        encrypted += number2Character[encrypted_numeric[i: i + 3]]

    return encrypted


def decryptMessage(message, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    message, alphabet, character2Number, number2Character = __prepare(
        message, alphabet)
    decrypted_numeric = []
    decrypted = ""

    for i in range(0, len(message) + 1, period):
        a, b, c = __decryptPart(message[i: i + period], character2Number)

        for j in range(0, len(a)):
            decrypted_numeric.append(a[j] + b[j] + c[j])

    for each in decrypted_numeric:
        decrypted += number2Character[each]

    return decrypted


if __name__ == "__main__":
    msg = "DEFEND THE EAST WALL OF THE CASTLE."
    encrypted = encryptMessage(msg, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    decrypted = decryptMessage(encrypted, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print("Encrypted: {}\nDecrypted: {}".format(encrypted, decrypted))
