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



import time
import os
import sys
import transposition_cipher as transCipher


def main():
    inputFile = "Prehistoric Men.txt"
    outputFile = "Output.txt"
    key = int(input("Enter key: "))
    mode = input("Encrypt/Decrypt [e/d]: ")

    if not os.path.exists(inputFile):
        print("File %s does not exist. Quitting..." % inputFile)
        sys.exit()
    if os.path.exists(outputFile):
        print("Overwrite %s? [y/n]" % outputFile)
        response = input("> ")
        if not response.lower().startswith("y"):
            sys.exit()

    startTime = time.time()
    if mode.lower().startswith("e"):
        with open(inputFile) as f:
            content = f.read()
        translated = transCipher.encryptMessage(key, content)
    elif mode.lower().startswith("d"):
        with open(outputFile) as f:
            content = f.read()
        translated = transCipher.decryptMessage(key, content)

    with open(outputFile, "w") as outputObj:
        outputObj.write(translated)

    totalTime = round(time.time() - startTime, 2)
    print(("Done (", totalTime, "seconds )"))


if __name__ == "__main__":
    main()
