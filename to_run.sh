#!/usr/bin/bash

make re
gcc -shared -o libft.so *.o
make fclean

python3 Moulinette.py
