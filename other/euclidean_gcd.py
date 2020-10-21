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



# https://en.wikipedia.org/wiki/Euclidean_algorithm


def euclidean_gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a


def main():
    print("GCD(3, 5) = " + str(euclidean_gcd(3, 5)))
    print("GCD(5, 3) = " + str(euclidean_gcd(5, 3)))
    print("GCD(1, 3) = " + str(euclidean_gcd(1, 3)))
    print("GCD(3, 6) = " + str(euclidean_gcd(3, 6)))
    print("GCD(6, 3) = " + str(euclidean_gcd(6, 3)))


if __name__ == "__main__":
    main()
