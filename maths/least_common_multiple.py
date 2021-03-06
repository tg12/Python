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



import unittest


def find_lcm(first_num: int, second_num: int) -> int:
    """Find the least common multiple of two numbers.

       Learn more: https://en.wikipedia.org/wiki/Least_common_multiple

       >>> find_lcm(5,2)
       10
       >>> find_lcm(12,76)
       228
    """
    max_num = first_num if first_num >= second_num else second_num
    common_mult = max_num
    while (common_mult % first_num > 0) or (common_mult % second_num > 0):
        common_mult += max_num
    return common_mult


class TestLeastCommonMultiple(unittest.TestCase):

    test_inputs = [
        (10, 20),
        (13, 15),
        (4, 31),
        (10, 42),
        (43, 34),
        (5, 12),
        (12, 25),
        (10, 25),
        (6, 9),
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18]

    def test_lcm_function(self):
        for i, (first_num, second_num) in enumerate(self.test_inputs):
            actual_result = find_lcm(first_num, second_num)
            with self.subTest(i=i):
                self.assertEqual(actual_result, self.expected_results[i])


if __name__ == "__main__":
    unittest.main()
