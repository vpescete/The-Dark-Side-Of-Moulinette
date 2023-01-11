import ctypes

# Load the shared library containing your ft_split function
lib = ctypes.cdll.LoadLibrary('./libft.so')

# Define the prototype of the ft_split function
ft_split = lib.ft_split
ft_split.argtypes = [ctypes.c_char_p, ctypes.c_char]
ft_split.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_char))

import ctypes
import pytest

# Load the shared library containing your ft_split function
lib = ctypes.cdll.LoadLibrary('./libft.so')

# Define the prototype of the ft_split function
ft_split = lib.ft_split
ft_split.argtypes = [ctypes.c_char_p, ctypes.c_char]
ft_split.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_char))

test_strings1 = ['hello world', '                  hello world', 'ciao come stai io na merda ', 'world', 'iuvheiuvh e sdv j k j k h g g  f ty ue 8e 87e 9ew9w9e8we9wee  we world']
test_expectations = [['hello', 'world'], ['hello', 'world'],['ciao', 'come', 'stai', 'io', 'na', 'merda'], ['world'], ['iuvheiuvh', 'e', 'sdv', 'j', 'k', 'j' , 'k', 'h', 'g', 'g', 'f', 'ty', 'ue' ,'8e' ,'87e' ,'9ew9w9e8we9wee' ,'we', 'world']]

test_data = [(test_strings1[0], test_expectations[0]), 
             (test_strings1[1], test_expectations[1]), 
             (test_strings1[2], test_expectations[2]), 
             (test_strings1[3], test_expectations[3]), 
             (test_strings1[4], test_expectations[4])]

ids = ["input string: '{}'".format(t[0]) for t in test_data]
@pytest.mark.parametrize("test_string, expected",test_data, ids=ids)

def test_ft_strncmp(test_string, expected):

    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(test_string.encode('utf-8')), ctypes.c_char(b' '))
    
    # Initialize an empty result list
    result_list = []
    
    # Iterate through the array of pointers to characters
    i = 0
    while i < len(expected):
        # Convert the pointer to a Python string and append it to the result list
        result_list.append(ctypes.string_at(result[i]).decode())
        i += 1
    # Compare the result list to the expected output
    assert result_list == expected
