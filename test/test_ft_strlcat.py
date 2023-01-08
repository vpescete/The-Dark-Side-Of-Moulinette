import ctypes
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
libft = ctypes.cdll.LoadLibrary(library_path)

libbsd_path = '/lib/x86_64-linux-gnu/libbsd.so.0'
libbsd = ctypes.cdll.LoadLibrary(libbsd_path)

def test1_ft_strlcat():

    # input function
    test_dst = ctypes.create_string_buffer(b'1234567890\0' * 2)
    test_src = b"abcdef"
    test_size = 5

    # Definizione della funzione ft_strlcat
    ft_strlcat = libft.ft_strlcat

    # Define the strlcat function in the library
    strlcat = libbsd.strlcat

    result = ft_strlcat(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcat(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_strlcat():

    # input function
    test_dst = ctypes.create_string_buffer(b'123456tretertert57890\0' * 2)
    test_src = b"abcdef6546346"
    test_size = 17

    # Definizione della funzione ft_strlcat
    ft_strlcat = libft.ft_strlcat

    # Define the strlcat function in the library
    strlcat = libbsd.strlcat

    result = ft_strlcat(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcat(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_strlcat():

    # input function
    test_dst = ctypes.create_string_buffer(b'123456tretertert57890\0' * 2)
    test_src = b"abcdef6546346"
    test_size = 20

    # Definizione della funzione ft_strlcat
    ft_strlcat = libft.ft_strlcat

    # Define the strlcat function in the library
    strlcat = libbsd.strlcat

    result = ft_strlcat(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcat(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_strlcat():

    # input function
    test_dst = ctypes.create_string_buffer(b'\0' * 2)
    test_src = b""
    test_size = 40

    # Definizione della funzione ft_strlcat
    ft_strlcat = libft.ft_strlcat

    # Define the strlcat function in the library
    strlcat = libbsd.strlcat

    result = ft_strlcat(test_dst, test_src, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcat(test_dst, test_src, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result