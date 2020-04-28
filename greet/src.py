import pkg_resources
from colorama import Fore


def greet(name: str) -> None:
    """Greet"""

    prefix = pkg_resources.resource_string(__name__, "greet.txt").decode().strip()

    print(Fore.RED + f"Hello, {prefix} {name}")
