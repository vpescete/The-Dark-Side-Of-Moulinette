import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
libft = ctypes.cdll.LoadLibrary(library_path)
        
ft_putchar_fd = libft.ft_putchar_fd

test_chars = [66, 62, 48, 32, 127]
expecteds = ['B', '>', '0', ' ', chr(127)]

test_data = [[test_chars[0], expecteds[0]],
             [test_chars[1], expecteds[1]],
             [test_chars[2], expecteds[2]],
             [test_chars[3], expecteds[3]],
             [test_chars[4], expecteds[4]]]

ids = ["char: {}".format(t[0]) for t in test_data]
@pytest.mark.parametrize("test_char, expected",test_data, ids=ids)

def test_ft_putchar_fd(test_char, expected):
    with open('test.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = test_char

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == expected
