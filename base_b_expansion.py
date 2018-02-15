'''
ALGORITHM 1 

Constructing Base b Expansions.
procedure base b expansion(n, b: positive integers with b > 1)
q := n
k := 0
while q = 0
ak := q mod b
q := q div b
k := k + 1
return (ak−1, . . . , a1, a0) {(ak−1 . . . a1a0)b is the base b expansion of n}
'''
import math
def expansion_of_n(n, b):
    q = n
    k = 0
    a = []
    i = (len(str(n)))
    while q != 0:
        a.append(q%b)
        q=math.floor(q/b)
    
    if (b==16):
        for element in range(len(a)):
            if a[element] == 10:
                a[element] = 'A'
            elif a[element] == 11:
                a[element] = 'B'
            elif a[element] == 12:
                a[element] = 'C'
            elif a[element] == 13:
                a[element] = 'D'
            elif a[element] == 14:
                a[element] = 'E'
            elif a[element] == 15:
                a[element] = 'F'


    print (a[::-1])
