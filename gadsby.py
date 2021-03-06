"""
Gadsby:a text w/out 'e'

Goal is to confirm/refute that the text does not contain the letter 'e' as claimed.

Text source file, see: https://en.wikisource.org/wiki/Gadsby

Python3 file I/O: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""


'''
Result: refute the claim.
There are four 'e' found in the whole passage.
'''

lineCount = 0
check = 0
# loop over file object
with open('GadsbyTrimmed.txt', encoding = 'utf-8') as f:    # EXTEND CODE TO HUNT FOR 'e's
    for line in f:      # for each line
        lineCount += 1
        for i in line:  # for each item in each line
            if i == 'e':  # compare
                check += 1 # and count
                print(lineCount)  # print out the lines where we found e.

if check == 0:
    print("no e.")
else:
    print('yes e, ', check, " of them.")
            

print("line count: ", lineCount)

