#!/usr/bin/python3
from crontab import CronTab

#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add a new job
log_pressure = cron.new(command='/usr/bin/python3 /home/pi/IOTASS1/log_pressure.py')
temp_notify = cron.new(command='/usr/bin/python3 /home/pi/IOTASS1/notify_phone.py')

#configure job
log_pressure.minute.every(60)
#log_pressure.hour.every(2)
temp_notify.minute.every(60)
temp_notify.hour.on(6)

cron.write()
