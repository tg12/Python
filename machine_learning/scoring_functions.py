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



import numpy as np

""" Here I implemented the scoring functions.
    MAE, MSE, RMSE, RMSLE are included.

    Those are used for calculating differences between
    predicted values and actual values.

    Metrics are slightly differentiated. Sometimes squared, rooted,
    even log is used.

    Using log and roots can be perceived as tools for penalizing big
    erors. However, using appropriate metrics depends on the situations,
    and types of data
"""

# Mean Absolute Error


def mae(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> np.around(mae(predict,actual),decimals = 2)
    0.67

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> mae(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    score = difference.mean()

    return score


# Mean Squared Error
def mse(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> np.around(mse(predict,actual),decimals = 2)
    1.33

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> mse(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score


# Root Mean Squared Error
def rmse(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> np.around(rmse(predict,actual),decimals = 2)
    1.15

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> rmse(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score


# Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [10,10,30];predict = [10,2,30]
    >>> np.around(rmsle(predict,actual),decimals = 2)
    0.75

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> rmsle(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict + 1)
    log_actual = np.log(actual + 1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score


# Mean Bias Deviation
def mbd(predict, actual):
    """
    This value is Negative, if the model underpredicts,
    positive, if it overpredicts.

    Example(rounded for precision):

    Here the model overpredicts
    >>> actual = [1,2,3];predict = [2,3,4]
    >>> np.around(mbd(predict,actual),decimals = 2)
    50.0

    Here the model underpredicts
    >>> actual = [1,2,3];predict = [0,1,1]
    >>> np.around(mbd(predict,actual),decimals = 2)
    -66.67
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    denumerator = np.sum(actual) / len(predict)
    # print(numerator, denumerator)
    score = float(numerator) / denumerator * 100

    return score
