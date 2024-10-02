import os

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')