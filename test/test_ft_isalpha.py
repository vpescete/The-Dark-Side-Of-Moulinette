import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_isalpha():

    # input function
    test_string = 99

    # Definizione della funzione ft_isalpha nella libreria
    ft_isalpha = libft.ft_isalpha

    # Specify the return type (int in this case)
    ft_isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha

     # Specify the return type (int in this case)
    isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalpha.argtypes = [ctypes.c_int]

    result = ft_isalpha(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalpha(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_isalpha():

    # input function
    test_string = 12

    # Definizione della funzione ft_isalpha nella libreria
    ft_isalpha = libft.ft_isalpha

    # Specify the return type (int in this case)
    ft_isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha

     # Specify the return type (int in this case)
    isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalpha.argtypes = [ctypes.c_int]

    result = ft_isalpha(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalpha(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_isalpha():

    # input function
    test_string = 102

    # Definizione della funzione ft_isalpha nella libreria
    ft_isalpha = libft.ft_isalpha

    # Specify the return type (int in this case)
    ft_isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha

     # Specify the return type (int in this case)
    isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalpha.argtypes = [ctypes.c_int]

    result = ft_isalpha(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalpha(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_isalpha():

    # input function
    test_string = 70

    # Definizione della funzione ft_isalpha nella libreria
    ft_isalpha = libft.ft_isalpha

    # Specify the return type (int in this case)
    ft_isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha

     # Specify the return type (int in this case)
    isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalpha.argtypes = [ctypes.c_int]

    result = ft_isalpha(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalpha(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_isalpha():

    # input function
    test_string = 0

    # Definizione della funzione ft_isalpha nella libreria
    ft_isalpha = libft.ft_isalpha

    # Specify the return type (int in this case)
    ft_isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha

     # Specify the return type (int in this case)
    isalpha.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalpha.argtypes = [ctypes.c_int]

    result = ft_isalpha(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalpha(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result