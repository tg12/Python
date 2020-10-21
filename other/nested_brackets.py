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
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

	- s is empty
	- s has the form (U) or [U] or {U} where U is a properly nested string
	- s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of brackets and
returns true if S is nested and false otherwise.

"""


def is_balanced(S):

    stack = []
    open_brackets = set({"(", "[", "{"})
    closed_brackets = set({")", "]", "}"})
    open_to_closed = dict({"{": "}", "[": "]", "(": ")"})

    for i in range(len(S)):

        if S[i] in open_brackets:
            stack.append(S[i])

        elif S[i] in closed_brackets:
            if len(stack) == 0 or (
                len(stack) > 0 and open_to_closed[stack.pop()] != S[i]
            ):
                return False

    return len(stack) == 0


def main():

    S = input("Enter sequence of brackets: ")

    if is_balanced(S):
        print((S, "is balanced"))

    else:
        print((S, "is not balanced"))


if __name__ == "__main__":
    main()
