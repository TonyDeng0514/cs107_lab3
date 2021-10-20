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
>>> assert palindrome("Mom")
>>> assert palindrome('hello olleh')
>>> assert palindrome('Aibohphobia')
>>> assert palindrome('Baby Bab')
"""

def palindrome(s: str)-> bool:
    if len(s) == 0:  # make sure the input is not nothing.
        raise ValueError

    s = s.lower()    # switch everything to lower case since computer
                     # doesn't know M and m are the same lol.

    lst1 = list(s)   # turn the input string into a list.
    
    for i in lst1:   # remove all the space from the list.
        if i == " ":
            lst1.remove(i)

    l = len(lst1)
    lst2 = [lst1[-i] for i in range(1,l+1)] # list comprehension! Flip the list
    if lst1 == lst2:  # compare.
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")
