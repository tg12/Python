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
import rsa_key_generator as rkg
import os

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def main():
    filename = "encrypted_file.txt"
    response = input(r"Encrypte\Decrypt [e\d]: ")

    if response.lower().startswith("e"):
        mode = "encrypt"
    elif response.lower().startswith("d"):
        mode = "decrypt"

    if mode == "encrypt":
        if not os.path.exists("rsa_pubkey.txt"):
            rkg.makeKeyFiles("rsa", 1024)

        message = input("\nEnter message: ")
        pubKeyFilename = "rsa_pubkey.txt"
        print("Encrypting and writing to %s..." % (filename))
        encryptedText = encryptAndWriteToFile(
            filename, pubKeyFilename, message)

        print("\nEncrypted text:")
        print(encryptedText)

    elif mode == "decrypt":
        privKeyFilename = "rsa_privkey.txt"
        print("Reading from %s and decrypting..." % (filename))
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
        print("writing decryption to rsa_decryption.txt...")
        with open("rsa_decryption.txt", "w") as dec:
            dec.write(decryptedText)

        print("\nDecryption:")
        print(decryptedText)


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    messageBytes = message.encode("ascii")

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(
            blockStart, min(
                blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return "".join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(
        encryptedBlocks,
        messageLength,
        key,
        blockSize=DEFAULT_BLOCK_SIZE):
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    with open(keyFilename) as fo:
        content = fo.read()
    keySize, n, EorD = content.split(",")
    return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(
    messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE
):
    keySize, n, e = readKeyFile(keyFilename)
    if keySize < blockSize * 8:
        sys.exit(
            "ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys." %
            (blockSize * 8, keySize))

    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ",".join(encryptedBlocks)
    encryptedContent = "%s_%s_%s" % (len(message), blockSize, encryptedContent)
    with open(messageFilename, "w") as fo:
        fo.write(encryptedContent)
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    keySize, n, d = readKeyFile(keyFilename)
    with open(messageFilename) as fo:
        content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split("_")
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if keySize < blockSize * 8:
        sys.exit(
            "ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?" %
            (blockSize * 8, keySize))

    encryptedBlocks = []
    for block in encryptedMessage.split(","):
        encryptedBlocks.append(int(block))

    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


if __name__ == "__main__":
    main()
