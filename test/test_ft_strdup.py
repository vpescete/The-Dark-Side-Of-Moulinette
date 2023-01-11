import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings = ["CiaoCmondo    ", "    ", "kjcbdsicbksihcbdskcjbsib1nn\n\n\n\n\n\n\t\t\t\t\t\t\t\t %&$$££%$%$£&$   "]
ids = ["input string: '{}'".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string", test_strings, ids = ids)

def test_ft_strdup(test_string):
    # Define the function ft_strdup in the library
    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_strdup nella libreria
    ft_strdup = libft.ft_strdup

    # Define the strdup function in the library
    strdup = libc.strdup

    result = ctypes.string_at(ft_strdup(test_string_buffer))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strdup(test_string_buffer))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
