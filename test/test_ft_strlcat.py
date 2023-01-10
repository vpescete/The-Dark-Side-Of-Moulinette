import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)

libbsd_path = '/lib/x86_64-linux-gnu/libbsd.so.0'
libbsd = ctypes.cdll.LoadLibrary(libbsd_path)

test_dests = [ctypes.create_string_buffer(b'1234567890\0' * 2), ctypes.create_string_buffer(b'123456tretertert57890\0' * 2), ctypes.create_string_buffer(b'123456tretertert57890\0' * 2), ctypes.create_string_buffer(b'\0' * 2)]
test_strings2 = [b"abcdef", b"abcdef6546346", b"abcdef6546346", b""]
test_sizes = [5, 17, 20, 40]

test_data = [(test_dests[0], test_strings2[0], test_sizes[0]), 
             (test_dests[1], test_strings2[1], test_sizes[1]), 
             (test_dests[2], test_strings2[2], test_sizes[2]), 
             (test_dests[3], test_strings2[3], test_sizes[3])]

ids = ["string: {}, size:{}".format(t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_dest, test_string2, test_size",test_data, ids=ids)

def test_ft_strlcat(test_dest, test_string2, test_size):

    # Definizione della funzione ft_strlcat nella libreria
    ft_strlcat = libft.ft_strlcat

    # Define the strlcat function in the library
    strlcat = libbsd.strlcat

    result = ft_strlcat(test_dest, test_string2, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcat(test_dest, test_string2, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
