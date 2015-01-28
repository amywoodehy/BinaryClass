from bin2 import *
import os
import time

os.system("cls")
print("You are running python script on", os.name)
#
#Creating new object
print("\n\tCreating new object\n")
#
a = Word(3)
print(">>>a = Word(10)\n", a)

b = a
print(">>>b = a\n", b)

a = ~a
print(">>>a = ~a\n", a)
print(">>>b\n",b)

c = Word(10000111, 32)
print(">>>c = Word(130000111, 32)\n", c)

a.fill(len(c))
print(">>>a.fill(len(c))\n", a)

eqlen(b, c)
print(">>>eqlen(b, c)\n", b,c)

eqlento(a, c)
print(">>>eqlento(a, c)\n", a,c)

d = Word("ababa")
print(">>>d = Word('ababa')\n", d)

g = a + b
print(">>>g = a + b\n", g)

g = a + c
print(">>>g = a + c\n", g)

os.system("pause")

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
j = Word(1337)
print("j = Word(1337)\n", j)

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

os.system("pause")
os.system("cls")