import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = [67, 12, 102, 70, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isalpha(test_string):
    # Define the function ft_isalpha in the library
    ft_isalpha = libft.ft_isalpha
    ft_isalpha.restype = ctypes.c_int
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha
    isalpha.restype = ctypes.c_int
    isalpha.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isalpha(test_string)
    original_result = isalpha(test_string)

    # Check that the results are equal
    assert result == original_result
