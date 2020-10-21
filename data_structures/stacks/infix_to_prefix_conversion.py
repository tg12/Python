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

Enter an Infix Equation = a + b ^c
 Symbol  |  Stack  | Postfix
----------------------------
   c     |         | c
   ^     | ^       | c
   b     | ^       | cb
   +     | +       | cb^
   a     | +       | cb^a
         |         | cb^a+

	 a+b^c (Infix) ->  +a^bc (Prefix)
"""


def infix_2_postfix(Infix):
    Stack = []
    Postfix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
    }  # Priority of each operator
    print_width = len(Infix) if (len(Infix) > 7) else 7

    # Print table header for output
    print(
        "Symbol".center(8),
        "Stack".center(print_width),
        "Postfix".center(print_width),
        sep=" | ",
    )
    print("-" * (print_width * 3 + 7))

    for x in Infix:
        if x.isalpha() or x.isdigit():
            Postfix.append(x)  # if x is Alphabet / Digit, add it to Postfix
        elif x == "(":
            Stack.append(x)  # if x is "(" push to Stack
        elif x == ")":  # if x is ")" pop stack until "(" is encountered
            while Stack[-1] != "(":
                # Pop stack & add the content to Postfix
                Postfix.append(Stack.pop())
            Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(x)  # If stack is empty, push x to stack
            else:
                while (
                    len(Stack) > 0 and priority[x] <= priority[Stack[-1]]
                ):  # while priority of x is not greater than priority of element in the stack
                    Postfix.append(Stack.pop())  # pop stack & add to Postfix
                Stack.append(x)  # push x to stack

        print(
            x.center(8),
            ("".join(Stack)).ljust(print_width),
            ("".join(Postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    while len(Stack) > 0:  # while stack is not empty
        Postfix.append(Stack.pop())  # pop stack & add to Postfix
        print(
            " ".center(8),
            ("".join(Stack)).ljust(print_width),
            ("".join(Postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    return "".join(Postfix)  # return Postfix as str


def infix_2_prefix(Infix):
    Infix = list(Infix[::-1])  # reverse the infix equation

    for i in range(len(Infix)):
        if Infix[i] == "(":
            Infix[i] = ")"  # change "(" to ")"
        elif Infix[i] == ")":
            Infix[i] = "("  # change ")" to "("

    return (infix_2_postfix("".join(Infix)))[
        ::-1
    ]  # call infix_2_postfix on Infix, return reverse of Postfix


if __name__ == "__main__":
    Infix = input("\nEnter an Infix Equation = ")  # Input an Infix equation
    Infix = "".join(Infix.split())  # Remove spaces from the input
    print("\n\t", Infix, "(Infix) -> ", infix_2_prefix(Infix), "(Prefix)")
