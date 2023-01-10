import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = ["ciao mondo", "", "    +-18329jchdbckjdhb", "ciao mondo               ", "ciao    \n mondo", "    -+18329234987298472904802498", "    + 18329234987298472904802498", "c"]
ids = ["input: '{}'".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string", test_strings, ids = ids)
def test_ft_strlen(test_string):
    # Define the function ft_strlen in the library
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    # Run the test
    result = ft_strlen(test_string)
    original_result = strlen(test_string)

    # Check that the results are equal
    assert result == original_result

