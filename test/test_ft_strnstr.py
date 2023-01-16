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

test_strings1 = ["ciaotring2mondo", "ciaotring2mondo", "", "ciaotring2   mondo"]
test_strings2 = ["0", "ng2", "ciao mondo", "mondo"]
test_sizes = [len(test_strings1[0]), len(test_strings1[1]), len(test_strings1[2]), len(test_strings1[3])]

test_data = [(test_strings1[0], test_strings2[0], test_sizes[0]),
             (test_strings1[1], test_strings2[1], test_sizes[1]),
             (test_strings1[2], test_strings2[2], test_sizes[2]),
             (test_strings1[3], test_strings2[3], test_sizes[3])]

ids = ["string: {}, to_find: {}, size:{}".format(t[0], t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_string1, test_string2, test_size",test_data, ids=ids)

def test_ft_strnstr(test_string1, test_string2, test_size):

    # Define the ft_strnstr function in the library
    ft_strnstr = libft.ft_strnstr

    # Define the strnstr function in the library
    strnstr = libbsd.strnstr
    
    # Create buffer of the input strings
    test_buffer_string1 = ctypes.create_string_buffer(test_string1.encode())
    test_buffer_string2 = ctypes.create_string_buffer(test_string2.encode())
    
    # Save the pointer to the string from the functions (custom and real) in a variable
    str_ft = ft_strnstr(test_buffer_string1, test_buffer_string2, test_size)
    str_original = strnstr(test_buffer_string1, test_buffer_string2, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert hex(str_ft) == hex(str_original)