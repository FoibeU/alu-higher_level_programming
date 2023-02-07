#!/usr/bin/python3
def islower(c):
    """Function checks for lowercase characters."""
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        else:
            return False

islower = __import__('7-islower').islower
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))


