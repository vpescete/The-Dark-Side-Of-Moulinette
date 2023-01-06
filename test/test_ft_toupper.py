import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_toupper():

    # input function
    test_string = 99

    # Definizione della funzione ft_toupper nella libreria
    ft_toupper = libft.ft_toupper

    # Specify the return type (int in this case)
    ft_toupper.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_toupper.argtypes = [ctypes.c_int]

    # Define the toupper function in the library
    toupper = libc.toupper

     # Specify the return type (int in this case)
    toupper.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    toupper.argtypes = [ctypes.c_int]

    result = ft_toupper(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = toupper(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result