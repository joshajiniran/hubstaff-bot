import subprocess

import psutil
import pyautogui

from config import setup_config
from session import Session

"""
When the scripts starts running, check if the browser, code editor and postman is running, otherwise launch them
You want to automate mouse movement at intervals: scroll, click
You want to alternate between code and browser or any other app (postman, terminal etc) at intervals
You want to visit websites (usually stackoverflow, or sites that show you are working)

For more advance/complex automation, you want to copy an entire code and simulate typing it in the editor
toml/json config may hold configurations for settings/config
sqlite may hold state configs for app settings like desired coordinates, should run first/last, depends on app etc.
"""


if __name__ == "__main__":
    linux_config = setup_config("linux")

    dev_tools: list[str] = [
        linux_config.BROWSER,
        linux_config.EDITOR,
        linux_config.TERMINAL,
        linux_config.TESTER,
    ]

    # create a session: will hold the list of running applications
    session = Session()

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
