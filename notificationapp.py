import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "**Please drink water",
        message = "Water is good for health",
        app_icon = "D:\py projects\Paomedia-Small-N-Flat-Bell.ico",
        timeout = 5,
    )
