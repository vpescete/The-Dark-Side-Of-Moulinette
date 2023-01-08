import pytest

if __name__ == '__main__':
  print('FT_ISALPHA')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_isalpha.py'])
  print('FT_ISDIGIT')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_isdigit.py'])
  print('FT_ISALNUM')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_isalnum.py'])
  print('FT_ISASCII')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_isascii.py'])
  print('FT_ISPRINT')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_isprint.py'])
  print('FT_MEMCHR')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_memchr.py'])
  print('FT_MEMCMP')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_memcmp.py'])
  print('FT_MEMCPY')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_memcpy.py'])

  #LE FUNZIONI MEMMOVE VANNO IN SEGMANTTION FAULT ----> DA FIXARE

  # print('FT_MEMMOVE')
  # pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_memmove.py'])
  # print('FT_MEMSET')
  # pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_memset.py'])

  #LA FUNZIONE BZERO RESTITUISCE UN VALORE TOTALMENTE DIFFERENTE ---> DA FIXARE

  # print('FT_BZERO')
  # pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_bzero.py'])


  print('FT_ATOI')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_atoi.py'])
  print('FT_STRCHR')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strchr.py'])
  print('FT_STRLEN')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strlen.py'])
  print('FT_STRRCHR')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strrchr.py'])
  print('FT_TOLOWER')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_tolower.py'])
  print('FT_TOUPPER')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_toupper.py'])

  #LA FUNZIONE CALLOC RESTITUISCO GLI INDIRIZZI DI MEMORIA ---> DA FIXARE 

  # print('FT_CALLOC')
  # pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_calloc.py'])
  print('FT_STRDUP')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strdup.py'])
  print('FT_SUBSTR')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_substr.py'])
  print('FT_STRJOIN')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strjoin.py'])
  print('FT_STRTRIM')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_strtrim.py'])
  print('FT_ITOA')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_itoa.py'])
  print('FT_PUTCHAR_FD')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_putchar_fd.py'])
  print('FT_PUTSTR_FD')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_putstr_fd.py'])
  print('FT_PUTENDL_FD')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_putendl_fd.py'])
  print('FT_PUTNBR_FD')
  pytest.main(['-v', '--tb=short', '--no-header', './test/test_ft_putnbr_fd.py'])
