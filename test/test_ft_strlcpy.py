import ctypes
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)

# Load the library that implements strlcpy
libbsd_path = '/lib/x86_64-linux-gnu/libbsd.so.0'
libbsd = ctypes.cdll.LoadLibrary(libbsd_path)

def test1_ft_strlcpy():

    # input function
    test_dst = ctypes.create_string_buffer(b'\0' * 20)
    test_src = b"1234567890"
    test_size = 20

    # Definizione della funzione ft_strlcpy nella libreria
    ft_strlcpy = libft.ft_strlcpy

    # Define the strlcpy function in the library
    strlcpy = libbsd.strlcpy

    result = ft_strlcpy(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcpy(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strlcpy():

    # input function
    test_dst = ctypes.create_string_buffer(b'\0' * 20)
    test_src = b"ciaocomeva"
    test_size = 5

    # Definizione della funzione ft_strlcpy nella libreria
    ft_strlcpy = libft.ft_strlcpy

    # Define the strlcpy function in the library
    strlcpy = libbsd.strlcpy

    result = ft_strlcpy(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcpy(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strlcpy():

    # input function
    test_dst = ctypes.create_string_buffer(b'\0' * 20)
    test_src = b""
    test_size = 15

    # Definizione della funzione ft_strlcpy nella libreria
    ft_strlcpy = libft.ft_strlcpy

    # Define the strlcpy function in the library
    strlcpy = libbsd.strlcpy

    result = ft_strlcpy(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcpy(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_strlcpy():

    # input function
    test_dst = ctypes.create_string_buffer(b'\0' * 20)
    test_src = b"         \n"
    test_size = 1

    # Definizione della funzione ft_strlcpy nella libreria
    ft_strlcpy = libft.ft_strlcpy

    # Define the strlcpy function in the library
    strlcpy = libbsd.strlcpy

    result = ft_strlcpy(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcpy(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
