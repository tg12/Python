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
This script demonstrates the implementation of the Softmax function.

Its a function that takes as input a vector of K real numbers, and normalizes
it into a probability distribution consisting of K probabilities proportional
to the exponentials of the input numbers. After softmax, the elements of the
vector always sum up to 1.

Script inspired from its corresponding Wikipedia article
https://en.wikipedia.org/wiki/Softmax_function
"""

import numpy as np


def softmax(vector):
    """
        Implements the softmax function

        Parameters:
            vector (np.array,list,tuple): A  numpy array of shape (1,n)
            consisting of real values or a similar list,tuple


        Returns:
            softmax_vec (np.array): The input numpy array  after applying
            softmax.

        The softmax vector adds up to one. We need to ceil to mitigate for
        precision
        >>> np.ceil(np.sum(softmax([1,2,3,4])))
        1.0

        >>> vec = np.array([5,5])
        >>> softmax(vec)
        array([0.5, 0.5])

        >>> softmax([0])
        array([1.])
    """

    # Calculate e^x for each x in your vector where e is Euler's
    # number (approximately 2.718)
    exponentVector = np.exp(vector)

    # Add up the all the exponentials
    sumOfExponents = np.sum(exponentVector)

    # Divide every exponent by the sum of all exponents
    softmax_vector = exponentVector / sumOfExponents

    return softmax_vector


if __name__ == "__main__":
    print(softmax((0,)))
