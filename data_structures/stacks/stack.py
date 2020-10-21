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



__author__ = "Omkar Pathak"


class Stack(object):
    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).

    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)


class StackOverflowError(BaseException):
    pass


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print("Stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))
