# from pynotifier import Notification
# import psutil
# battery = psutil.sensors_battery()
# percent = battery.percent
# Notification("Battery Percentage", 
# str(percent)+ "%Percent Remaining", duration=10).send()

import psutil
psutil.cpu_times()