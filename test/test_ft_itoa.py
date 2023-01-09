import ctypes
import pytest

import os

# Get the current working directory
cwd = os.getcwd()

# Construct the full path to the library file
library_path = os.path.join(cwd, 'libft.so')
library2_path = os.path.join(cwd, 'libft_tester.so')


libft = ctypes.cdll.LoadLibrary(library_path)
libft_tester = ctypes.cdll.LoadLibrary(library2_path)

def test1_ft_itoa():
    # input function
    test_int = 4359

    # Definizione della funzione ft_itoa nella libreria
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))


    print("======ERROR OUTPUT=======")
    print("ft_itoa: ",result)
    print("itoa: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test2_ft_itoa():
    # input function
    test_int = 43595

    # Definizione della funzione ft_itoa nella libreria
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))


    print("======ERROR OUTPUT=======")
    print("ft_itoa: ",result)
    print("itoa: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test3_ft_itoa():
    # input function
    test_int = -4385309

    # Definizione della funzione ft_itoa nella libreria
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))


    print("======ERROR OUTPUT=======")
    print("ft_itoa: ",result)
    print("itoa: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test4_ft_itoa():
    # input function
    test_int = -34658342

    # Definizione della funzione ft_itoa nella libreria
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))


    print("======ERROR OUTPUT=======")
    print("ft_itoa: ",result)
    print("itoa: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result

def test5_ft_itoa():
    # input function
    test_int = 0

    # Definizione della funzione ft_itoa nella libreria
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))


    print("======ERROR OUTPUT=======")
    print("ft_itoa: ",result)
    print("itoa: ",original_result)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
