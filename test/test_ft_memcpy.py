import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_memcpy():

    # input function
    test_dest = ""
    test_src = "ciao mondo"
    test_size = len(test_dest)

    # Definizione della funzione ft_memcpy nella libreria
    ft_memcpy = libft.ft_memcpy

    # Define the memcpy function in the library
    memcpy = libc.memcpy

    result = ft_memcpy(test_dest, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = memcpy(test_dest, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result