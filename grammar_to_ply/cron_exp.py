#Execute output ply program :
from crontab import CronTab
import os
cron = CronTab(user=True)
chdir = "cd "+os.getcwd()

job = cron.new(command=chdir +" && "+ ' /usr/bin/python ex.py>>cron.out  2>&1')

job.minute.every(1)
for item in cron:
    print item
cron.write()
print("done")
