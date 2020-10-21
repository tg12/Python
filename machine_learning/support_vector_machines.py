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



from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.model_selection import train_test_split
import doctest

# different functions implementing different types of SVM's


def NuSVC(train_x, train_y):
    svc_NuSVC = svm.NuSVC()
    svc_NuSVC.fit(train_x, train_y)
    return svc_NuSVC


def Linearsvc(train_x, train_y):
    svc_linear = svm.LinearSVC()
    svc_linear.fit(train_x, train_y)
    return svc_linear


def SVC(train_x, train_y):
    # svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, random_state=None)
    # various parameters like "kernal","gamma","C" can effectively tuned for a
    # given machine learning model.
    SVC = svm.SVC(gamma="auto")
    SVC.fit(train_x, train_y)
    return SVC


def test(X_new):
    """
    3 test cases to be passed
    an array containing the sepal length (cm), sepal width (cm),petal length (cm),petal width (cm)
    based on which  the target name will be predicted
    >>> test([1,2,1,4])
    'virginica'
    >>> test([5, 2, 4, 1])
    'versicolor'
    >>> test([6,3,4,1])
    'versicolor'

    """
    iris = load_iris()
    # splitting the dataset to test and train
    train_x, test_x, train_y, test_y = train_test_split(
        iris["data"], iris["target"], random_state=4
    )
    # any of the 3 types of SVM can be used
    # current_model=SVC(train_x, train_y)
    # current_model=NuSVC(train_x, train_y)
    current_model = Linearsvc(train_x, train_y)
    prediction = current_model.predict([X_new])
    return iris["target_names"][prediction][0]


if __name__ == "__main__":
    doctest.testmod()
