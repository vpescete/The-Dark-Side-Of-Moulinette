import pytest
import subprocess


if __name__ == '__main__':
  print('FT_BZERO')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_bzero.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISALPHA')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_isalpha.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISDIGIT')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_isdigit.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISALNUM')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_isalnum.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISASCII')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_isascii.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ISPRINT')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_isprint.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCHR')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_memchr.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCMP')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_memcmp.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMCPY')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_memcpy.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMMOVE')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_memmove.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_MEMSET')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_memset.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_TOLOWER')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_tolower.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_TOUPPER')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_toupper.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ATOI')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_atoi.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRCHR')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strchr.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLEN')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strlen.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRRCHR')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strrchr.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLCPY')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strlcpy.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRLCAT')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strlcat.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_CALLOC')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_calloc.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRDUP')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strdup.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_SUBSTR')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_substr.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRJOIN')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strjoin.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRTRIM')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strtrim.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_ITOA')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_itoa.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRNCMP')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strncmp.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_STRNSTR')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_strnstr.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_SPLIT')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_split.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTCHAR_FD')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_putchar_fd.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTSTR_FD')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_putstr_fd.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTENDL_FD')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_putendl_fd.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")
  print('FT_PUTNBR_FD')
  ret = subprocess.call(['pytest', '-v', '--tb=short', '--no-header', './test/test_ft_putnbr_fd.py'])
  if ret != 0:
    print("Segfault occurred, moving on to the next test.\n")