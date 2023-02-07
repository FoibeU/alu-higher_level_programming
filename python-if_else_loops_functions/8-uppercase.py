#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        """Change to uppercase character."""
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
            print("{}".format(ch), end="")
            print()
                                                            
