import time
from pywinauto.keyboard import send_keys
import pyautogui
import keyboard
from global_config import codes, bot_image_paths
from src.core import (load_bots_from_file, load_accounts_from_file, launch_telegram, close_telegram,
                      write_to_excel, click_console, close_app)
from src.cucumber import _banner, log, mrh, pth, hju, kng, bru, htm


# Function to find and click on the link
def click_link():
    time.sleep(1)  # Give time for the link to appear

    for image_path in bot_image_paths:
        try:
            link_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if link_location:  # If the image is found, exit the loop
                break
        except Exception as e:
            log(f'Error while searching for image {image_path}: {e}')

    if link_location:
        log(hju + "Link found. Clicking on it...")
        pyautogui.click(pyautogui.center(link_location))
        time.sleep(1)  # Delay before pressing Enter
        send_keys('{ENTER}')  # Press Enter after 1 second
    else:
        log("Failed to find the link.")

# Function to interact with the bot
def interact_with_bot(app, bot_name, code, account_num, row):
    log("Focusing on the Telegram window...")
    main_window = app.top_window()
    main_window.set_focus()
    time.sleep(1)

    log("Opening search...")
    main_window.type_keys('^f')  # Ctrl + F
    time.sleep(2)

    log(f"Entering bot name: {bot_name}...")
    for _ in range(25):
        keyboard.press_and_release('BackSpace')
    time.sleep(1)
    main_window.type_keys(bot_name)
    time.sleep(2)

    log("Pressing down key to select the bot and Enter...")
    main_window.type_keys('{DOWN}')
    time.sleep(1)
    main_window.type_keys('{ENTER}')
    time.sleep(2)

    log("Pressing Enter to start the bot...")
    main_window.type_keys('{ENTER}')
    time.sleep(2)

    click_link()

    time.sleep(2)

    log("Pressing F12 to open the developer console...")
    send_keys('{F12}')

    click_console(bot_name)

    keyboard.write('`')  # Simulating the ` key for switching console

    log("Activating command line with Ctrl+`...")
    keyboard.press_and_release('ctrl+`')
    time.sleep(1)

    # Entering command in the console
    send_keys(code)
    time.sleep(1)

    # Pressing Enter
    send_keys('{ENTER}')
    time.sleep(1)

    # Copying data from clipboard and writing to Excel
    write_to_excel(account_num, bot_name, row)

    time.sleep(1)
    log("Closing 2 windows")
    keyboard.press_and_release('alt+F4')
    time.sleep(1)
    keyboard.press_and_release('alt+F4')
    time.sleep(1)

    close_app()

    keyboard.press_and_release('Esc')
    time.sleep(1)

# Main function for working with multiple accounts
def main(account, bots_list, row):
    try:
        app = launch_telegram(account)
        for bot in bots_list:
            # Get the specific code for the bot, or use the default if not found
            code = codes.get(bot, "copy+9Telegram.WebApp.initData+0")
            interact_with_bot(app, bot, code, account, row)
    except Exception as e:
        log(mrh + f"Error while interacting with account {account}: {e}")
        open("error.log", "a", encoding="utf-8").write(
            f"Error while interacting with account {account}: {e} \n")
    finally:
        close_telegram(account)


# Loading accounts and bots
accounts_list = load_accounts_from_file('acc.txt')
bots_list = load_bots_from_file('bots.txt')

# Get the total number of accounts
total_accounts = len(accounts_list)

_banner()
log(f'Starting query collection for bots: {bru} {bots_list}')
log(f'Total accounts to process: {bru} {total_accounts}')

row = 1

for index, account in enumerate(accounts_list, start=1):
    log(f'Processing account {bru} {index} of {total_accounts}...')
    row += 1
    main(account, bots_list, row)