from random import randint
from re import M

from pyfiglet import Figlet

f = Figlet()

zufall_1 = randint(1,6)
zufall_2 = randint(1,6)

combination_1 = """
 ____________    ____________
|             | |             |
|             | |             |
|      O      | |      O      |
|             | |             |
|____________ | |____________ |
"""

combination_2 = """
 ____________    ____________
|             | |O            |
|             | |             |
|      O      | |             |
|             | |             |
|____________ | |____________O|
"""

combination_3 = """
 ____________    ____________
|             | |O            |
|             | |             |
|      O      | |      O      |
|             | |             |
|____________ | |____________O|
"""

combination_4 = """
 ____________    ____________
|             | |O           O|
|             | |             |
|      O      | |             |
|             | |             |
|____________ | |O___________O|
"""

combination_5 = """
 ____________    ____________
|             | |O           O|
|             | |             |
|      O      | |      O      |
|             | |             |
|____________ | |O___________O|
"""

combination_6 = """
 ____________    ____________
|             | |O           O|
|             | |             |
|      O      | |O           O|
|             | |             |
|____________ | |O___________O|
"""

combination_7 = """
 ____________    ____________
|O            | |             |
|             | |             |
|             | |      O      |
|             | |             |
|____________O| |____________ |
"""

combination_8 = """
 ____________    ____________
|O            | |O            |
|             | |             |
|             | |             |
|             | |             |
|____________O| |____________O|
"""

combination_9 = """
 ____________    ____________
|O            | |O            |
|             | |             |
|             | |      O      |
|             | |             |
|____________O| |____________O|
"""

combination_10 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|             | |             |
|             | |             |
|____________O| |O___________O|
"""

combination_11 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|             | |      O      |
|             | |             |
|____________O| |O___________O|
"""

combination_12 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|             | |O           O|
|             | |             |
|____________O| |O___________O|
"""

combination_13 = """
 ____________    ____________
|O            | |             |
|             | |             |
|      O      | |      O      |
|             | |             |
|____________O| |____________ |
"""

combination_14 = """
 ____________    ____________
|O            | |O            |
|             | |             |
|      O      | |             |
|             | |             |
|____________O| |____________O|
"""

combination_15 = """
 ____________    ____________
|O            | |O            |
|             | |             |
|      O      | |      O      |
|             | |             |
|____________O| |____________O|
"""

combination_16 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|      O      | |             |
|             | |             |
|____________O| |O___________O|
"""

combination_17 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|      O      | |      O      |
|             | |             |
|____________O| |O___________O|
"""

combination_18 = """
 ____________    ____________
|O            | |O           O|
|             | |             |
|      O      | |O           O|
|             | |             |
|____________O| |O___________O|
"""

combination_19 = """
 ____________    ____________
|O           O| |             |
|             | |             |
|             | |      O      |
|             | |             |
|O___________O| |____________ |
"""

combination_20 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|             | |             |
|             | |             |
|O___________O| |____________O|
"""

combination_21 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|             | |      O      |
|             | |             |
|O___________O| |____________O|
"""

combination_22 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|             | |             |
|             | |             |
|O___________O| |O___________O|
"""

combination_23 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|             | |      O      |
|             | |             |
|O___________O| |O___________O|
"""

combination_24 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|             | |O           O|
|             | |             |
|O___________O| |O___________O|
"""

combination_25 = """
 ____________    ____________
|O           O| |             |
|             | |             |
|      O      | |      O      |
|             | |             |
|O___________O| |____________ |
"""

combination_26 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|      O      | |             |
|             | |             |
|O___________O| |____________O|
"""

combination_27 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|      O      | |      O      |
|             | |             |
|O___________O| |____________O|
"""

combination_28 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|      O      | |             |
|             | |             |
|O___________O| |O___________O|
"""

combination_29 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|      O      | |      O      |
|             | |             |
|O___________O| |O___________O|
"""

combination_30 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|      O      | |O           O|
|             | |             |
|O___________O| |O___________O|
"""

combination_31 = """
 ____________    ____________
|O           O| |             |
|             | |             |
|O           O| |      O      |
|             | |             |
|O___________O| |____________ |
"""

combination_32 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|O           O| |             |
|             | |             |
|O___________O| |____________O|
"""

combination_33 = """
 ____________    ____________
|O           O| |O            |
|             | |             |
|O           O| |      O      |
|             | |             |
|O___________O| |____________O|
"""

combination_34 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|O           O| |             |
|             | |             |
|O___________O| |O___________O|
"""

combination_35 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|O           O| |      O      |
|             | |             |
|O___________O| |O___________O|
"""

combination_36 = """
 ____________    ____________
|O           O| |O           O|
|             | |             |
|O           O| |O           O|
|             | |             |
|O___________O| |O___________O|
"""

if zufall_1 == 1 and zufall_2 == 1:
    print(combination_1)
if zufall_1 == 1 and zufall_2 == 2:
    print(combination_2)
if zufall_1 == 1 and zufall_2 == 3:
    print(combination_3)
if zufall_1 == 1 and zufall_2 == 4:
    print(combination_4)
if zufall_1 == 1 and zufall_2 == 5:
    print(combination_5)
if zufall_1 == 1 and zufall_2 == 6:
    print(combination_6)
if zufall_1 == 2 and zufall_2 == 1:
    print(combination_7)
if zufall_1 == 2 and zufall_2 == 2:
    print(combination_8)
if zufall_1 == 2 and zufall_2 == 3:
    print(combination_9)
if zufall_1 == 2 and zufall_2 == 4:
    print(combination_10)
if zufall_1 == 2 and zufall_2 == 5:
    print(combination_11)
if zufall_1 == 2 and zufall_2 == 6:
    print(combination_12)
if zufall_1 == 3 and zufall_2 == 1:
    print(combination_13)
if zufall_1 == 3 and zufall_2 == 2:
    print(combination_14)
if zufall_1 == 3 and zufall_2 == 3:
    print(combination_15)
if zufall_1 == 3 and zufall_2 == 4:
    print(combination_16)
if zufall_1 == 3 and zufall_2 == 5:
    print(combination_17)
if zufall_1 == 3 and zufall_2 == 6:
    print(combination_18)
if zufall_1 == 4 and zufall_2 == 1:
    print(combination_19)
if zufall_1 == 4 and zufall_2 == 2:
    print(combination_20)
if zufall_1 == 4 and zufall_2 == 3:
    print(combination_21)
if zufall_1 == 4 and zufall_2 == 4:
    print(combination_22)
if zufall_1 == 4 and zufall_2 == 5:
    print(combination_23)
if zufall_1 == 4 and zufall_2 == 6:
    print(combination_24)
if zufall_1 == 5 and zufall_2 == 1:
    print(combination_25)
if zufall_1 == 5 and zufall_2 == 2:
    print(combination_26)
if zufall_1 == 5 and zufall_2 == 3:
    print(combination_27)
if zufall_1 == 5 and zufall_2 == 4:
    print(combination_28)
if zufall_1 == 5 and zufall_2 == 5:
    print(combination_29)
if zufall_1 == 5 and zufall_2 == 6:
    print(combination_30)
if zufall_1 == 6 and zufall_2 == 1:
    print(combination_31)
if zufall_1 == 6 and zufall_2 == 2:
    print(combination_32)
if zufall_1 == 6 and zufall_2 == 3:
    print(combination_33)
if zufall_1 == 6 and zufall_2 == 4:
    print(combination_34)
if zufall_1 == 6 and zufall_2 == 5:
    print(combination_35)
if zufall_1 == 6 and zufall_2 == 6:
    print(combination_36)