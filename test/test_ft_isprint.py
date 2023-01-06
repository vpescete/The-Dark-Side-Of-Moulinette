import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_isprint():

    # input function
    test_string = 32

    # Definizione della funzione ft_isprint nella libreria
    ft_isprint = libft.ft_isprint

    # Specify the return type (int in this case)
    ft_isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isprint.argtypes = [ctypes.c_int]

    # Define the isprint function in the library
    isprint = libc.isprint

     # Specify the return type (int in this case)
    isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isprint.argtypes = [ctypes.c_int]

    result = ft_isprint(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isprint(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_isprint():

    # input function
    test_string = 127

    # Definizione della funzione ft_isprint nella libreria
    ft_isprint = libft.ft_isprint

    # Specify the return type (int in this case)
    ft_isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isprint.argtypes = [ctypes.c_int]

    # Define the isprint function in the library
    isprint = libc.isprint

     # Specify the return type (int in this case)
    isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isprint.argtypes = [ctypes.c_int]

    result = ft_isprint(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isprint(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_isprint():

    # input function
    test_string = 33

    # Definizione della funzione ft_isprint nella libreria
    ft_isprint = libft.ft_isprint

    # Specify the return type (int in this case)
    ft_isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isprint.argtypes = [ctypes.c_int]

    # Define the isprint function in the library
    isprint = libc.isprint

     # Specify the return type (int in this case)
    isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isprint.argtypes = [ctypes.c_int]

    result = ft_isprint(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isprint(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_isprint():

    # input function
    test_string = 10

    # Definizione della funzione ft_isprint nella libreria
    ft_isprint = libft.ft_isprint

    # Specify the return type (int in this case)
    ft_isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isprint.argtypes = [ctypes.c_int]

    # Define the isprint function in the library
    isprint = libc.isprint

     # Specify the return type (int in this case)
    isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isprint.argtypes = [ctypes.c_int]

    result = ft_isprint(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isprint(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_isprint():

    # input function
    test_string = 6

    # Definizione della funzione ft_isprint nella libreria
    ft_isprint = libft.ft_isprint

    # Specify the return type (int in this case)
    ft_isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isprint.argtypes = [ctypes.c_int]

    # Define the isprint function in the library
    isprint = libc.isprint

     # Specify the return type (int in this case)
    isprint.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isprint.argtypes = [ctypes.c_int]

    result = ft_isprint(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isprint(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result


