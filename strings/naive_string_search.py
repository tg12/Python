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
this algorithm tries to find the pattern from every position of
the mainString if pattern is found from position i it add it to
the answer and does the same for position i+1

Complexity : O(n*m)
    n=length of main string
    m=length of pattern string
"""


def naivePatternSearch(mainString, pattern):
    patLen = len(pattern)
    strLen = len(mainString)
    position = []
    for i in range(strLen - patLen + 1):
        match_found = True
        for j in range(patLen):
            if mainString[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position


mainString = "ABAAABCDBBABCDDEBCABC"
pattern = "ABC"
position = naivePatternSearch(mainString, pattern)
print("Pattern found in position ")
for x in position:
    print(x)
