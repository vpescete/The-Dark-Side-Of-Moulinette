import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = ["    +18329jchdbckjdhb", "    -18329jchdbckjdhb", "    +-18329jchdbckjdhb", "    +18329234987298472904802498", "    -18329234987298472904802498", "    -+18329234987298472904802498", "    + 18329234987298472904802498"]
ids = ["input: '{}'".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string", test_strings, ids = ids)
def test_ft_atoi(test_string):
    # Define the function ft_atoi in the library
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    # Run the test
    result = ft_atoi(test_string)
    original_result = atoi(test_string)

    # Check that the results are equal
    assert result == original_result
