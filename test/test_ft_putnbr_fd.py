import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')


libft = ctypes.cdll.LoadLibrary(library_path)
        
ft_putnbr_fd = libft.ft_putnbr_fd

def test1_ft_putnbr_fd():
# Apri un file di test in scrittura
    with open('test3001.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb = 123456789

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3001.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')

def test2_ft_putnbr_fd():
# Apri un file di test in scrittura
    with open('test3002.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb = -127849

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3002.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')

def test3_ft_putnbr_fd():
# Apri un file di test in scrittura
    with open('test3003.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb =  0

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3003.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')

def test4_ft_putnbr_fd():
# Apri un file di test in scrittura
    with open('test3004.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb =  -2147483648

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3004.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')

def test5_ft_putnbr_fd():
# Apri un file di test in scrittura
    with open('test3005.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb =  -21474836

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3005.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')