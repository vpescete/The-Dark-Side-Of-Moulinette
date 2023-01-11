import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
library2_path = os.path.join(cwd, 'libft_tester.so')


libft = ctypes.cdll.LoadLibrary(library_path)
libft_tester = ctypes.cdll.LoadLibrary(library2_path)

test_dests = ["CiaoCmondo    ", "", "kjcdbicjbds", "kjcdbicjbds", "kjcdbicjbdsf ihfbi biwu fw98y98n98", "kjcdbicjbds"]
test_ints = [3, 3, 0, 25, 6, 4]
test_sizes = [len(test_dests[0]), len(test_dests[1]), len(test_dests[2]), len(test_dests[3]), len(test_dests[4]) - 5, 3]

test_data = [(test_dests[0], test_ints[0], test_sizes[0]), 
             (test_dests[1], test_ints[1], test_sizes[1]), 
             (test_dests[2], test_ints[2], test_sizes[2]), 
             (test_dests[3], test_ints[3], test_sizes[3]), 
             (test_dests[4], test_ints[4], test_sizes[4]),
             (test_dests[5], test_ints[5], test_sizes[5])]

ids = ["string: {}, int: {}, size: {}".format(t[0], t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_dest, test_int, test_size",test_data, ids=ids)

def test_ft_substr(test_dest, test_int, test_size):

    # Definizione della funzione ft_substr nella libreria
    ft_substr = libft.ft_substr

    # Define the substr function in the library
    substr = libft_tester.substr

    result = ctypes.string_at(ft_substr(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(substr(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    