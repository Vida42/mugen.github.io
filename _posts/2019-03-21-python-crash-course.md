---
layout:     post
title:      "Python Crash Course Part I: Basics"
subtitle:   " \"Notes\""
date:       2019-03-21 10:00:00
author:     "Mugen"
header-img: "img/post-bg-os-metro.jpg"
tags:
    - Python Book
    - Book Notes
---

> A hands-on, project-based introduction to programming.

# 1. Python Installation

> Nothing important


# 2. Variables and simple data types

> In this chapter you’ll learn about the different kinds of data you can work with in your Python programs, and you’ll learn to use variables as well.

## Variables

Every variable holds a value, which is the information associated with that variable.

### Naming and Using Variables

Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.

Breaking some of these rules will cause errors; other guidelines just help you write code that’s easier to read and understand.

Be sure to keep the following variable rules in mind:

- Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.

- Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names.

- Avoid using Python keywords and function names as variable names.

- Variable names should be short but descriptive.

## Strings

In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols.

```python
name = "ada lovalace"
print(name.title())
print(name.upper())
print(name.lower())
```

## Numbers

## Comments

The main reason to write comments is to explain what your code is supposed to do and how you are making it work. When you’re in the middle of working on a project, you understand how all of the pieces fit together. But when you return to a project after some time away, you’ll likely have forgotten some of the details. You can always study your code for a while and figure out how segments were supposed to work, but writing good comments can save you time by summarizing your overall approach in clear English.

If you want to become a professional programmer or collaborate with other programmers, you should write meaningful comments. Today, most software is written collaboratively, whether by a group of employees at one company or a group of people working together on an open source project. Skilled programmers expect to see comments in code, so it’s best to start adding descriptive comments to your programs now. Writing clear, concise comments in your code is one of the most beneficial habits you can form as a new programmer.

## The Zen of Python

```python
import this
```


# 3. Introducing Lists

> Lists allow you to store sets of information in one place, whether you have just a few items or millions of items. Lists are one of Python’s most powerful features readily accessible to new programmers, and they tie together many important concepts in programming.

A *list* is a collection of items in a particular order.

## Changing, Adding, and Removing Elements

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
>>> ['honda', 'ducati', 'yamaha', 'suzuki']

del motorcycles[2]
>>> ['honda', 'ducati', 'suzuki']

motorcycles.pop()
>>> 'suzuki'
# you can pop item from any posotion by including the index

motorcycles.remove('honda')
>>> ['ducati']
# The remove() method deletes only the first occurrence of the value you specify.
```


# 4. Working With Lists

> *loop*

## Tuples

> Sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

> A tuple looks just like a list except you use parentheses instead of square brackets.

## Styling Your Code

The Python style guide was written with the understanding that code is read more often than it is written.

Given the choice between writing code that’s easier to write or code that’s easier to read, Python programmers will almost always encourage you to write code that’s easier to read. The following guidelines will help you write clear code from the start.

### Indentation
PEP 8 recommends that you use four spaces per indentation level.

### Line Length
Many Python programmers recommend that each line should be less than 80 characters.

### Blank Lines


# 5. If Statements

> Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's *if* statement allows you to examine the current state of a program and respond appropriately to that state.

Python does not require an *else* block at the end of an *if-elif* chain. Sometimes an *else* block is useful; sometimes it is clearer to use an additional *elif* statement that catches the specific condition of interest.


# 6. Dictionaries

> In this chapter you’ll learn how to use Python’s dictionaries, which allow you to connect pieces of related information.

```python
for key, value in user_0.items():
# Looping Through All Key-Value Pairs

for name in favorite_languages.keys():
# Looping Through All the Keys in a Dictionary

for language in favorite_languages.values():
# Looping Through All Values in a Dictionary
```

## Nesting

Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. This is called nesting. You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary. Nesting is a powerful feature, as the following examples will demonstrate.


# 7. User Input and while Loops

## How the input() Function Works

The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it stores it in a variable to make it convenient for you to work with.

The input() function takes one argument: the prompt, or instructions, that we want to display to the user so they know what to do.

### The Modulo Operator

> the *modulo operator* (%)


# 8. Functions

/>>> *function definition*+*body*(*docstring*)

/<<< *function call*

When you are passing arguments, you can use **Positional Arguments** or **Keyword Arguments**. You can also define a *default value* for each parameter when writing a function.


# 9. Classes

> In object-oriented programming you write *classes* that represent real-world things and situations, and you create *objects* based on these classes.

## Creating and Using a Class

By convention, capitalized names refer to classes in Python.

*Class, methods(functions), instance, attributes*

## Inheritance

> see code of TRY IT YOURSELF in [*HERE*](https://github.com/Vida42/Vida42.github.io/blob/master/file/in-post/practice_0.py)

If the class you’re writing is a specialized version of another class you wrote, you can use *inheritance*. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The original class is called the *parent class*, and the new class is the *child class*.

We start with Car. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.

```python
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
```

We define the child class, ElectricCar. The name of the parent class must be included in parentheses in the definition of the child class.

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
```

The `__init__()` method takes in the information required to make a Car instance.

The `super()` function is a special function that helps Python make connections between the parent and child class. This line tells Python to call the `__init__()` method from ElectricCar's parent class, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a `superclass` and the child class a `subclass`.

```python
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
>>> 2016 Tesla Model S
```

### Overriding Methods from the Parent Class

When you use inheritance, you can make your child classes retain what you need and override anything you don't need from the parent class.


## The Python Standard Library

> Instances of the *OrderedDict* class behave almost exactly like dictionaries except they keep track of the order in which key-value pairs are added.

```python
from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
```


# 10. Files and Exceptions

> In Chapter 10 you’ll learn to work with files so you can save the work you’ve done in a program and the work you’ve allowed users to do. You’ll also learn about exceptions, a special Python class designed to help you respond to errors when they arise.

## Storing Data

> The `json` module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs.

## Refactoring

Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called `refactoring`. Refactoring makes your code cleaner, easier to understand, and easier to extend.

> See the example in [*HERE*](https://github.com/Vida42/Vida42.github.io/blob/master/file/in-post/practice_1.py)


# 11. Testing Your Code

> Testing proves that your code works as it’s supposed to in response to all the input types it’s designed to receive. Every programmer makes mistakes, so every programmer must test their code often, catching problems before users encounter them.

## Testing a Function

The module `unittest` from the Python standard library provides tools for testing your code. A `unit test` verifies that one specific aspect of a function’s behavior is correct. A `test case` is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.

A test case with `full coverage` includes a full range of unit tests covering all the possible ways you can use a function.

```python
import unittest

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

## Testing a Class

### A Variety of Assert Methods

Python provides a number of `assert` methods in the `unittest.TestCase` class. As mentioned earlier, `assert` methods test whether a condition you believe is true at a specific point in your code is indeed true.

*Assert Methods Available from the unittest Module*

|**Method**|**Use**|
|---|---|
|assertEqual(a, b)      | Verify that a == b|
|assertNotEqual(a, b)   | Verify that a != b|
|assertTrue(x)          | Verify that x is True|
|assertFalse(x)         | Verify that x is False|
|assertIn(item, list)   | Verify that item is in list|
|assertNotIn(item, list)| Verify that item is not in list|


