#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-23 20:14:58
# @Author  : Amano
# @Version : $Id$

# with open ('pi_digits.txt') as f:
#     contents = f.read()
#     print(contents)

# with open ('pi_digits.txt') as f:
#     for line in f:
#         print(line.strip())

# with open ('pi_digits.txt') as f:
#     lines = f.readlines()
#     # the readlines() method takes each line from the file and stores it in a list.

# filename = 'programming.txt'
# with open(filename, 'w') as f:
#     f.write('I love Python.')


'''Version 1'''

import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username2 = json.load(f)
            print("welcome back, " + username2 + '.')
    except:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember when you come back, " + username + '!')

# The function greet_user() is doing more than just greeting the user
# it’s also retrieving a stored username if one exists
# and prompting for a new username if one doesn’t exist.

'''Version 2'''

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

# We should factor one more block of code out of greet_user().
# If the username doesn’t exist, we should move the code
# that prompts for a new username to a function dedicated to that purpose

'''Version 3'''

import json

def get_stored_username():
    """Get stored username if available."""
    --snip--

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
