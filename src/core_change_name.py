import pyautogui
from src.cucumber import log, mrh, pth, hju, kng, bru, htm
import time
import pyperclip

add_to_name = "🍅"

image_paths = {
    "lines": [r"pic\change_name\lines.png"],
    "settings": [r"pic\change_name\settings1.png", r"pic\change_name\settings2.png"],
    "account": [r"pic\change_name\account1.png", r"pic\change_name\account2.png"],
    "name": [r"pic\change_name\name1.png", r"pic\change_name\name2.png"],
    "save": [r"pic\change_name\save1.png", r"pic\change_name\save2.png"],
}

def click_button(button_name):
    # Search and click on the "Console" tab
    log(f"Searching for {button_name} button on the screen...")

    images_paths = image_paths.get(button_name)

    for image_path in images_paths:
        try:
            button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if button_location:  # If the image is found, exit the loop
                log(hju + f"{button_name} found, clicking on it...")
                break
        except Exception as e:
            log(f'Error while searching for image {image_path}: {e}')
            open("error.log", "a", encoding="utf-8").write(
                f"Error while interacting with button {images_paths}: {e} \n")

    time.sleep(1)

    if button_location:
        pyautogui.click(pyautogui.center(button_location))
        time.sleep(2)
    else:
        log("Failed to find Console tab.")
        return


def paste_to_name():
    # Copy the string to clipboard before pasting
    log(bru + f'copy and paste it into the nickname {add_to_name}')
    pyperclip.copy(add_to_name)
    time.sleep(1)

    # Simulate pasting action (Ctrl + V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)