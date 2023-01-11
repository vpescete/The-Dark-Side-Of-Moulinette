import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)

libbsd_path = '/lib/x86_64-linux-gnu/libbsd.so.0'
libbsd = ctypes.cdll.LoadLibrary(libbsd_path)

test_strings1 = ["ciaotring2mondo", "ciaotring2mondo", "", "ciaotring2   mondo"]
test_strings2 = ["0", "ciao mondo", "ciao mondo", "ciao mondo"]
test_sizes = [10, 100, 0, 3]

test_data = [(test_strings1[0], test_strings2[0], test_sizes[0]), 
             (test_strings1[1], test_strings2[1], test_sizes[1]), 
             (test_strings1[2], test_strings2[2], test_sizes[2]), 
             (test_strings1[3], test_strings2[3], test_sizes[3])]

ids = ["string: {}, size:{}".format(t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_string1, test_string2, test_size",test_data, ids=ids)

def test_ft_strnstr(test_string1, test_string2, test_size):

    # Definizione della funzione ft_strnstr nella libreria
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr

    result = print(ft_strnstr(test_string1, test_string2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strnstr(test_string1, test_string2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result