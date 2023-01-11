import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = [32, 127, 33, 10, 6, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isascii(test_string):
    # Define the function ft_isascii in the library
    ft_isascii = libft.ft_isascii
    ft_isascii.restype = ctypes.c_int
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii
    isascii.restype = ctypes.c_int
    isascii.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isascii(test_string)
    original_result = isascii(test_string)

    # Check that the results are equal
    assert result == original_result
