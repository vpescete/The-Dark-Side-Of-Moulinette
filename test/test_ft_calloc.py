import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_calloc():

    # input function
    num_elements = 2
    element_size = 6

    # Definizione della funzione ft_calloc nella libreria

    ft_calloc = libft.ft_calloc
    ft_calloc.restype = ctypes.c_void_p

    # Define the calloc function in the library
    calloc = libc.calloc
    calloc.restype = ctypes.c_void_p

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert ctypes.string_at(ft_calloc(num_elements, element_size), num_elements * element_size) == ctypes.string_at(calloc(num_elements, element_size), num_elements * element_size)

def test2_ft_calloc():

    # input function
    num_elements = 21
    element_size = 63

    # Definizione della funzione ft_calloc nella libreria

    ft_calloc = libft.ft_calloc
    ft_calloc.restype = ctypes.c_void_p

    # Define the calloc function in the library
    calloc = libc.calloc
    calloc.restype = ctypes.c_void_p

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert ctypes.string_at(ft_calloc(num_elements, element_size), num_elements * element_size) == ctypes.string_at(calloc(num_elements, element_size), num_elements * element_size)

def test3_ft_calloc():

    # input function
    num_elements = 20
    element_size = 0

    # Definizione della funzione ft_calloc nella libreria

    ft_calloc = libft.ft_calloc
    ft_calloc.restype = ctypes.c_void_p

    # Define the calloc function in the library
    calloc = libc.calloc
    calloc.restype = ctypes.c_void_p

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert ctypes.string_at(ft_calloc(num_elements, element_size), num_elements * element_size) == ctypes.string_at(calloc(num_elements, element_size), num_elements * element_size)

def test4_ft_calloc():

    # input function
    num_elements = 0
    element_size = 0

    # Definizione della funzione ft_calloc nella libreria

    ft_calloc = libft.ft_calloc
    ft_calloc.restype = ctypes.c_void_p

    # Define the calloc function in the library
    calloc = libc.calloc
    calloc.restype = ctypes.c_void_p

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert ctypes.string_at(ft_calloc(num_elements, element_size), num_elements * element_size) == ctypes.string_at(calloc(num_elements, element_size), num_elements * element_size)