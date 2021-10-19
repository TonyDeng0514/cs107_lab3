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
    outlst = []
    for i in a:
        for j in b:
            if i == j:
                outlst.append(j)
    return outlst      #REPLACE WITH YOUR CODE


def in_common_LC(a: list, b: list)-> list:
    outlst = []
    [outlst.append(i) for i in a if i in b and i not in outlst]     #REPLACE WITH YOUR CODE
    return outlst

in_common = in_common_LC    # set the function name here to execute/test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests passed")

