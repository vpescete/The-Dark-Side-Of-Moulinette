import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = [99, 48, 56, 127, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isdigit(test_string):
    # Define the function ft_isdigit in the library
    ft_isdigit = libft.ft_isdigit
    ft_isdigit.restype = ctypes.c_int
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit
    isdigit.restype = ctypes.c_int
    isdigit.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isdigit(test_string)
    original_result = isdigit(test_string)

    # Check that the results are equal
    assert result == original_result
