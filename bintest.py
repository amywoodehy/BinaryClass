from bin import *

a = BinWord(3)
print("a = BinWord(10) \n", a)

b = a
print("b = a\n", b)

c = BinWord(100)
print("c = BinWord(100) \n", c)

a.fill(len(c))
print("a.fill(len(c))\n", a)

eqlen(b, c)
print("eqlen(b, c)\n", (b,c))

d = BinWord("ababa", True)
print("d = BinWord('ababa', True)\n", d)

#er = BinWord("asdasd", True)
#print("expected error\ner = BinWord('asdasd', True)\n", er)

f = abs(d)
print("f = abs(d)\n", f)

g = a + c
print("g = a + c\n", g)

#invering the image of the bin word
h = ~g
print("h = ~g\n", h)

