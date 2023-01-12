import ctypes
import os
import pytest

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

input_lists = [bytearray([0, 1, 2, 3, 4]), bytearray([0]), bytearray([0, 0, 0 ,0 ,0]), bytearray([0, 1]), bytearray([])]
ids = ["input: '{}'".format(t) for t in input_lists]
@pytest.mark.parametrize("input_list", input_lists, ids = ids)

def test_ft_bzero(input_list):
    # Test input
    input_l = input_list
    input_buf = ctypes.create_string_buffer(bytes(input_l))
    input_ptr = ctypes.cast(input_buf, ctypes.POINTER(ctypes.c_byte))
    input_len = len(input_l)
    
    # Define the ft_bzero function
    ft_bzero = libft.ft_bzero
    bzero = libc.bzero

    result = ft_bzero(input_ptr, input_len)
    original_result = bzero(input_ptr, input_len)

    # Check that all bytes in the input_buf are set to 0
    input_buf_str = ctypes.string_at(input_ptr, input_len)
    assert input_buf_str.count(0) == input_len
    assert all(i == 0 for i in input_buf_str)
    assert result == original_result