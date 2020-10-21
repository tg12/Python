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



from .stack import Stack

__author__ = "Omkar Pathak"


def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses is balanced."""
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == "(":
            stack.push(parenthesis)
        elif parenthesis == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        print(example + ": " + str(balanced_parentheses(example)))
