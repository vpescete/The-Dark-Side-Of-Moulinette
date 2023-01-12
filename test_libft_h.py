import pytest
import re

file_path = 'libft.h'

def check_include_guard(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
    # Compile regular expression pattern to match include guards
    pattern = re.compile(r"^#ifndef\s+[A-Z_]+\s*$\s*^# define\s+[A-Z_]+\s*$.*^#endif", re.MULTILINE | re.DOTALL)
    match = pattern.search(file_contents)
    if match:
        return("Include guard present.")
    else:
        return("Include guard not found.")

def test_check_include_guard():
    file_p = file_path
    assert check_include_guard(file_p) == "Include guard present."
