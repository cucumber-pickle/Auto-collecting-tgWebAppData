import time
from pywinauto.keyboard import send_keys
import pyautogui
from src.core import load_accounts_from_file, launch_telegram, close_telegram
from src.cucumber import _banner, log, mrh, pth, hju, kng, bru, htm
from src.core_change_name import click_button, paste_to_name

# Function to search and click on the link
def click_link(bot_name):  # Give time for the link to display

    link = fr"pic\bots\{bot_name}.png"
    try:
        link_location = pyautogui.locateOnScreen(link, confidence=0.7)
        time.sleep(1)

    except Exception as e:
        log(f'Error while searching for image {bot_name}: {e}')

    if link_location:
        log(hju + "Link found. Clicking on it...")
        pyautogui.click(pyautogui.center(link_location))
        time.sleep(2)  # Delay before pressing Enter
        send_keys('{ENTER}')  # Press Enter after 3 seconds
    else:
        log("Failed to find the link.")

# Function to interact with the bot
def interact_with_bot(app):
    log("Focusing on the Telegram window...")
    main_window = app.top_window()
    main_window.set_focus()

    click_button("lines")

    click_button("settings")

    click_button("account")

    click_button("name")

    paste_to_name()

    click_button("save")


# Main function for working with multiple accounts
def main(account):
    try:
        app, exe_file = launch_telegram(account)
        interact_with_bot(app)

    except Exception as e:
        log(mrh + f"Error while interacting with account {account} : {e}")
        open("error.log", "a", encoding="utf-8").write(
            f"Error while interacting with account {account} : {e} \n")

    finally:
        close_telegram(account, exe_file)


# Loading accounts and bots
accounts_list = load_accounts_from_file('acc.txt')

# Get the total number of accounts
total_accounts = len(accounts_list)

_banner()

log(f'Total accounts to process: {bru} {total_accounts}')

row = 1

for index, account in enumerate(accounts_list, start=1):
    log(f'Processing account {bru} {index} of {total_accounts}...')
    row += 1
    main(account)