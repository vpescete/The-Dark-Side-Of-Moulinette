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

def test1_ft_strtrim():
    # input function
    test_string = "   Ciao   "
    test_toattach = "C "

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())

    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    print("======ERROR OUTPUT=======")
    print("ft_strtrim: ",result)
    print("strtrim: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    
def test2_ft_strtrim():
    # input function
    test_string = " ciao Vaffanculo ciao    "
    test_toattach = "ciao "

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())

    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    print("======ERROR OUTPUT=======")
    print("ft_strtrim: ",result)
    print("strtrim: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
        
def test3_ft_strtrim():
    # input function
    test_string = "vaffancul"
    test_toattach = "_ciao"

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())

    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    print("======ERROR OUTPUT=======")
    print("ft_strtrim: ",result)
    print("strtrim: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    
def test4_ft_strtrim():
    # input function
    test_string = ""
    test_toattach = "vjdnvkjdfnvkjnksdfjdskfjsdf"

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())

    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    print("======ERROR OUTPUT=======")
    print("ft_strtrim: ",result)
    print("strtrim: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
    
def test5_ft_strtrim():
    # input function
    test_string = ""
    test_toattach = ""

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())

    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    print("======ERROR OUTPUT=======")
    print("ft_strtrim: ",result)
    print("strtrim: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert  result == original_result

