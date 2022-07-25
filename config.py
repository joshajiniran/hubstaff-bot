class Config:
    APPLICATIONS = {
        "browser": "brave",
        "editor": "code",
        "terminal": "qterminal",
        "tester": "postman",
        "slack": "slack",
        "hubstaff": "hubstaff"
    }
    URLS = {
        "stackoverflow": "",
        "youtube": "",
        "reddit": ""
    }
    DURATION = {
        "alternate_apps": "",
        "scroll": "",
        "session": ""
    }
    SHORTCUTS = {
        "browser": ["ctrl+l", "ctrl+w", "ctrl+t", "ctrl+tab", "ctrl+shift+tab"],
        "editor": ["ctrl+`", "ctrl+c", "ctrl+v"],
        "terminal": ["up", "down", "enter"]
    }
    COORDINATES = {
        "hubstaff": {
            
        },
        "browser": {
            
        },
        "editor": {
            
        },
        "tester": {
            "launch": ()
        }
    }
