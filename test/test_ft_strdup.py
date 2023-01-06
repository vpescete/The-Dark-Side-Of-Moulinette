import ctypes
import pytest

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

def test1_ft_strdup():
    # input function
    test_string = "CiaoCmondo    "

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_strdup nella libreria
    ft_strdup = libft.ft_strdup

    # Define the strdup function in the library
    strdup = libc.strdup

    result = ctypes.string_at(ft_strdup(test_string_buffer))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strdup(test_string_buffer))

    print("======OUTPUT=======")
    print("ft_strdup: ",result)
    print("strdup: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strdup():
    # input function
    test_string = "    "

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_strdup nella libreria
    ft_strdup = libft.ft_strdup

    # Define the strdup function in the library
    strdup = libc.strdup

    result = ctypes.string_at(ft_strdup(test_string_buffer))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strdup(test_string_buffer))

    print("======OUTPUT=======")
    print("ft_strdup: ",result)
    print("strdup: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strdup():
    # input function
    test_string = "kjcbdsicbksihcbdskcjbsib1nn\n\n\n\n\n\n\t\t\t\t\t\t\t\t %&$$££%$%$£&$   "

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())

    # Definizione della funzione ft_strdup nella libreria
    ft_strdup = libft.ft_strdup

    # Define the strdup function in the library
    strdup = libc.strdup

    result = ctypes.string_at(ft_strdup(test_string_buffer))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strdup(test_string_buffer))

    print("======OUTPUT=======")
    print("ft_strdup: ",result)
    print("strdup: ",original_result)
    
    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result