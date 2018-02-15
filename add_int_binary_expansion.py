'''
ALGORITHM 2 Addition of Integers.
procedure add(a, b: positive integers)
{the binary expansions of a and b are (an−1an−2 . . . a1a0)2
and (bn−1bn−2 . . . b1b0)2, respectively}
c := 0
for j := 0 to n − 1
d := (aj + bj + c)/2
sj := aj + bj + c − 2d
c := d
sn := c
return (s0, s1, . . . , sn) {the binary expansion of the sum is (snsn−1 . . . s0)2}

example: 
I want to add 1110 + 1011: 
add_binary(1110,1011)
output: 
[1,1,0,0,1]
'''

import math
def add_binary(a, b):
    #turns int into a list
    lst_a = [int(i) for i in str(a)]
    lst_b = [int(i) for i in str(b)]
    #if the list is smaller it adds a 0 to index 0
    if (len(lst_a)<len(lst_b)):
        while len(lst_a) != len(lst_b):
            lst_a.insert(0,0)
    else:
        while len(lst_a) != len(lst_b):
            lst_b.insert(0,0)

    #flips the list around in order for the code to match the algorithm        
    lst_a = lst_a[::-1]
    lst_b = lst_b[::-1]
    maxlength = max(len(lst_a), len(lst_b))
    c = 0
    s = []
    for w in range(maxlength):
        d = math.floor((lst_a[w]+lst_b[w]+c)/2)
        s.append(lst_a[w]+lst_b[w]+c-(2*d))
        c = d
        
    s.append(c)
    
    s =s[::-1]
    #print (s)

    return s
