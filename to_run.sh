#!/usr/bin/bash

make re
gcc -shared -o libft.so *.o
make fclean

chmod 775 to_run.sh

python3 Moulinette.py

rm -f *.txt