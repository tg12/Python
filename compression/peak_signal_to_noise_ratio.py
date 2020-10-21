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
	Peak signal-to-noise ratio - PSNR - https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
    Soruce: https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python/
"""

import math
import os

import cv2
import numpy as np


def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Loading images (original image and compressed image)
    original = cv2.imread(
        os.path.join(
            dir_path,
            "image_data/original_image.png"))
    contrast = cv2.imread(
        os.path.join(
            dir_path,
            "image_data/compressed_image.png"),
        1)

    original2 = cv2.imread(
        os.path.join(
            dir_path,
            "image_data/PSNR-example-base.png"))
    contrast2 = cv2.imread(
        os.path.join(dir_path, "image_data/PSNR-example-comp-10.jpg"), 1
    )

    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"PSNR value is {psnr(original, contrast)} dB")

    # # Value expected: 31.53dB (Wikipedia Example)
    print("\n-- Second Test --")
    print(f"PSNR value is {psnr(original2, contrast2)} dB")


if __name__ == "__main__":
    main()
