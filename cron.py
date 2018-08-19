#!/usr/bin/python3
from crontab import CronTab

#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add a new job
job = cron.new(command='/usr/bin/python3 /home/pi/IOTASS1/log_pressure.py')

#configure job
job.minute.every(60)
#job.hour.every(2)

cron.write()
