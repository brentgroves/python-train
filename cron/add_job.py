# https://www.askpython.com/python-modules/python-crontab
# Importing the CronTab class from the module
from crontab import CronTab

# Creating an object from the class
## Using the root user
# cron = CronTab(user="root")
 
## Using the current user
my_cron = CronTab(user=True)