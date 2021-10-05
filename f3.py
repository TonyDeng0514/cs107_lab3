"""
Lab 3: complexity revisited -- recall ...

f3(n)   === 1  if n < 3
        === f3(n-1) + f3(n-2) + f3(n-3)

>>> print(4, f3(4))
4 5

>>> print(10, f3(10))
10 193

"""

import time
import math

def f3loop(n: int) -> int:
    return 1            # REPLACE THIS WITH YOUR CODE

def f3tail(n: int) -> int:
    return 1            # REPLACE THIS WITH YOUR CODE

f3 = f3loop             # replace with name of function to execute/test

""" if you want to time, remove comment delimiters

start = time.time()
for n in range(100, 1001, 100):
    print(n, f3(n))
stop = time.time()
print("elapsed time: ", stop - start)
"""

if __name__ == "__main__":
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    doctest.testmod()
    print("doctests complete")
