#!/usr/bin/env python3

import sys


ARGCOUNT = len(sys.argv) - 1

if ARGCOUNT != 1:
        print("Error: Incorrect number of arguments.") #Print this if the user runs this with the incorrect number of arguments
        exit(1)

ARG_1 = sys.argv[1]

if int(ARG_1) % 100 == 0:
        if int(ARG_1) % 400 == 0:
                print(str(ARG_1) + " is a leap year.")
        else:
                print(str(ARG_1) + " is not a leap year.")
        exit(0)
else:
        if int(ARG_1) % 4 == 0:
                print(str(ARG_1) + " is a leap year.")
        else:
                print(str(ARG_1) + " is not a leap year.")
