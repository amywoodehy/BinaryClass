from bin import *

a = BinWord(10)
print("a = BinWord(10) \n", a)

b = a
print("b = a\n", b)

c = BinWord(100)
print("c = BinWord(100) \n", c)

a.fill(len(c))
print("a.fill(len(c))\n", a)

d = BinWord(c)
print("d = BinWord(c)\n", d)