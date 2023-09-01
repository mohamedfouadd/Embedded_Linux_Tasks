import psutil
from plyer import notification

battery = psutil.sensors_battery()
percent = battery.percent

print(percent)
notification.notify(
    title='low battery',
    message='battery low please charge',
    app_icon=None,
    timeout=10
)