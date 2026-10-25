import questionary as q
import os
from .utils import *
from .config import *

def main():

    clear()

    while True:
        choice = q.select(
            "scopesim-cli",
            choices=[
                "Setup Instrument",
                "Exit"
            ]
        ).ask()

        if choice == "Exit":
            break
        else:
            clear()

            # ask user which instrument: METIS, MICADO etc

            setup_instrument()

if __name__ == "__main__":
    main()