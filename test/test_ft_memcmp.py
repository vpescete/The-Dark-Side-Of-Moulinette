import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_memcmp():

    # input function
    test_string = "    +18329jchdbckjdhb"
    test_string2 = "    +18329jchdbckjdhb"
    test_size = len(test_string)

    # Definizione della funzione ft_memcmp nella libreria
    ft_memcmp = libft.ft_memcmp

    # Define the memcmp function in the library
    memcmp = libc.memcmp

    result = ft_memcmp(test_String, test_string2, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = memcmp(test_String, test_string2, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result