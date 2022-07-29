from typing import Optional


class Config:
    CONFIG = {
        "BROWSER": {
            "launch": ("brave", ""),
            "duration": "",
            "shortcuts": [
                "ctrl+l",
                "ctrl+w",
                "ctrl+t",
                "ctrl+tab",
                "ctrl+shift+tab",
                "ctrl+shift+i",
            ],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "EDITOR": {
            "launch": ("code", ""),
            "urls": [],
            "duration": "",
            "shortcuts": ["ctrl+`", "ctrl+c", "ctrl+v", "ctrl+tab", "ctrl+shift+tab"],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "TERMINAL": {
            "launch": ("qterminal",),
            "duration": "",
            "shortcuts": ["up", "down", "enter"],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "TESTER": {
            "launch": ("postman", "/home/projosh/Downloads/Compressed/Postman/Postman"),
            "urls": [],
            "duration": "",
            "shortcuts": [],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "SLACK": {
            "launch": ("slack",),
            "urls": [],
            "duration": "",
            "shortcuts": [],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "HUBSTAFF": {
            "launch": ("hubstaff",),
            "urls": [],
            "duration": "",
            "shortcuts": [],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
    }


class LinuxConfig(Config):
    pass


class WindowsConfig(Config):
    pass


class MacConfig(Config):
    pass


configuration: Optional[Config] = None

# You can use the factory class creational pattern
def setup_config(conf: str = "linux") -> Config:
    configs = {"linux": LinuxConfig(), "windows": WindowsConfig(), "mac": MacConfig()}
    global configuration
    configuration = configs[conf]
