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
Greatest Common Divisor.

Wikipedia reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def gcd(a, b):
    """Calculate Greatest Common Divisor (GCD)."""
    return b if a == 0 else gcd(b % a, a)


def main():
    """Call GCD Function."""
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(",")
        num_1 = int(nums[0])
        num_2 = int(nums[1])
        print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")


if __name__ == "__main__":
    main()
