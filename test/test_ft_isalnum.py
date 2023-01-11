import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = [99, 1, 999, 127, 50]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isalnum(test_string):
    # Define the function ft_isalnum in the library
    ft_isalnum = libft.ft_isalnum
    ft_isalnum.restype = ctypes.c_int
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum
    isalnum.restype = ctypes.c_int
    isalnum.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isalnum(test_string)
    original_result = isalnum(test_string)

    # Check that the results are equal
    assert result == original_result