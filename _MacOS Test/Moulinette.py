import pytest
import subprocess


if __name__ == '__main__':
  print('FT_BZERO')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_bzero.py'])
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_bzero.py'])
  # # if ret != 0:
  # #   print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISALPHA')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_isalpha.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISDIGIT')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_isdigit.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISALNUM')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_isalnum.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISASCII')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_isascii.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISPRINT')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_isprint.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCHR')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_memchr.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCMP')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_memcmp.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCPY')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_memcpy.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMMOVE')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_memmove.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMSET')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_memset.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_TOLOWER')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_tolower.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_TOUPPER')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_toupper.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_ATOI')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_atoi.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRCHR')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strchr.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLEN')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strlen.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRRCHR')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strrchr.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLCPY')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strlcpy.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLCAT')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strlcat.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_CALLOC')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_calloc.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  # print('FT_STRDUP')
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strdup.py'])
  # # if ret != 0:
  #   # print("Segfault occurred, moving on to the next test.\n")
  # print('FT_SUBSTR')
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_substr.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  # print('FT_STRJOIN')
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strjoin.py'])
  # # if ret != 0:
  #   # print("Segfault occurred, moving on to the next test.\n")
  # print('FT_STRTRIM')
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strtrim.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  # print('FT_ITOA')
  # pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_itoa.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRNCMP')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strncmp.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRNSTR')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_strnstr.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_SPLIT')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_split.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTCHAR_FD')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_putchar_fd.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTSTR_FD')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_putstr_fd.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTENDL_FD')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_putendl_fd.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTNBR_FD')
  pytest.main([ '-v', '--tb=short', '--no-header', './test/test_ft_putnbr_fd.py'])
  # if ret != 0:
    # print("Segfault occurred, moving on to the next test.\n")