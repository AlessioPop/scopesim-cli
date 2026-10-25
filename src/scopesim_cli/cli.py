import questionary as q

def main():
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
            print("...")

if __name__ == "__main__":
    main()