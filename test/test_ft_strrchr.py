import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_strrchr():

    # input function
    test_src = "ciao mondo"
    test_char = 99

    # Definizione della funzione ft_strrchr nella libreria
    ft_strrchr = libft.ft_strrchr

    # Define the strrchr function in the library
    strrchr = libc.strrchr

    result = ft_strrchr( test_src, test_char)
    
    # chiamare la funzione originale con i dati di input
    original_result = strrchr( test_src, test_char)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result