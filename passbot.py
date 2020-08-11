import pyautogui
from time import sleep
import os

pyautogui.FAILSAFE = True


def get_screenshot_region():
    print("Take your mouse pointer to the top left corner of the target window")
    sleep(5)
    ss_x, ss_y = pyautogui.position()

    print("Take your mouse pointer to the bottom right corner of the window")
    sleep(5)
    ss_x2, ss_y2 = pyautogui.position()

    x_len, y_len = ss_x2 - ss_x, ss_y2 - ss_y
    return [ss_x, ss_y, x_len, y_len]


def generate_key(key_length, position=0, key="") -> str:
    if position == key_length:
        yield key
        return

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ch in chars:
        for generated_key in generate_key(key_length, position + 1, key + str(ch)):
            yield generated_key

pin_field = {}
submit_button = {}
pin_length = 4
screenshot_directory = "screenshots"

if not os.path.exists(screenshot_directory):
    os.mkdir(screenshot_directory)

print("Take your mouse pointer to the pin input field")
sleep(5)
pin_field['x'], pin_field['y'] = pyautogui.position()
print("Input field position:", pin_field['x'], pin_field['y'])
print("\n\n")

print("Take your mouse pointer to the submit button")
sleep(5)
submit_button['x'], submit_button['y'] = pyautogui.position()
print("Submit button position:", submit_button['x'], submit_button['y'])
print("\n\n")

region = get_screenshot_region()

for key in generate_key(pin_length):
    pyautogui.moveTo(pin_field['x'], pin_field['y'])
    pyautogui.click(pin_field['x'], pin_field['y'])
    pyautogui.typewrite(key)
    # sleep(0.1)

    pyautogui.click(submit_button['x'], submit_button['y'])
    # sleep(0.2)

    print(key)

    screenshot_file_name = "{screenshot_directory}/{key}.png".format(screenshot_directory = screenshot_directory, key = key)
    pyautogui.screenshot(screenshot_file_name, region)
