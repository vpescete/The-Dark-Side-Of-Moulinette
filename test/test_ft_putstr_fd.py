import ctypes
import pytest
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
libft = ctypes.cdll.LoadLibrary(library_path)
        
ft_putstr_fd = libft.ft_putstr_fd

test_strings = ["02987549238573405934753408573409573409573405973405983", "983iubfd0q987f4u3bf03f87b2306t234ubf032hg730cv2304f23460fg\t\n\t", "C", "      C/niao come/n stai/n", ""]

ids = ["string: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_putstr_fd(test_string):
    with open('test1001.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = test_string

        # Usa ft_putstr_fd per scrivere un carattere nel file
        result = ft_putstr_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test1001.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == s.encode('utf-8')