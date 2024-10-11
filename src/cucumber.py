from datetime import datetime
import os
from colorama import Fore, Style


mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX


def log(message):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"{htm}[{now}]{pth} {message}{reset}")

def _banner():
    banner = r"""
  _____   _    _    _____   _    _   __  __   ____    ______   _____  
 / ____| | |  | |  / ____| | |  | | |  \/  | |  _ \  |  ____| |  __ \ 
| |      | |  | | | |      | |  | | | \  / | | |_) | | |__    | |__) |
| |      | |  | | | |      | |  | | | |\/| | |  _ <  |  __|   |  _  / 
| |____  | |__| | | |____  | |__| | | |  | | | |_) | | |____  | | \ \ 
 \_____|  \____/   \_____|  \____/  |_|  |_| |____/  |______| |_|  \_\ """
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
    log_line()
    print(hju + f" Auto collecting tgWebAppData")
    print(mrh + f" FREE TO USE = Join us on {pth}t.me/cucumber_scripts")
    print(mrh + f" before start please '{hju}git pull{mrh}' to update bot")
    log_line()


def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def log_line():
    print(pth + "~" * 60)