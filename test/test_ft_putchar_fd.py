import ctypes

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')


libft = ctypes.cdll.LoadLibrary(library_path)
        
ft_putchar_fd = libft.ft_putchar_fd

def test1_ft_putchar_fd():
# Apri un file di test in scrittura
    with open('test1.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = 66

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test1.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == 'B'

def test2_ft_putchar_fd():
# Apri un file di test in scrittura
    with open('test2.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = 62

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test2.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == '>'

def test3_ft_putchar_fd():
# Apri un file di test in scrittura
    with open('test3.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = 48

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test3.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == '0'

def test4_ft_putchar_fd():
# Apri un file di test in scrittura
    with open('test4.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = 32

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test4.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == ' '

def test5_ft_putchar_fd():
# Apri un file di test in scrittura
    with open('test5.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        c = 127

        # Usa ft_putchar_fd per scrivere un carattere nel file
        result = ft_putchar_fd(c, f.fileno())

    # Apri il file di test in lettura
    with open('test5.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert chr(f.read()[0]) == chr(127)