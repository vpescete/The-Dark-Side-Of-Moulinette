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

test_ints = [4359, 43595, -4385309, -34658342, 0, -2147483648]

ids = ["input: '{}'".format(t) for t in test_ints]
@pytest.mark.parametrize("test_int", test_ints, ids = ids)

def test_ft_itoa(test_int):
    # Define the function ft_itoa in the library
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))
    
    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result