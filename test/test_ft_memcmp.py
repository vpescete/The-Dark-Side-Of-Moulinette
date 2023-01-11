import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings1 = ["    +18329jchdbckjdhb", "    Ciao mondo", "Ciao mondo", "    Ciao mondo", "", "Ciao mondo"]
test_strings2 = ["  +18329jchdbckjdhb", "    +18329jchdbckjdhb", "    +18329jchdbckjdhb", "+18329jchdbckjdhb", "+18329jchdbckjdhb", "Ciao mondo"]
test_sizes = [len(test_strings1[0]), len(test_strings1[1]), len(test_strings1[2]), len(test_strings1[3]), len(test_strings1[4]), len(test_strings1[5])]

test_data = [(test_strings1[0], test_strings2[0], test_sizes[0]), 
             (test_strings1[1], test_strings2[1], test_sizes[1]), 
             (test_strings1[2], test_strings2[2], test_sizes[2]), 
             (test_strings1[3], test_strings2[3], test_sizes[3]), 
             (test_strings1[4], test_strings2[4], test_sizes[4]),
             (test_strings1[5], test_strings2[5], test_sizes[5])]

ids = ["string: {}, char:{}, size:{}".format(t[0], t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_string1, test_string2, test_size",test_data, ids=ids)

def test_ft_memcmp(test_string1, test_string2, test_size):

    # Definizione della funzione ft_memcmp nella libreria
    ft_memcmp = libft.ft_memcmp

    # Define the memcmp function in the library
    memcmp = libc.memcmp

    result = ft_memcmp(test_string1, test_string2, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = memcmp(test_string1, test_string2, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result