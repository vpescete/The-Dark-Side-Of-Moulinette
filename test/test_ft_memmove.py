import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_memmove():

    # input function
    test_dest = ""
    test_src = "ciao mondo"
    test_size = len(test_dest)

    # Definizione della funzione ft_memmove nella libreria
    ft_memmove = libft.ft_memmove

    # Define the memmove function in the library
    memmove = libc.memmove

    result = print(ft_memmove(test_dest, test_src, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memmove(test_dest, test_src, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_memmove():

    # input function
    test_dest = ""
    test_src = "os"
    test_size = len(test_dest)

    # Definizione della funzione ft_memmove nella libreria
    ft_memmove = libft.ft_memmove

    # Define the memmove function in the library
    memmove = libc.memmove

    result = print(ft_memmove(test_dest, test_src, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memmove(test_dest, test_src, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_memmove():

    # input function
    test_dest = "ciao"
    test_src = "ciao mondo"
    test_size = len(test_dest)

    # Definizione della funzione ft_memmove nella libreria
    ft_memmove = libft.ft_memmove

    # Define the memmove function in the library
    memmove = libc.memmove

    result = print(ft_memmove(test_dest, test_src, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memmove(test_dest, test_src, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_memmove():

    # input function
    test_dest = "                              "
    test_src = "ciao mondo"
    test_size = len(test_dest)

    # Definizione della funzione ft_memmove nella libreria
    ft_memmove = libft.ft_memmove

    # Define the memmove function in the library
    memmove = libc.memmove

    result = print(ft_memmove(test_dest, test_src, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memmove(test_dest, test_src, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_memmove():

    # input function
    test_dest = ""
    test_src = "                             ciao mondo"
    test_size = len(test_dest)

    # Definizione della funzione ft_memmove nella libreria
    ft_memmove = libft.ft_memmove

    # Define the memmove function in the library
    memmove = libc.memmove

    result = print(ft_memmove(test_dest, test_src, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memmove(test_dest, test_src, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result