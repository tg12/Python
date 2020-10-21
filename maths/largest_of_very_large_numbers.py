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



# Author: Abhijeeth S

import math


def res(x, y):
    if 0 not in (x, y):
        # We use the relation x^y = y*log10(x), where 10 is the base.
        return y * math.log10(x)
    else:
        if x == 0:  # 0 raised to any number is 0
            return 0
        elif y == 0:
            return 1  # any number raised to 0 is 1


if __name__ == "__main__":  # Main function
    # Read two numbers from input and typecast them to int using map function.
    # Here x is the base and y is the power.
    prompt = "Enter the base and the power separated by a comma: "
    x1, y1 = map(int, input(prompt).split(","))
    x2, y2 = map(int, input(prompt).split(","))

    # We find the log of each number, using the function res(), which takes two
    # arguments.
    res1 = res(x1, y1)
    res2 = res(x2, y2)

    # We check for the largest number
    if res1 > res2:
        print("Largest number is", x1, "^", y1)
    elif res2 > res1:
        print("Largest number is", x2, "^", y2)
    else:
        print("Both are equal")
