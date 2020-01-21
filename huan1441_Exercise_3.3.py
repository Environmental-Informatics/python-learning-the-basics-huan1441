# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab01 Exercise 3.3
#
# Purpose: Script to generating a 4x4 grid from Exercise 3.3
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 17, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# a function that calls the argument(a function, f) four times

def do_four(f):
    for i in range(4):
        f()

# a function that prints one dash row

def print_dash_row():
    print("+ - - - - "*4 + "+")
    
# a function that prints one bar row

def print_bar_row():
    print("|         "*4 + "|")
    
# a function that integrates one dash row and four bar rows

def print_db_row():
    print_dash_row()
    do_four(print_bar_row)

def print_4x4_grid():
    do_four(print_db_row)
    print_dash_row()

print_4x4_grid()