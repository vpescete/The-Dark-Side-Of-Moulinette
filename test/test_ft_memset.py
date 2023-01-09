import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_memset():

    # input function
    test_dest = "ucococsdicja989 9888     \n\n\n\n\t\t\t\n\t\n "
    test_int = ord('\t')
    test_size = len(test_dest)

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_memset():

    # input function
    test_dest = "wouihdosijdaIUHSiuha9889a8YA9ha98"
    test_int = 66
    test_size = len(test_dest)

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_memset():

    # input function
    test_dest = "ciao"
    test_int = 99
    test_size = len(test_dest)

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_memset():

    # input function
    test_dest = "ciao  "
    test_int = 66
    test_size = len(test_dest)

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_memset():

    # input function
    test_dest = ""
    test_int = 0
    test_size = len(test_dest)

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_int, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_int, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result