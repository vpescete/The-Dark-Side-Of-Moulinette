import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_memchr():

    # input function
    test_string = "    +18329jchdbckjdhb"
    test_char = 'a'
    test_size = len(test_string)

    # Definizione della funzione ft_memchr nella libreria
    ft_memchr = libft.ft_memchr

    # Define the memchr function in the library
    memchr = libc.memchr

    result = ft_memchr(test_String, test_char, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = memchr(test_String, test_char, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result