"""
Strings

This file talks about strings.
"""

my_string = "Hello, World!"
print(my_string)

string_with_quotes = "Hello, it's me"
print(string_with_quotes)

another_with_quotes = 'He said "You are amazing!" yesterday.'
print(another_with_quotes)

escaping_quotes = "He said \"You are amazing!\" yesterday."
print(escaping_quotes)

multiline = """Hello, World.

My name is Bruno. Welcome to my program.
"""
print(multiline)

name = "Bruno"
greeting = "Hello, " + name + "."
print(greeting)

age = 20
age_as_str = str(age)
print("You are " + age_as_str)