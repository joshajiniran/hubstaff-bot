from dataclasses import dataclass
from typing import List

from tool import Application


@dataclass
class Session:
    current_app: Application
    apps: List[Application]
    session_time: int
    active: bool

    def switch_app(self, current_app: Application, next_app: Application) -> int:
        """Switch app as in alt+tab to another application"""
