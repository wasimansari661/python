#to print the strings in alphabetical order

import sys
n = len(sys.argv)
print(n)
d = []
for i in range(1,n):
    d.insert(i-1,sys.argv[i])
d.sort()
print(d)