"""
List Comprehension (and loops) for the intersection of two lists
Here are some test cases, please add others, esp. extreme cases.

Beware, the first answer may be in any order and still correct -- jd


>>> in_common(['NJ', 'PA', 'CA', 'WA'],['WA', 'PA', 'GA', 'VA'])
['PA', 'WA']

>>> in_common(['NJ', 'PA', 'CA', 'WA'],['WV', 'DE', 'GA', 'VA'])
[]

>>> in_common(['a','o','e'],['i','u','v'])
[]

>>> in_common(['1','2','tony','tony'],['tony'])
['tony']
"""

def in_common_loops(a: list, b: list)-> list:
    outlst = []  # innocent output list
    for i in a:  # loop through all the element in the first list
        for j in b:  # compare to each of the second element
            if i == j:
                outlst.append(j)  # if match, append to the output list
    return outlst      


def in_common_LC(a: list, b: list)-> list:
    outlst = []  # innocent output list
    [outlst.append(i) for i in a if i in b and i not in outlst]     # use list comprehension to append it
                                                                    # feels like cheating, but acutally not lol.
    return outlst

in_common = in_common_LC    # set the function name here to execute/test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")

