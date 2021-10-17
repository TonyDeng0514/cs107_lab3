"""
Gadsby:a text w/out 'e'

Goal is to confirm/refute that the text does not contain the letter 'e' as claimed.

Text source file, see: https://en.wikisource.org/wiki/Gadsby

Python3 file I/O: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""

lineCount = 0

# loop over file object
with open('GadsbyTrimmed.txt') as f:    # EXTEND CODE TO HUNT FOR 'e's
    for line in f:
        print(line[1])
        lineCount += 1

print("line count: ", lineCount)

