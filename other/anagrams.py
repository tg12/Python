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



import collections
import pprint
import time
import os

start_time = time.time()
print("creating word list...")
path = os.path.split(os.path.realpath(__file__))
with open(path[0] + "/words") as f:
    word_list = sorted(list(set([word.strip().lower() for word in f])))


def signature(word):
    return "".join(sorted(word))


word_bysig = collections.defaultdict(list)
for word in word_list:
    word_bysig[signature(word)].append(word)


def anagram(myword):
    return word_bysig[signature(myword)]


print("finding anagrams...")
all_anagrams = {word: anagram(word)
                for word in word_list if len(anagram(word)) > 1}

print("writing anagrams to file...")
with open("anagrams.txt", "w") as file:
    file.write("all_anagrams = ")
    file.write(pprint.pformat(all_anagrams))

total_time = round(time.time() - start_time, 2)
print(("Done [", total_time, "seconds ]"))
