import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = [110, 90, 99, 67, 127]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_toupper(test_string):
    # Define the function ft_toupper in the library
    ft_toupper = libft.ft_toupper
    ft_toupper.restype = ctypes.c_int
    ft_toupper.argtypes = [ctypes.c_int]

    # Define the toupper function in the library
    toupper = libc.toupper
    toupper.restype = ctypes.c_int
    toupper.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_toupper(test_string)
    original_result = toupper(test_string)

    # Check that the results are equal
    assert result == original_result