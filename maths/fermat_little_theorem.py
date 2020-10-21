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



# Python program to show the usage of Fermat's little theorem in a division
# According to Fermat's little theorem, (a / b) mod p always equals a * (b ^ (p - 2)) mod p
# Here we assume that p is a prime number, b divides a, and p doesn't divide b
# Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem


def binary_exponentiation(a, n, mod):

    if n == 0:
        return 1

    elif n % 2 == 1:
        return (binary_exponentiation(a, n - 1, mod) * a) % mod

    else:
        b = binary_exponentiation(a, n / 2, mod)
        return (b * b) % mod


# a prime number
p = 701

a = 1000000000
b = 10

# using binary exponentiation function, O(log(p)):
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p)

# using Python operators:
print((a / b) % p == (a * b ** (p - 2)) % p)
