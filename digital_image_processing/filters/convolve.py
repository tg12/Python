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



# @Author  : lightXu
# @File    : convolve.py
# @Time    : 2019/7/8 0008 下午 16:13
from cv2 import imread, cvtColor, COLOR_BGR2GRAY, imshow, waitKey
from numpy import array, zeros, ravel, pad, dot, uint8


def im2col(image, block_size):
    rows, cols = image.shape
    dst_height = cols - block_size[1] + 1
    dst_width = rows - block_size[0] + 1
    image_array = zeros(
        (dst_height *
         dst_width,
         block_size[1] *
         block_size[0]))
    row = 0
    for i in range(0, dst_height):
        for j in range(0, dst_width):
            window = ravel(image[i: i + block_size[0], j: j + block_size[1]])
            image_array[row, :] = window
            row += 1

    return image_array


def img_convolve(image, filter_kernel):
    height, width = image.shape[0], image.shape[1]
    k_size = filter_kernel.shape[0]
    pad_size = k_size // 2
    # Pads image with the edge values of array.
    image_tmp = pad(image, pad_size, mode="edge")

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = im2col(image_tmp, (k_size, k_size))

    #  turn the kernel into shape(k*k, 1)
    kernel_array = ravel(filter_kernel)
    # reshape and get the dst image
    dst = dot(image_array, kernel_array).reshape(height, width)
    return dst


if __name__ == "__main__":
    # read original image
    img = imread(r"../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)
    # Laplace operator
    Laplace_kernel = array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    out = img_convolve(gray, Laplace_kernel).astype(uint8)
    imshow("Laplacian", out)
    waitKey(0)
