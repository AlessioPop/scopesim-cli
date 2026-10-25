import questionary as q
import os
from .utils import *

def main():
    
    clear()

    while True:
        choice = q.select(
            "ScopeSim CLI",
            choices=[
                "Setup Instrument",
                "Exit"
            ]
        ).ask()

        if choice == "Exit":
            break
        else:
            clear()
            print("Hello World")

if __name__ == "__main__":
    main()