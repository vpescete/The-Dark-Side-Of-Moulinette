import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_isalnum():

    # input function
    test_string = 99

    # Definizione della funzione ft_isalnum nella libreria
    ft_isalnum = libft.ft_isalnum

    # Specify the return type (int in this case)
    ft_isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum

     # Specify the return type (int in this case)
    isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalnum.argtypes = [ctypes.c_int]

    result = ft_isalnum(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalnum(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_isalnum():

    # input function
    test_string = 1

    # Definizione della funzione ft_isalnum nella libreria
    ft_isalnum = libft.ft_isalnum

    # Specify the return type (int in this case)
    ft_isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum

     # Specify the return type (int in this case)
    isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalnum.argtypes = [ctypes.c_int]

    result = ft_isalnum(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalnum(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_isalnum():

    # input function
    test_string = 999

    # Definizione della funzione ft_isalnum nella libreria
    ft_isalnum = libft.ft_isalnum

    # Specify the return type (int in this case)
    ft_isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum

     # Specify the return type (int in this case)
    isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalnum.argtypes = [ctypes.c_int]

    result = ft_isalnum(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalnum(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_isalnum():

    # input function
    test_string = 127

    # Definizione della funzione ft_isalnum nella libreria
    ft_isalnum = libft.ft_isalnum

    # Specify the return type (int in this case)
    ft_isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum

     # Specify the return type (int in this case)
    isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalnum.argtypes = [ctypes.c_int]

    result = ft_isalnum(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalnum(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test1_ft_isalnum():

    # input function
    test_string = 50

    # Definizione della funzione ft_isalnum nella libreria
    ft_isalnum = libft.ft_isalnum

    # Specify the return type (int in this case)
    ft_isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum

     # Specify the return type (int in this case)
    isalnum.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    isalnum.argtypes = [ctypes.c_int]

    result = ft_isalnum(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = isalnum(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result