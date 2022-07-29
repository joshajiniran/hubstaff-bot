import subprocess
from dataclasses import dataclass
from time import sleep
from typing import List, Optional

import psutil

from tool import Application


@dataclass
class Session:
    current_app: Optional[Application] = None
    apps: Optional[List[Application]] = None
    session_time: int = 2000
    active: bool = True

    def set_current_app(self, app: Application) -> None:
        """Set current app in the session , ensure app is running first"""
        self.current_app = app

    def get_current_app(self) -> Application | None:
        if self.current_app is None:
            return None

        return self.current_app

    def get_current_app_pid(self) -> int | None:
        if self.current_app is None:
            return None
        return self.current_app.pid

    def switch_app(self, current_app: Application, next_app: Application) -> None:
        """Switch app as in alt+tab to another application"""

    def close_app(self, app: Application) -> None:
        """Close an application and remove from session"""
        try:
            psutil.Process(app.pid).kill()
        except Exception as e:
            print("An exception occurred, could not close app", e)

    def start_app(self, app: Application) -> int:
        """Start an application that is not active but in the list of session apps"""
        try:
            subprocess.Popen(app.name, start_new_session=True)
        except FileNotFoundError as e:
            print(e) # use path to open
            subprocess.Popen("/home/projosh/Downloads/Compressed/Postman/Postman")
    
        while self.is_running != True:
            sleep(5)

        print("Application started...")
        return app.pid
