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

test_strings1 = ["Hello ", "    Ciao mondo", "Porco", "Ciao", "", ""]
test_toattachs = ["World", " fanculo", "    Dio", "                                     Stronzo", "", "Matteo e' stronzo"]

test_data = [(test_strings1[0], test_toattachs[0]), 
             (test_strings1[1], test_toattachs[1]), 
             (test_strings1[2], test_toattachs[2]), 
             (test_strings1[3], test_toattachs[3]), 
             (test_strings1[4], test_toattachs[4]),
             (test_strings1[5], test_toattachs[5])]

ids = ["string: '{}', to_attach: '{}'".format(t[0], t[1]) for t in test_data]
@pytest.mark.parametrize("test_string, test_toattach",test_data, ids=ids)

def test_ft_strjoin(test_string, test_toattach):

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())
    
    # Definizione della funzione ft_strjoin nella libreria
    ft_strjoin = libft.ft_strjoin

    # Define the strjoin function in the library
    strjoin = libft_tester.strjoin

    result = ctypes.string_at(ft_strjoin(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strjoin(test_string_buffer, test_string_buffer2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

