"""
Palindrome predicate: here are a few tests cases,
please add a few more, esp. extreme

>>> assert palindrome("mom")
>>> assert not palindrome("mother")
"""

def palindrome(s: str)-> bool:
    return True     # REPLACE WITH YOUR CODE


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")
