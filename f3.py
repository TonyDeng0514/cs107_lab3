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
# import math
# importing the sys module
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**6)

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


f3 = f3loop            # replace with name of function to execute/test

# if you want to time, remove comment delimiters

start = time.time()
for n in range(100, 1001, 100):
    print(n, f3(n))
stop = time.time()
print("elapsed time: ", stop - start)


'''
For tail recursion method.
Trial 1: time is 0.004 sec.
Trial 2: time is 0.003 sec.
Trial 3: time is 0.003 sec.
Trial 4: time is 0.004 sec.
Trial 5: time is 0.004 sec.
Trial 6: time is 0.004 sec.
Trial 7: time is 0.003 sec.
Trial 8: time is 0.004 sec.
Trial 9: time is 0.003 sec.
Trial 10: time is 0.004 sec.
Trial 11: time is 0.003 sec.
Trial 12: time is 0.004 sec.
Trial 13: time is 0.003 sec.
Trial 14: time is 0.003 sec.
Trial 15: time is 0.004 sec.
The average time is .0035 sec.
The standard deviation is .0005 sec.

For loop method.
Trial 1: time is 0.002 sec.
Trial 2: time is 0.002 sec.
Trial 3: time is 0.001 sec.
Trial 4: time is 0.002 sec.
Trial 5: time is 0.002 sec.
Trial 6: time is 0.002 sec.
Trial 7: time is 0.002 sec.
Trial 8: time is 0.002 sec.
Trial 9: time is 0.001 sec.
Trial 10: time is 0.002 sec.
Trial 11: time is 0.001 sec.
Trial 12: time is 0.002 sec.
Trial 13: time is 0.001 sec.
Trial 14: time is 0.002 sec.
Trial 15: time is 0.001 sec.
The average time is .0017 sec.
The standard deviation is .0005 sec.

Through the data we collected, it is obvious that the loop version of f3 is faster than the 
tail recursion version of it.
However, both are significantly faster than the recursion version.

I'm actually surprised by this result since I thought recursion should always be faster than
other type of algorithms, especially in for f3.
Nevertheless, I could have overlooked the fact that f3 has base 3 so any recursion around it would
have execution time that is a power of 3.

The reason why tail recursion is slower than the loop version is probably the sample is still
too small. If we go up to 100000, tail recursion is probably faster than loop.
'''


if __name__ == "__main__":
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    doctest.testmod()
    print("doctests complete")
