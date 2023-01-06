import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_strchr():

    # input function
    test_src = "ciao mondo"
    test_char = 99

    # Definizione della funzione ft_strchr nella libreria
    ft_strchr = libft.ft_strchr

    # Define the strchr function in the library
    strchr = libc.strchr

    result = print(ft_strchr( test_src, test_char))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strchr( test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strchr():

    # input function
    test_src = "ciao mondo"
    test_char = 48

    # Definizione della funzione ft_strchr nella libreria
    ft_strchr = libft.ft_strchr

    # Define the strchr function in the library
    strchr = libc.strchr

    result = print(ft_strchr( test_src, test_char))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strchr( test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strchr():

    # input function
    test_src = "ciao mondo"
    test_char = 32

    # Definizione della funzione ft_strchr nella libreria
    ft_strchr = libft.ft_strchr

    # Define the strchr function in the library
    strchr = libc.strchr

    result = print(ft_strchr( test_src, test_char))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strchr( test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result


def test4_ft_strchr():

    # input function
    test_src = "ciao      mondo"
    test_char = 12

    # Definizione della funzione ft_strchr nella libreria
    ft_strchr = libft.ft_strchr

    # Define the strchr function in the library
    strchr = libc.strchr

    result = print(ft_strchr( test_src, test_char))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strchr( test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result


def test5_ft_strchr():

    # input function
    test_src = "ciao mondo"
    test_char = '\n'

    # Definizione della funzione ft_strchr nella libreria
    ft_strchr = libft.ft_strchr

    # Define the strchr function in the library
    strchr = libc.strchr

    result = print(ft_strchr( test_src, test_char))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(strchr( test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result


