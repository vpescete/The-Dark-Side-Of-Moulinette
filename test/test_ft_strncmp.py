import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_strncmp():

    # input function
    test_s1 = "ciao mondo"
    test_s2 = "0"

    # Definizione della funzione ft_strncmp nella libreria
    ft_strncmp = libft.ft_strncmp

    # Define the strncmp function in the library
    strncmp = libc.strncmp

    result = print(ft_strncmp( test_s1, test_s2))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strncmp( test_s1, test_s2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strncmp():

    # input function
    test_s1 = "ciao mondo"
    test_s2 = "vaffanculo"

    # Definizione della funzione ft_strncmp nella libreria
    ft_strncmp = libft.ft_strncmp

    # Define the strncmp function in the library
    strncmp = libc.strncmp

    result = print(ft_strncmp( test_s1, test_s2))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strncmp( test_s1, test_s2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strncmp():

    # input function
    test_s1 = ""
    test_s2 = "vaffanculo"

    # Definizione della funzione ft_strncmp nella libreria
    ft_strncmp = libft.ft_strncmp

    # Define the strncmp function in the library
    strncmp = libc.strncmp

    result = print(ft_strncmp( test_s1, test_s2))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strncmp( test_s1, test_s2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_strncmp():

    # input function
    test_s1 = "ciao mondo"
    test_s2 = "ciao mondo"

    # Definizione della funzione ft_strncmp nella libreria
    ft_strncmp = libft.ft_strncmp

    # Define the strncmp function in the library
    strncmp = libc.strncmp

    result = print(ft_strncmp( test_s1, test_s2))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strncmp( test_s1, test_s2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result