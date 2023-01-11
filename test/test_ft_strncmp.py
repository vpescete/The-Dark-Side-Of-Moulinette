import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

test_strings1 = ["Hello ", "    Ciao mondo", "Porco", "Ciao", ""]
test_strings2 = ["Hello ", " Ciao modno", "    Dio", "       Stronzo", "+1832dejdn idneibewfiuewh 9jchdbckjdhb"]

test_data = [(test_strings1[0], test_strings2[0]), 
             (test_strings1[1], test_strings2[1]), 
             (test_strings1[2], test_strings2[2]), 
             (test_strings1[3], test_strings2[3]), 
             (test_strings1[4], test_strings2[4])]

ids = ["string: '{}', string_2: '{}'".format(t[0], t[1]) for t in test_data]
@pytest.mark.parametrize("test_string, test_string2",test_data, ids=ids)

def test_ft_strncmp(test_string, test_string2):

    # Definizione della funzione ft_strncmp nella libreria
    ft_strncmp = libft.ft_strncmp

    # Define the strncmp function in the library
    strncmp = libc.strncmp

    result = print(ft_strncmp( test_string, test_string2))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strncmp( test_string, test_string2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result