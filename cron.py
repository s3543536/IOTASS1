#!/usr/bin/env python3
from crontab import CronTab

#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add a new job
job = cron.new(command='/home/pi/Assignment1/log_pressure.py')

#configure job
job.minute.every(1)
cron.write()
