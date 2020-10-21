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



from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load iris file
iris = load_iris()
iris.keys()


print("Target names: \n {} ".format(iris.target_names))
print("\n Features: \n {}".format(iris.feature_names))

# Train set e Test set
X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state=4
)

# KNN

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# new array to test
X_new = [[1, 2, 1, 4], [2, 3, 4, 5]]

prediction = knn.predict(X_new)

print(
    "\nNew array: \n {}"
    "\n\nTarget Names Prediction: \n {}".format(
        X_new,
        iris["target_names"][prediction]))
