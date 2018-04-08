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
    if n < 0:
        return False
    else:
        return round(math.sqrt(n), 2) == round(math.sqrt(n))

print(is_square(-100))
print(is_square(10))
print(is_square(4))

