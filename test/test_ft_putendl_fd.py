import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')


libft = ctypes.cdll.LoadLibrary(library_path)
        
ft_putendl_fd = libft.ft_putendl_fd

def test1_ft_putendl_fd():
# Apri un file di test in scrittura
    with open('test2001.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = "02987549238573405934753408573409573409573405973405983"

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test2001.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')


def test2_ft_putendl_fd():
# Apri un file di test in scrittura
    with open('test2002.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = "983iubfd0q987f4u3bf03f87b2306t234ubf032hg730cv2304f23460fg\t\n\t"

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test2002.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')
            

def test3_ft_putendl_fd():
# Apri un file di test in scrittura
    with open('test2003.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = "C"

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test2003.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')
            

def test4_ft_putendl_fd():
# Apri un file di test in scrittura
    with open('test2004.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = "      C/niao come/n stai/n"

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test2004.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')
            

def test5_ft_putendl_fd():
# Apri un file di test in scrittura
    with open('test2005.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = ""

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open('test2005.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')
            