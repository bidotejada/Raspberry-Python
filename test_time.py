from datetime import datetime
from time import sleep

current_time = float(datetime.now().time().strftime('%S'))

# some code that takes 2 seconds
sleep(2)

current_time1 = float(datetime.now().time().strftime('%S'))
time_elapsed = current_time1-current_time

print(time_elapsed)
