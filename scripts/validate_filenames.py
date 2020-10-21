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

import os
from build_directory_md import good_filepaths

filepaths = list(good_filepaths())
assert filepaths, "good_filepaths() failed!"


upper_files = [file for file in filepaths if file != file.lower()]
if upper_files:
    print(f"{len(upper_files)} files contain uppercase characters:")
    print("\n".join(upper_files) + "\n")

space_files = [file for file in filepaths if " " in file]
if space_files:
    print(f"{len(space_files)} files contain space characters:")
    print("\n".join(space_files) + "\n")

nodir_files = [file for file in filepaths if os.sep not in file]
if nodir_files:
    print(f"{len(nodir_files)} files are not in a directory:")
    print("\n".join(nodir_files) + "\n")

bad_files = len(upper_files + space_files + nodir_files)
if bad_files:
    import sys

    sys.exit(bad_files)
