import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = ["    +18329jchdbckjdhb", "    +18329jchdbckjdhb", "     +18329jchdbckjdhb", "    +18329jchdbckjdhb", "", "    "]
test_chars = ['a', '+', '    ', 'k', '+', "+"]
test_sizes = [len(test_strings[0]), len(test_strings[1]), len(test_strings[2]), len(test_strings[3]), len(test_strings[4]), len(test_strings[5])]

test_data = [(test_strings[0], test_chars[0], test_sizes[0]), 
             (test_strings[1], test_chars[1], test_sizes[1]), 
             (test_strings[2], test_chars[2], test_sizes[2]), 
             (test_strings[3], test_chars[3], test_sizes[3]), 
             (test_strings[4], test_chars[4], test_sizes[4]),
             (test_strings[5], test_chars[5], test_sizes[5])]

ids = ["string: {}, char:{}, size:{}".format(t[0], t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_string, test_char, test_size",test_data, ids=ids)


# @pytest.mark.parametrize("test_string, test_char, test_size",test_data, ids=["string: {}, char:{}, size:{}".format(test_string, test_char, test_size)])

def test_ft_memchr(test_string, test_char, test_size):

    # Definizione della funzione ft_memchr nella libreria
    ft_memchr = libft.ft_memchr

    # Define the memchr function in the library
    memchr = libc.memchr

    result = ft_memchr(test_string, test_char, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = memchr(test_string, test_char, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
