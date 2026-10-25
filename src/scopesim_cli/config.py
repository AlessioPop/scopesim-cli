import scopesim as sim
from pathlib import Path
import questionary as q
from .utils import *

__all__ = [
    "setup_instrument"
]

# ────────────────────────────────────────────────────────────
# setup instruments
# ────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_DIR = PROJECT_ROOT / "instrument_pkgs"

def setup_metis():
    sim.download_packages(
        ["Armazones", "ELT", "METIS"],
        save_dir=PACKAGE_DIR
    )

def setup_micado():
    sim.download_packages(
        ["Armazones", "ELT",  "MORFEO", "MICADO"],
        save_dir=PACKAGE_DIR
    )

def validate_pkg(inst : str) -> bool:
    """
    returns True if package is missing

    Params:
    -------
    instrument : str
        Takes the instrument name as input
    """

    if inst == "METIS":
        for i in ["Armazones", "ELT", "METIS"]:
            if (PACKAGE_DIR / f"{i}.zip").is_file():
                pass
            else:
                return True
            
    elif inst == "MICADO":
        for i in ["Armazones", "ELT", "MICADO", "MORFEO"]:
            if (PACKAGE_DIR / f"{i}.zip").is_file():
                pass
            else:
                return True

    return False

# ────────────────────────────────────────────────────────────
# CLI functions
# ────────────────────────────────────────────────────────────

def setup_instrument():

    instruments = {
        "METIS": setup_metis,
        "MICADO": setup_micado
    }

    choice = q.select(
        "Select Instrument",
        choices=[*instruments, "Back"]
    ).ask()

    if choice in instruments:
        clear()

        if validate_pkg(choice):
            instruments[choice]()
        else:
            print(f"{choice} is setup correctly")

if __name__ == "__main__":
    ...