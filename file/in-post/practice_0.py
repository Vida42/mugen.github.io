# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Date    : 2019-03-23 12:23:38
# # @Author  : Amano
# # @Version : $Id$

'''
try it yourself 9-6

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)


class IceCreamStand(Restaurant):
    """A class representing a icecreamstand"""

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_info(self):
        """Display what is included."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

iceream1 = IceCreamStand('The Big One', 'ice_cream', ['vanilla', 'chocolate', 'black cherry'])
iceream1.describe_restaurant()
iceream1.display_info()

'''

'''
try it yourself 9-7

class User():
    """A class representing a user."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        msg = self.first_name.title() + ' ' + self.last_name.title()
        print("\n" + msg)

    def greet_user(self):
        msg = self.first_name.title() + ' ' + self.last_name.title()
        print("\n" + "hello to " + msg)


class Admin(User):
    """A class representing an admin."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        """Display what is included."""
        print("\nWe have the following privileges.")
        for each in self.privileges:
            print("- " + each.title())

admin1 = Admin('eric', 'matthes')
admin1.privileges = ['can reset passwords',
                    'can moderate discussions',
                    'can suspend accounts',
                    ]
admin1.greet_user()
admin1.show_privileges()

'''

'''
try it yourself 9-8

class Privileges():
    """A class to store an admin's privileges."""
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:        
            for each in self.privileges:
                print("- " + each.title())
        else:
            print("- This user has no privileges.")


class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


eric = Admin('eric', 'matthes')
eric.describe_user()
eric.privileges.show_privileges()
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()

'''