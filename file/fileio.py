#!/bin/python2
import os

def read_print_file():
    f = open("../input/input.txt","r")
    content = f.readlines()
    for line in content:
        print line

    f.close()

read_print_file()
