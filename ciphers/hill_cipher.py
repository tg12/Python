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

Hill Cipher:
The below defined class 'HillCipher' implements the Hill Cipher algorithm.
The Hill Cipher is an algorithm that implements modern linear algebra techniques
In this algortihm, you have an encryption key matrix. This is what will be used
in encoding and decoding your text.

Algortihm:
Let the order of the encryption key be N (as it is a square matrix).
Your text is divided into batches of length N and converted to numerical vectors
by a simple mapping starting with A=0 and so on.

The key is then mulitplied with the newly created batch vector to obtain the
encoded vector. After each multiplication modular 36 calculations are performed
on the vectors so as to bring the numbers between 0 and 36 and then mapped with
their corresponding alphanumerics.

While decrypting, the decrypting key is found which is the inverse of the
encrypting key modular 36. The same process is repeated for decrypting to get
the original message back.

Constraints:
The determinant of the encryption key matrix must be relatively prime w.r.t 36.

Note:
The algorithm implemented in this code considers only alphanumerics in the text.
If the length of the text to be encrypted is not a multiple of the
break key(the length of one batch of letters),the last character of the text
is added to the text until the length of the text reaches a multiple of
the break_key. So the text after decrypting might be a little different than
the original text.

References:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA

"""

import numpy


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


class HillCipher:
    key_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # This cipher takes alphanumerics into account
    # i.e. a total of 36 characters

    def replaceLetters(self, letter): return self.key_string.index(letter)

    def replaceNumbers(self, num): return self.key_string[round(num)]

    # take x and return x % len(key_string)
    modulus = numpy.vectorize(lambda x: x % 36)

    toInt = numpy.vectorize(lambda x: round(x))

    def __init__(self, encrypt_key):
        """
        encrypt_key is an NxN numpy matrix
        """
        self.encrypt_key = self.modulus(
            encrypt_key)  # mod36 calc's on the encrypt key
        self.checkDeterminant()  # validate the determinant of the encryption key
        self.decrypt_key = None
        self.break_key = encrypt_key.shape[0]

    def checkDeterminant(self):
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if gcd(det, len(self.key_string)) != 1:
            raise ValueError(
                "discriminant modular {0} of encryption key({1}) is not co prime w.r.t {2}.\nTry another key.".format(
                    req_l, det, req_l))

    def processText(self, text):
        text = list(text.upper())
        text = [char for char in text if char in self.key_string]

        last = text[-1]
        while len(text) % self.break_key != 0:
            text.append(last)

        return "".join(text)

    def encrypt(self, text):
        text = self.processText(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i: i + self.break_key]
            batch_vec = list(map(self.replaceLetters, batch))
            batch_vec = numpy.matrix([batch_vec]).T
            batch_encrypted = self.modulus(
                self.encrypt_key.dot(batch_vec)).T.tolist()[0]
            encrypted_batch = "".join(
                list(map(self.replaceNumbers, batch_encrypted)))
            encrypted += encrypted_batch

        return encrypted

    def makeDecryptKey(self):
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv
            * numpy.linalg.det(self.encrypt_key)
            * numpy.linalg.inv(self.encrypt_key)
        )

        return self.toInt(self.modulus(inv_key))

    def decrypt(self, text):
        self.decrypt_key = self.makeDecryptKey()
        text = self.processText(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i: i + self.break_key]
            batch_vec = list(map(self.replaceLetters, batch))
            batch_vec = numpy.matrix([batch_vec]).T
            batch_decrypted = self.modulus(
                self.decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted_batch = "".join(
                list(map(self.replaceNumbers, batch_decrypted)))
            decrypted += decrypted_batch

        return decrypted


def main():
    N = int(input("Enter the order of the encryption key: "))
    hill_matrix = []

    print("Enter each row of the encryption key with space separated integers")
    for i in range(N):
        row = list(map(int, input().split()))
        hill_matrix.append(row)

    hc = HillCipher(numpy.matrix(hill_matrix))

    print("Would you like to encrypt or decrypt some text? (1 or 2)")
    option = input(
        """
1. Encrypt
2. Decrypt
"""
    )

    if option == "1":
        text_e = input("What text would you like to encrypt?: ")
        print("Your encrypted text is:")
        print(hc.encrypt(text_e))
    elif option == "2":
        text_d = input("What text would you like to decrypt?: ")
        print("Your decrypted text is:")
        print(hc.decrypt(text_d))


if __name__ == "__main__":
    main()
