""" 
Your task is to write a Python program to construct the following pattern. 
Upper part should be done in one line of code without using a loop.
Lower part can be done with any kind of loop or also with one line of code and without loops.
"""

print('* ', 2 * '* ', 3 * '* ', 4 * '* ', sep='\n')
n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
