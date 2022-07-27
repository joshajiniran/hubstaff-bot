from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict


class AppType(Enum, str):
    EDITOR = "editor"
    BROWSER = "browser"
    MEDIA = "media"
    SYSTEM = "system"
    TEST_TOOL = "tester"
    OTHERS = "others"


@dataclass
class Application:
    name: str
    pid: int = field(default=None)
    app_type: str = AppType.EDITOR.value
    config: Dict[str, Any] = field(default_factory=dict)

    def start(self) -> int:
        """Starts application and returns the pid"""

    def stop(self) -> None:
        """Stops application from running"""

    @property
    def is_running(self) -> bool:
        """Checks if the application is currently running"""
