# https://geekyhumans.com/set-up-crontab-in-python/
# * * * * * echo "Hello world" >> /var/log/cron.log 2>&1
# * * * * * /home/bgroves@BUSCHE-CNC.COM/srcpy/python-train/cron/script_test.py
# watch cat /var/log/cron.log
# https://www.askpython.com/python-modules/python-crontab
# 
# import random
from datetime import datetime
import random
now = datetime.now()
num = random.randint(1, 101)
with open('/var/log/cron.log', 'a') as f:  #write your own path here
  f.write('{} - The random number is {}\n'.format(now, num))  
