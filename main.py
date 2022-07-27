import subprocess

import psutil
import pyautogui

from config import LinuxConfig

"""
When the scripts starts running, check if the browser, code editor and postman is running, otherwise launch them
You want to automate mouse movement at intervals: scroll, click
You want to alternate between code and browser or any other app (postman, terminal etc) at intervals
You want to visit websites (usually stackoverflow, or sites that show you are working)

For more advance/complex automation, you want to copy an entire code and simulate typing it in the editor
toml/json config would hold configurations for 
"""


def automate_mouse():
    pass


def automate_keypress():
    pass


def automate_browsing(url: str):
    pass


def start_application(process_name: str):
    pass


def alternate_btw_apps():
    pass


if __name__ == "__main__":
    dev_tools: list[str] = ["postman", "brave", "qterminal", "code"]

    for tool in dev_tools:
        if tool not in (p.name() for p in psutil.process_iter()):
            print("yay, will call subprocess now")
            # either open with launcher or use a subprocess call
            try:
                subprocess.Popen(tool, start_new_session=True)
            except FileNotFoundError as e:
                print(f"Could not launch application {tool}")
                pyautogui.moveTo(5, pyautogui.size()[1], duration=0.5)
                pyautogui.hotkey("win", "r")

                pyautogui.press("postman")
                pyautogui.press("accept")
