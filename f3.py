"""
Lab 3: complexity revisited -- recall ...

f3(n)   === 1  if n < 3
        === f3(n-1) + f3(n-2) + f3(n-3)

>>> print(4, f3(4))
4 5

>>> print(10, f3(10))
10 193

>>> print(0, f3(0))
0 1

>>> print(1, f3(1))
1 1

>>> print(3, f3(3))
3 3

>>> print(5, f3(5))
5 9

>>> print(6, f3(6))
6 17

>>> print(15, f3(15))
15 4063

>>> print(2, f3(2))
2 1
"""

import time
import math

def f3loop(n: int) -> int:
    assert n >= 0
    answer = 1
    prev = 1 # base case 0
    prev2 = 1 # base case 1
    # prev3 = 1 base case 2, but no need to define it outside the loop
    for i in range(n-2):
        prev3 = prev2
        prev2 = prev
        prev = answer
        answer = prev + prev2 + prev3
    return answer

                       

def f3tail(n: int) -> int:
    def fib_helper(n:int, answer:int, prev:int, prev2:int, i:int)-> int:
        # n is the input number, i is the largest input for base case.
        # answer is the supposed output
        # prev is previous answer
        # prev2 is a slot that to contain prev
        if i >= n:
            return answer
        else:
            # the next answer is the sum of the previous three items
            return fib_helper(n, prev+answer+prev2, answer, prev, i+1)
        
    
    assert n >= 0

    return fib_helper(n, 1, 1, 1, 2)


f3 = f3tail            # replace with name of function to execute/test

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
