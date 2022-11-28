import sys

vlsm = input("What do you want the program to calculate?(vlsm=v, subneting=s) ")
if vlsm.lower() == 's':
    from subneting import *
elif vlsm.lower() == 'v':
    from vlsm import *
else:
    print("Error: the given text cannot be interpreted!")
