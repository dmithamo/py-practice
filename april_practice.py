import math # For challenges requiring the math module, e.g #3

"""
1.

Usually when you buy something, you're asked whether your 
credit card number, phone number or answer to 
your most secret question is still correct. However, since someone 
could look over your shoulder, you don't want that shown on your screen. 
Instead, we mask it.

Your task is to write a function maskify, 
which changes all but the last four characters into '#'.
"""

# Return masked string
def maskify(cc):
    
    return "{}{}".format("#"*len(cc[4:]), cc[-4:])

"""
2. 

You are going to be given a word. 
Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. 
If the word's length is even, return the middle 2 characters.
"""

def get_middle(s):
    if len(s) % 2 == 0:
        return "{}{}".format(s[len(s)//2-1], s[len(s)//2])
    else:
        return "{}".format(s[len(s)//2])

"""
4.

A square of squares

You like building blocks. You especially like building blocks 
that are squares. And what you even like more, is to arrange them into 
a square of square building blocks!

However, sometimes, you can't arrange them into a square. 
Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a 
way to know, whether you're currently working in vain… Wait! That's it! You just 
have to check if your number of building blocks is a perfect square.
"""

def is_square(n):
    return n > 0 and (n**0.5).is_integer()

"""
5.

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

"""
def get_count(input_str):
    num_vowels = 0
    vowels = "aeiouAEIOU"
    for letter in input_str:
        if letter in vowels:
            num_vowels += 1
    return num_vowels


"""
6. 
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    seq_count = {element: seq.count(element) for element in seq}
    for k, v in seq_count.items():
        if v % 2 != 0:
            return k


"""
7. 
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and 
returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than 
one word is present.
"""
def spin_words(sentence):
    words = sentence.split(" ")
    for i, word in enumerate(words):
        if len(words[i]) >= 5:
            words[i] = word[::-1]
    return " ".join(words)

