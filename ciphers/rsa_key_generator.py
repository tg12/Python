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



import random
import sys
import os
import rabin_miller as rabinMiller
import cryptomath_module as cryptoMath


def main():
    print("Making key files...")
    makeKeyFiles("rsa", 1024)
    print("Key files generation successful.")


def generateKey(keySize):
    print("Generating prime p...")
    p = rabinMiller.generateLargePrime(keySize)
    print("Generating prime q...")
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    print("Generating e that is relatively prime to (p - 1) * (q - 1)...")
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print("Calculating d that is mod inverse of e...")
    d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    if os.path.exists("%s_pubkey.txt" % (name)) or os.path.exists(
        "%s_privkey.txt" % (name)
    ):
        print("\nWARNING:")
        print(
            '"%s_pubkey.txt" or "%s_privkey.txt" already exists. \nUse a different name or delete these files and re-run this program.' %
            (name, name))
        sys.exit()

    publicKey, privateKey = generateKey(keySize)
    print("\nWriting public key to file %s_pubkey.txt..." % name)
    with open("%s_pubkey.txt" % name, "w") as fo:
        fo.write("%s,%s,%s" % (keySize, publicKey[0], publicKey[1]))

    print("Writing private key to file %s_privkey.txt..." % name)
    with open("%s_privkey.txt" % name, "w") as fo:
        fo.write("%s,%s,%s" % (keySize, privateKey[0], privateKey[1]))


if __name__ == "__main__":
    main()
