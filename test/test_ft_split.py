import ctypes

# Load the shared library containing your ft_split function
lib = ctypes.cdll.LoadLibrary('./libft.so')

# Define the prototype of the ft_split function
ft_split = lib.ft_split
ft_split.argtypes = [ctypes.c_char_p, ctypes.c_char]
ft_split.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_char))

def test1_ft_split():
    # Test with a simple string
    s = 'hello world'
    expected = ['hello', 'world']
    
    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(s.encode('utf-8')), ctypes.c_char(b' '))
    
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

def test2_ft_split():
    # Test with a simple string
    s = '                  hello world'
    expected = ['hello', 'world']
    
    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(s.encode('utf-8')), ctypes.c_char(b' '))
    
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

def test3_ft_split():
    # Test with a simple string
    s = 'ciao come stai io na merda '
    expected = ['ciao', 'come', 'stai', 'io', 'na', 'merda']
    
    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(s.encode('utf-8')), ctypes.c_char(b' '))
    
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

def test4_ft_split():
    # Test with a simple string
    s = 'world'
    expected = ['world']
    
    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(s.encode('utf-8')), ctypes.c_char(b' '))
    
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

def test5_ft_split():
    # Test with a simple string
    s = 'iuvheiuvh e sdv j k j k h g g  f ty ue 8e 87e 9ew9w9e8we9wee  we world'
    expected = ['iuvheiuvh', 'e', 'sdv', 'j', 'k', 'j' , 'k', 'h', 'g', 'g', 'f', 'ty', 'ue' ,'8e' ,'87e' ,'9ew9w9e8we9wee' ,'we', 'world']
    
    # Call the ft_split function
    result = ft_split(ctypes.c_char_p(s.encode('utf-8')), ctypes.c_char(b' '))
    
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
    




