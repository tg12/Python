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
Output:

Enter a Postfix Equation (space separated) = 5 6 9 * +
 Symbol  |    Action    | Stack
-----------------------------------
       5 | push(5)      | 5
       6 | push(6)      | 5,6
       9 | push(9)      | 5,6,9
         | pop(9)       | 5,6
         | pop(6)       | 5
       * | push(6*9)    | 5,54
         | pop(54)      | 5
         | pop(5)       |
       + | push(5+54)   | 59

	Result =  59
"""

import operator as op


def Solve(Postfix):
    Stack = []

    def Div(x, y): return int(x / y)  # integer division operation
    Opr = {
        "^": op.pow,
        "*": op.mul,
        "/": Div,
        "+": op.add,
        "-": op.sub,
    }  # operators & their respective operation

    # print table header
    print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
    print("-" * (30 + len(Postfix)))

    for x in Postfix:
        if x.isdigit():  # if x in digit
            Stack.append(x)  # append x to stack
            print(
                x.rjust(8), ("push(" + x + ")").ljust(12), ",".join(Stack), sep=" | "
            )  # output in tabular format
        else:
            B = Stack.pop()  # pop stack
            print(
                "".rjust(8), ("pop(" + B + ")").ljust(12), ",".join(Stack), sep=" | "
            )  # output in tabular format

            A = Stack.pop()  # pop stack
            print(
                "".rjust(8), ("pop(" + A + ")").ljust(12), ",".join(Stack), sep=" | "
            )  # output in tabular format

            Stack.append(
                str(Opr[x](int(A), int(B)))
            )  # evaluate the 2 values poped from stack & push result to stack
            print(
                x.rjust(8),
                ("push(" + A + x + B + ")").ljust(12),
                ",".join(Stack),
                sep=" | ",
            )  # output in tabular format

    return int(Stack[0])


if __name__ == "__main__":
    Postfix = input(
        "\n\nEnter a Postfix Equation (space separated) = ").split(" ")
    print("\n\tResult = ", Solve(Postfix))
