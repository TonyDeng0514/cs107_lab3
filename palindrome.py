"""
Palindrome predicate: here are a few tests cases,
please add a few more, esp. extreme

>>> assert palindrome("mom")
>>> assert not palindrome("mother")
>>> assert palindrome("kopok")
>>> assert palindrome("a")

# this should raise value error
# >>> assert palindrome('')

>>> assert not palindrome('Tony')
>>> assert not palindrome("Mom")
>>> assert palindrome('hello olleh')
"""

def palindrome(s: str)-> bool:
    if len(s) == 0:
        raise ValueError
    lst1 = list(s)
    l = len(lst1)
    lst2 = [lst1[-i] for i in range(1,l+1)]
    if lst1 == lst2:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")
