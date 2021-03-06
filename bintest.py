from bin import *

#
#Creating new object
print("\n\tCreating new object\n")
#
a = Word(3)
print("a = Word(10) \n", a)

b = a
print("b = a\n", b)

c = Word(100)
print("c = Word(100) \n", c)

a.fill(len(c))
print("a.fill(len(c))\n", a)

eqlen(b, c)
print("eqlen(b, c)\n", (b,c))

d = Word("ababa", True)
print("d = Word('ababa', True)\n", d)

# dd = Word("asd", True)
#
#er = Word("asdasd", True)
#print("expected error\ner = Word('asdasd', True)\n", er)
#


g = a + c
print("g = a + c\n", g)

#
#unary operators
print("\n\tUnary Operators\n")
#
h = ~g
print("h = ~g\n", h)

i = (-g) + 10
print("i = -g + 0\n", i)

j = g + '01010'
print("j = g + 'opopoop'\n", j)

f = abs(d)
print("f = abs(d)\n", f)


#
#shifts
print("\n\tShifts\n")
#
lk = j.lshift(2)
print("lk = j.lshift(2)\n", lk)
ll = j<<2
print("ll = j<<2\n", ll)

rk = j.rshift(2)
print("rk = j.rshift(2)\n", rk)
rl = j>>2
print("rl = j>>2\n", rl)

mrk = j.rshift(2, '1')
print("mrk = j.rshift(2, '1')\n", mrk)
mlk = j.lshift(2, '1')
print("mlk = j.lshift(2, '1')\n", mlk)


import os
os.system("pause")