import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid font")
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

text = input("Input: ")
print(figlet.renderText(text))
