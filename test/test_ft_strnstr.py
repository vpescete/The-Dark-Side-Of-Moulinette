import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)

libbsd_path = '/lib/x86_64-linux-gnu/libbsd.so.0'
libbsd = ctypes.cdll.LoadLibrary(libbsd_path)

def test1_ft_strnstr():

    # input function
    test_s1 = "ciao mondo"
    test_s2 = "0"
    test_size = 10

    # Definizione della funzione ft_strnstr nella libreria
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr

    result = print(ft_strnstr(test_s1, test_s2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strnstr(test_s1, test_s2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strnstr():

    # input function
    test_s1 = "ciao mondo"
    test_s2 = "ciao mondo"
    test_size = 100

    # Definizione della funzione ft_strnstr nella libreria
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr

    result = print(ft_strnstr(test_s1, test_s2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strnstr(test_s1, test_s2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strnstr():

    # input function
    test_s1 = ""
    test_s2 = "ciao mondo"
    test_size = 0

    # Definizione della funzione ft_strnstr nella libreria
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr

    result = print(ft_strnstr(test_s1, test_s2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strnstr(test_s1, test_s2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_strnstr():

    # input function
    test_s1 = "ciao    mondo"
    test_s2 = "ciao mondo"
    test_size = 3

    # Definizione della funzione ft_strnstr nella libreria
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr

    result = print(ft_strnstr(test_s1, test_s2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strnstr(test_s1, test_s2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result