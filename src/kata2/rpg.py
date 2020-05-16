#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen):
    list_values=string.printable
    passwrd=""
    for i in range(passLen):
        passwrd+=random.choice(string.printable)
    

    return passwrd

print(RandomPasswordGenerator(10))
