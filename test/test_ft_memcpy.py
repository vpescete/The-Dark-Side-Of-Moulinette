import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_dests = ["                       ", "   ", "              ", "                                                  ", "                          "]
test_strings2 = ["  +18329jchdbckjdhb", "os", "ciao mondo", "                             ciao mondo", "+18329jchdbckjdhb"]
test_sizes = [len(test_strings2[0]), len(test_strings2[1]), len(test_strings2[2]), len(test_strings2[3]), len(test_strings2[4])]

test_data = [(test_dests[0], test_strings2[0], test_sizes[0]), 
             (test_dests[0], test_strings2[1], test_sizes[1]), 
             (test_dests[0], test_strings2[2], test_sizes[2]), 
             (test_dests[0], test_strings2[3], test_sizes[3]), 
             (test_dests[0], test_strings2[4], test_sizes[4])]

ids = ["string: {}, size:{}".format(t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_dest, test_string2, test_size",test_data, ids=ids)

def test_ft_memcpy(test_dest, test_string2, test_size):

    # Definizione della funzione ft_memcpy nella libreria
    ft_memcpy = libft.ft_memcpy

    # Define the memcpy function in the library
    memcpy = libc.memcpy

    result = print(ft_memcpy(test_dest, test_string2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memcpy(test_dest, test_string2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result