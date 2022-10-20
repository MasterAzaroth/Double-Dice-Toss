complex(1,3)

complex_number = 1 + 2j

# print(type(complex))

wert1 = 3 #int
wert2 = 4.32 #float
wert3 = 3 + 4j #complex
wert4 = True #bool
wert5 = "Hello world" #str
wert6 = (1,2,3) #tuple
wert7 = [1,2,3] #list
wert8 = {1,2,3} #set
wert9 = {"name": "Léonard", "age": "18", "favourite color": "purple"} #dict

# print(
#     type(wert1), type(wert2), type(wert3),
#     type(wert4), type(wert5), type(wert6),
#     type(wert7), type(wert8), type(wert9)
#    )

x = 3 + 4j

# print(x.real, x.imag)

string1 = "name"
string2 = 'name'

# print (string1 == string2)

# print(string1, string2)

wert1 = 1e10
wert2 = 1E10

# print(wert1 == wert2)

# bool(0) = False
# bool(1) = True
# int(False) = 0
# int(True) = 1

a = bool(0) == False
b = bool(1) == True

# print(a, b)

wert1 = 5
wert2 = 4.32

#define wert1 as float
#define wert2 as boolean
#define wert1&2 as string

# print((float(wert1)), bool(wert2), (str(wert1), str(wert2)))

r = 3
s = 4.32
t = 3 + 4j
u = True
v = "Hello world"
w = (1,2,3)
x = [1,2,3]
y = {1,2,3}
z = {"name": "Léonard", "age": "18", "favourite color": "purple"}

a = isinstance(r, int)
b = isinstance(s, float)
c = isinstance(t, complex)
d = isinstance(u, bool)
e = isinstance(v, str)
f = isinstance(w, tuple)
g = isinstance(x, list)
h = isinstance(y, set)
i = isinstance(z, dict)

# werte = [ a, b, c, d, e, f, g, h, i ]

# for wert in werte:
#     print(wert)

from random import randint

Liste=[]

# for i in range(100):
#     randperc = randint(0,100)
#     Liste.append(randperc)
#     print(randperc)

# print(Liste)

doublecheck = [28, 94, 33, 40, 58, 0, 41, 24, 34, 61, 98, 81, 10, 84, 9, 25, 45, 11, 39, 94, 77, 
                39, 97, 23, 46, 88, 4, 37, 12, 98, 26, 71, 1, 98, 86, 78, 80, 78, 94, 49, 40, 48, 
                49, 84, 17, 43, 93, 67, 34, 37, 83, 18, 25, 92, 98, 82, 46, 66, 57, 97, 20, 78, 85, 
                26, 34, 75, 1, 11, 60, 0, 40, 53, 30, 38, 25, 36, 3, 59, 72, 66, 38, 37, 64, 18, 4, 
                34, 3, 29, 71, 90, 20, 77, 30, 39, 43, 39, 24, 67, 80, 52]

# from collections import Counter
# count = Counter(doublecheck)
# print(count)

# Counter({34: 4, 98: 4, 39: 4, 94: 3, 40: 3, 25: 3, 37: 3, 78: 3, 0: 2, 24: 2, 84: 2, 11: 2, 
#         77: 2, 97: 2, 46: 2, 4: 2, 26: 2, 71: 2, 1: 2, 80: 2, 49: 2, 43: 2, 67: 2, 18: 2, 
#         66: 2, 20: 2, 30: 2, 38: 2, 3: 2, 28: 1, 33: 1, 58: 1, 41: 1, 61: 1, 81: 1, 10: 1, 
#         9: 1, 45: 1, 23: 1, 88: 1, 12: 1, 86: 1, 48: 1, 17: 1, 93: 1, 83: 1, 92: 1, 82: 1, 
#         57: 1, 85: 1, 75: 1, 60: 1, 53: 1, 36: 1, 59: 1, 72: 1, 64: 1, 29: 1, 90: 1, 52: 1})

from fractions import Fraction
x = 1.5
# print(Fraction(x))

x = 19
y = 3

a = x // y
b = x % y
c = x ** y
d = x * y
e = x + y ** 2

Loesungen = [a, b, c, d, e]

# for wert in Loesungen:
#     print (wert)

string1 = "Hallo"
string2 = " Welt"

a = string1 + string2
b = string1 * 2

# print(a, b)