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

print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("of"))
         