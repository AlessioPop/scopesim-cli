import os

__all__ = [
    "clear"
]

def clear():
    """
    Clears terminal
    """
    return os.system("clear")

if __name__ == "__main__":
    clear()