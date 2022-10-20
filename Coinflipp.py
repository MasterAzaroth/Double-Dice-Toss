from random import randint

from pyfiglet import Figlet

Coinflipp = randint(1,2)

f = Figlet()

if Coinflipp == 1:
    print(f.renderText("heads"))

if Coinflipp == 2:
    print(f.renderText("tails"))