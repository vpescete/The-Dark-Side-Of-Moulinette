import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')

libft = ctypes.cdll.LoadLibrary(library_path)
libc = ctypes.cdll.LoadLibrary('libc.so.6')

@pytest.mark.parametrize("num_elements, element_size, expected_output", [
    (5, 4, [0, 0, 0, 0, 0]),
    (3, 2, [0, 0, 0]),
    (2, 3, [0, 0])
])

def test1_ft_calloc():

    # input function
    # num_elements = 2
    # element_size = 6

    # Definizione della funzione ft_calloc nella libreria
    ft_calloc = libft.ft_calloc

    # Define the calloc function in the library
    calloc = libc.calloc

    result = ft_calloc(num_elements, element_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = calloc(num_elements, element_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result