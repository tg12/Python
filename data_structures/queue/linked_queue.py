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



""" A Queue using a Linked List like structure """
from typing import Any, Optional


class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None):
        self.data: Any = data
        self.next: Optional["Node"] = next


class LinkedQueue:
    """
    Linked List Queue implementing put (to end of queue),
    get (from front of queue) and is_empty

    >>> queue = LinkedQueue()
    >>> queue.is_empty()
    True
    >>> queue.put(5)
    >>> queue.put(9)
    >>> queue.put('python')
    >>> queue.is_empty();
    False
    >>> queue.get()
    5
    >>> queue.put('algorithms')
    >>> queue.get()
    9
    >>> queue.get()
    'python'
    >>> queue.get()
    'algorithms'
    >>> queue.is_empty()
    True
    >>> queue.get()
    Traceback (most recent call last):
        ...
    IndexError: get from empty queue
    """

    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None

    def is_empty(self) -> bool:
        """ returns boolean describing if queue is empty """
        return self.front is None

    def put(self, item: Any) -> None:
        """ append item to rear of queue """
        node: Node = Node(item)
        if self.is_empty():
            # the queue contains just the single element
            self.front = node
            self.rear = node
        else:
            # not empty, so we add it to the rear of the queue
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def get(self) -> Any:
        """ returns and removes item at front of queue """
        if self.is_empty():
            raise IndexError("get from empty queue")
        else:
            # "remove" element by having front point to the next one
            assert isinstance(self.front, Node)
            node: Node = self.front
            self.front = node.next
            if self.front is None:
                self.rear = None

            return node.data
