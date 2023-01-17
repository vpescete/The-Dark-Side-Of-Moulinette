import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.dylib')

test_data = [
    ["hello world\x00", ord('w')],
    ["hello world\x00", ord('z')],
    ["\x00", ord('a')],
    ["\x00hello world\x00", ord('\x00')],
    ["\x00", ord('h')],
    ["hello world\x00", ord('h')]
]

@pytest.mark.parametrize("test_src, test_char",test_data, ids=[f"string: {t[0]}, char:{chr(t[1])}" for t in test_data])
def test_ft_strrchr(test_src, test_char):
    ft_strrchr = libft.ft_strrchr
    strrchr = libc.strrchr

    test_src = bytes(test_src, 'utf-8')
    
    result = ft_strrchr(test_src, test_char)
    original_result = strrchr(test_src, test_char)
    
    assert hex(result) == hex(original_result)
