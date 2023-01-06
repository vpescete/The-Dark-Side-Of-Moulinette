import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_isascii():

    # input function
    test_string = 99

    # Definizione della funzione ft_isascii nella libreria
    ft_isascii = libft.ft_isascii

    # Specify the return type (int in this case)
    ft_isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii

     # Specify the return type (int in this case)
    isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isascii.argtypes = [ctypes.c_int]

    result = ft_isascii(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isascii(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_isascii():

    # input function
    test_string = 127

    # Definizione della funzione ft_isascii nella libreria
    ft_isascii = libft.ft_isascii

    # Specify the return type (int in this case)
    ft_isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii

     # Specify the return type (int in this case)
    isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isascii.argtypes = [ctypes.c_int]

    result = ft_isascii(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isascii(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_isascii():

    # input function
    test_string = 23483

    # Definizione della funzione ft_isascii nella libreria
    ft_isascii = libft.ft_isascii

    # Specify the return type (int in this case)
    ft_isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii

     # Specify the return type (int in this case)
    isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isascii.argtypes = [ctypes.c_int]

    result = ft_isascii(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isascii(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result


def test4_ft_isascii():

    # input function
    test_string = 256

    # Definizione della funzione ft_isascii nella libreria
    ft_isascii = libft.ft_isascii

    # Specify the return type (int in this case)
    ft_isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii

     # Specify the return type (int in this case)
    isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isascii.argtypes = [ctypes.c_int]

    result = ft_isascii(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isascii(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_isascii():

    # input function
    test_string = 48

    # Definizione della funzione ft_isascii nella libreria
    ft_isascii = libft.ft_isascii

    # Specify the return type (int in this case)
    ft_isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii

     # Specify the return type (int in this case)
    isascii.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isascii.argtypes = [ctypes.c_int]

    result = ft_isascii(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isascii(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result