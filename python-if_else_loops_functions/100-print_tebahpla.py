#!/usr/bin/python3
i = 0
""""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(ord('z'), ord('a') - 1, - 1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
