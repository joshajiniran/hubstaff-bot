import subprocess
from dataclasses import dataclass, field
from enum import Enum, auto
from time import sleep
from typing import Any, Dict

import psutil

from config import configuration

print(configuration)


class AutoName(Enum):
    def _generate_next_value(name, start, cout, last_values):
        return name

class AppType(AutoName):
    EDITOR = auto()
    BROWSER = auto()
    MEDIA = auto()
    SYSTEM = auto()
    TESTER = auto()
    OTHERS = auto()


@dataclass
class Application:
    name: str
    launcher: str
    app_type: AppType
    pid: int = field(default=None)
    config: Dict[str, Any] = field(default_factory=dict)

    def is_running(self) -> bool:
        """Checks if the application is currently running"""
        return self.pid in (p.pid for p in psutil.process_iter())

app_type = AppType.TESTER
launcher = configuration.CONFIG[app_type.value]['launch']
app = Application('postman', launcher, app_type)

subprocess.Popen(app.launcher[0] or app.launcher[1], start_new_session=True)
