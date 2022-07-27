class Config:
    CONFIG = {
        "browser": {
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
        "editor": {
            "launch": ("code", ""),
            "urls": [],
            "duration": "",
            "shortcuts": ["ctrl+`", "ctrl+c", "ctrl+v", "ctrl+tab", "ctrl+shift+tab"],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "terminal": {
            "launch": ["qterm"],
            "duration": "",
            "shortcuts": ["up", "down", "enter"],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "tester": {
            "launch": ["postman"],
            "urls": [],
            "duration": "",
            "shortcuts": [],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "slack": {
            "launch": ["slack"],
            "urls": [],
            "duration": "",
            "shortcuts": [],
            "coordinates": [{"launch": ()}, {"close": ()}],
        },
        "hubstaff": {
            "launch": ["hubstaff"],
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
