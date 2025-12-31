import random
from pyfiglet import Figlet
from termcolor import colored

# Please install;
# pipenv pyfiglet and pipenv termcolor

fonts = [
    'slant', 'banner3-d', 'big', 'block',
    'bubble', 'digital', 'doom', 'isometric1',
    'mini','small', 'starwars'
]

colours = [
    'red', 'green', 'yellow', 'blue', 'magenta', 'cyan'
]

F = Figlet(font=random.choice(fonts))

print(colored(F.renderText("Happy New Year 2026"),
               random.choice(colours)))
