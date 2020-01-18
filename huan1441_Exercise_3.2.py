# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab01 Exercise 3.2
#
# Purpose: Script to use the function do_twice to call print_twice twice
#          and passing 'spam' as an argument
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 17, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# a function that takes two arguments, a function object(f) and a value(val), and calls f twice

def do_twice(f,val):
    f(val)
    f(val)

# a function that takes a string as a parameter and prints it twice

def print_twice(val):
    print(val)
    print(val)

do_twice(print_twice,"spam")
