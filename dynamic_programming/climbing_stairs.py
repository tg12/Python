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



#!/usr/bin/env python3


def climb_stairs(n: int) -> int:
    """
    LeetCdoe No.70: Climbing Stairs
    Distinct ways to climb a n step staircase where
    each time you can either climb 1 or 2 steps.

    Args:
        n: number of steps of staircase

    Returns:
        Distinct ways to climb a n step staircase

    Raises:
        AssertionError: n not positive integer

    >>> climb_stairs(3)
    3
    >>> climb_stairs(1)
    1
    >>> climb_stairs(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: n needs to be positive integer, your input -7
    """
    fmt = "n needs to be positive integer, your input {}"
    assert isinstance(n, int) and n > 0, fmt.format(n)
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = (1, 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
