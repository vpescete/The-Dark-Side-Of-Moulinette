import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_isdigit():

    # input function
    test_string = 99

    # Definizione della funzione ft_isdigit nella libreria
    ft_isdigit = libft.ft_isdigit

    # Specify the return type (int in this case)
    ft_isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit

     # Specify the return type (int in this case)
    isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isdigit.argtypes = [ctypes.c_int]

    result = ft_isdigit(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isdigit(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_isdigit():

    # input function
    test_string = 0

    # Definizione della funzione ft_isdigit nella libreria
    ft_isdigit = libft.ft_isdigit

    # Specify the return type (int in this case)
    ft_isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit

     # Specify the return type (int in this case)
    isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isdigit.argtypes = [ctypes.c_int]

    result = ft_isdigit(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isdigit(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_isdigit():

    # input function
    test_string = 48

    # Definizione della funzione ft_isdigit nella libreria
    ft_isdigit = libft.ft_isdigit

    # Specify the return type (int in this case)
    ft_isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit

     # Specify the return type (int in this case)
    isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isdigit.argtypes = [ctypes.c_int]

    result = ft_isdigit(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isdigit(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_isdigit():

    # input function
    test_string = 56

    # Definizione della funzione ft_isdigit nella libreria
    ft_isdigit = libft.ft_isdigit

    # Specify the return type (int in this case)
    ft_isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit

     # Specify the return type (int in this case)
    isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isdigit.argtypes = [ctypes.c_int]

    result = ft_isdigit(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isdigit(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_isdigit():

    # input function
    test_string = 127

    # Definizione della funzione ft_isdigit nella libreria
    ft_isdigit = libft.ft_isdigit

    # Specify the return type (int in this case)
    ft_isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit

     # Specify the return type (int in this case)
    isdigit.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isdigit.argtypes = [ctypes.c_int]

    result = ft_isdigit(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isdigit(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result