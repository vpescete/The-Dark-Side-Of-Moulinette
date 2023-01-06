import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_atoi():

    # input function
    test_string = "    +18329jchdbckjdhb"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_atoi():

    # input function
    test_string = "    -18329jchdbckjdhb"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_atoi():

    # input function
    test_string = "    +-18329jchdbckjdhb"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_atoi():

    # input function
    test_string = "    +18329234987298472904802498"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_atoi():

    # input function
    test_string = "    -183984359385794329jchdbckjdhb"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test6_ft_atoi():

    # input function
    test_string = "  6  -183984359385794329jchdbckjdhb"

    # Definizione della funzione ft_atoi nella libreria
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    result = ft_atoi(test_string)
    
    # chiamare la funzione originale con i dati di input
    original_result = atoi(test_string)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result