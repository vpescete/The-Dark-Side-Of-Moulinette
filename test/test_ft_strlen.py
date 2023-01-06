import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_strlen():

    # input function
    test_src = "ciao mondo"

    # Definizione della funzione ft_strlen nella libreria
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    result = ft_strlen( test_src)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlen( test_src)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strlen():

    # input function
    test_src = ""

    # Definizione della funzione ft_strlen nella libreria
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    result = ft_strlen( test_src)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlen( test_src)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strlen():

    # input function
    test_src = "ciao mondo               "

    # Definizione della funzione ft_strlen nella libreria
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    result = ft_strlen( test_src)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlen( test_src)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_strlen():

    # input function
    test_src = "ciao    \n mondo"

    # Definizione della funzione ft_strlen nella libreria
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    result = ft_strlen( test_src)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlen( test_src)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_strlen():

    # input function
    test_src = "c"

    # Definizione della funzione ft_strlen nella libreria
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    result = ft_strlen( test_src)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlen( test_src)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

