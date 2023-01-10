import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_data = [
    ["hello world", ord('w')],
    ["hello world", ord('z')],
    ["", ord('a')],
    ["\x00hello world", ord('\x00')],
    ["", ord('h')]
]

@pytest.mark.parametrize("test_src, test_char",test_data, ids=[f"string: {t[0]}, char:{chr(t[1])}" for t in test_data])
def test_ft_strchr(test_src, test_char):
    ft_strchr = libft.ft_strchr
    strchr = libc.strchr

    test_src = bytes(test_src, 'utf-8')
    
    result = print(ft_strchr(test_src, test_char))
    original_result = print(strchr(test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result 