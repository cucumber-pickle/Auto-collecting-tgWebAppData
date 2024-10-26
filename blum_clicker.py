import time
from pywinauto.keyboard import send_keys
import pyautogui
from src.core import load_accounts_from_file, launch_telegram, close_telegram
from src.cucumber import _banner, log, mrh, pth, hju, kng, bru, htm
from src.core_change_name import click_button, paste_to_name
from blum.core_blum import blum_main
import os


# Function to search and click on the link
def click_link():
    time.sleep(1)  # Give time for the link to appear
    image_path = r"blum\launch.png"
    try:
        link_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    except Exception as e:
        log(f'Error while searching for image {image_path}: {e}')

    if link_location:
        log(hju + "Link found. Clicking on it...")
        pyautogui.click(pyautogui.center(link_location))
        time.sleep(2)  # Delay before pressing Enter
        send_keys('{ENTER}')  # Press Enter after 1 second
    else:
        log("Failed to find the link.")



# Function to interact with the bot
def interact_with_bot(app):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    log("Focusing on the Telegram window...")
    main_window = app.top_window()
    main_window.set_focus()

    log("Opening search...")
    main_window.type_keys('^f')  # Ctrl + F
    time.sleep(2)

    time.sleep(1)
    main_window.type_keys("@BlumCryptoBot")
    time.sleep(2)

    log("Pressing down key to select the bot and Enter...")
    main_window.type_keys('{DOWN}')
    time.sleep(1)
    main_window.type_keys('{ENTER}')
    time.sleep(2)

    click_link()

    log("Waiting 10 seconds for blum to load")
    time.sleep(10)

    blum_image = r"blum\blum.png"
    try:
        button_location = pyautogui.locateOnScreen(blum_image, confidence=0.7)
        if button_location:  # If the image is found, exit the loop
            log(hju + f"button found, clicking on it...")
        time.sleep(1)
        pyautogui.click(pyautogui.center(button_location))
        time.sleep(2)
    except Exception as e:
        log(f'Error while searching for image: {e}')

    pyautogui.scroll(-300)
    time.sleep(2)


    blum_game = r"blum\template_play_button.png"

    try:
        play_location = pyautogui.locateOnScreen(blum_game, confidence=0.8)
        if play_location:
            blum_main()
    except Exception as e:
        log(mrh + f"You don't have tickets for the game")
    time.sleep(1)

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