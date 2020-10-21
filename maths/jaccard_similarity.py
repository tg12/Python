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
The Jaccard similarity coefficient is a commonly used indicator of the
similarity between two sets. Let U be a set and A and B be subsets of U,
then the Jaccard index/similarity is defined to be the ratio of the number
of elements of their intersection and the number of elements of their union.

Inspired from Wikipedia and
the book Mining of Massive Datasets [MMDS 2nd Edition, Chapter 3]

https://en.wikipedia.org/wiki/Jaccard_index
https://mmds.org

Jaccard similarity is widely used with MinHashing.
"""


def jaccard_similariy(setA, setB, alternativeUnion=False):
    """
    Finds the jaccard similarity between two sets.
    Essentially, its intersection over union.

    The alternative way to calculate this is to take union as sum of the
    number of items in the two sets. This will lead to jaccard similarity
    of a set with itself be 1/2 instead of 1. [MMDS 2nd Edition, Page 77]

    Parameters:
        :setA (set,list,tuple): A non-empty set/list
        :setB (set,list,tuple): A non-empty set/list
        :alternativeUnion (boolean): If True, use sum of number of
        items as union

    Output:
        (float) The jaccard similarity between the two sets.

    Examples:
    >>> setA = {'a', 'b', 'c', 'd', 'e'}
    >>> setB = {'c', 'd', 'e', 'f', 'h', 'i'}
    >>> jaccard_similariy(setA,setB)
    0.375

    >>> jaccard_similariy(setA,setA)
    1.0

    >>> jaccard_similariy(setA,setA,True)
    0.5

    >>> setA = ['a', 'b', 'c', 'd', 'e']
    >>> setB = ('c', 'd', 'e', 'f', 'h', 'i')
    >>> jaccard_similariy(setA,setB)
    0.375
    """

    if isinstance(setA, set) and isinstance(setB, set):

        intersection = len(setA.intersection(setB))

        if alternativeUnion:
            union = len(setA) + len(setB)
        else:
            union = len(setA.union(setB))

        return intersection / union

    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)):

        intersection = [element for element in setA if element in setB]

        if alternativeUnion:
            union = len(setA) + len(setB)
        else:
            union = setA + [element for element in setB if element not in setA]

        return len(intersection) / len(union)


if __name__ == "__main__":

    setA = {"a", "b", "c", "d", "e"}
    setB = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similariy(setA, setB))
