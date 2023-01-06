# int toupper(int c);

import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_tolower():

    # input function
    test_string = 90

    # Definizione della funzione ft_tolower nella libreria
    ft_tolower = libft.ft_tolower

    # Specify the return type (int in this case)
    ft_tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower

     # Specify the return type (int in this case)
    tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    tolower.argtypes = [ctypes.c_int]

    result = ft_tolower(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = tolower(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_tolower():

    # input function
    test_string = 68

    # Definizione della funzione ft_tolower nella libreria
    ft_tolower = libft.ft_tolower

    # Specify the return type (int in this case)
    ft_tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower

     # Specify the return type (int in this case)
    tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    tolower.argtypes = [ctypes.c_int]

    result = ft_tolower(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = tolower(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_tolower():

    # input function
    test_string = 48

    # Definizione della funzione ft_tolower nella libreria
    ft_tolower = libft.ft_tolower

    # Specify the return type (int in this case)
    ft_tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower

     # Specify the return type (int in this case)
    tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    tolower.argtypes = [ctypes.c_int]

    result = ft_tolower(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = tolower(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_tolower():

    # input function
    test_string = 32

    # Definizione della funzione ft_tolower nella libreria
    ft_tolower = libft.ft_tolower

    # Specify the return type (int in this case)
    ft_tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower

     # Specify the return type (int in this case)
    tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    tolower.argtypes = [ctypes.c_int]

    result = ft_tolower(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = tolower(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_tolower():

    # input function
    test_string = 102

    # Definizione della funzione ft_tolower nella libreria
    ft_tolower = libft.ft_tolower

    # Specify the return type (int in this case)
    ft_tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower

     # Specify the return type (int in this case)
    tolower.restype = ctypes.c_int

    # Specify the argument types (int in this case)
    tolower.argtypes = [ctypes.c_int]

    result = ft_tolower(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = tolower(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

