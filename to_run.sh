#!/usr/bin/bash

make re
gcc -shared -o libft.so *.o
make fclean

chmod 775 to_run.sh

pytest -v --tb=short --no-header test_libft_h.py

python3 Moulinette.py 2>/dev/null

rm -f *.txt