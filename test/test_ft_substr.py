import ctypes
import pytest

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
library2_path = os.path.join(cwd, 'libft_tester.so')


libft = ctypes.cdll.LoadLibrary(library_path)
libft_tester = ctypes.cdll.LoadLibrary(library2_path)

def test1_ft_substr():
    # input function
    test_string = "CiaoCmondo    "
    test_start = 3

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_substr nella libreria
    ft_substr = libft.ft_substr

    # Define the substr function in the library
    substr = libft_tester.substr

    result = ctypes.string_at(ft_substr(test_string_buffer, test_start, len(test_string)))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(substr(test_string_buffer, test_start, len(test_string)))

    print("======ERROR OUTPUT=======")
    print("ft_substr: ",result)
    print("substr: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    
def test2_ft_substr():
    # input function
    test_string = ""
    test_start = 3

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_substr nella libreria
    ft_substr = libft.ft_substr

    # Define the substr function in the library
    substr = libft_tester.substr

    result = ctypes.string_at(ft_substr(test_string_buffer, test_start, len(test_string)))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(substr(test_string_buffer, test_start, len(test_string)))

    print("======OUTPUT=======")
    print("ft_substr: ",result)
    print("substr: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    
def test3_ft_substr():
    # input function
    test_string = "kjcdbicjbds"
    test_start = 0

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_substr nella libreria
    ft_substr = libft.ft_substr

    # Define the substr function in the library
    substr = libft_tester.substr

    result = ctypes.string_at(ft_substr(test_string_buffer, test_start, len(test_string)))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(substr(test_string_buffer, test_start, len(test_string)))

    print("======OUTPUT=======")
    print("ft_substr: ",result)
    print("substr: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_substr():
    # input function
    test_string = "kjcdbicjbds"
    test_start = 25

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_substr nella libreria
    ft_substr = libft.ft_substr

    # Define the substr function in the library
    substr = libft_tester.substr

    result = ctypes.string_at(ft_substr(test_string_buffer, test_start, len(test_string)))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(substr(test_string_buffer, test_start, len(test_string)))

    print("======OUTPUT=======")
    print("ft_substr: ",result)
    print("substr: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result