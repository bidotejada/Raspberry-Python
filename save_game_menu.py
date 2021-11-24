import json
import os
import sys
from os.path import exists
import time

# config file name
settings_file = 'saved_values.json'

# dictionary to hold settings options
rt_var = dict()
# rt_var['current_count'] = 0

# fetch the data
# check to see if files exist
if exists(settings_file):
    # open and load the data
    file = open(settings_file, 'r')
    rt_var_text = file.read()
    rt_var = json.loads(rt_var_text)
else:
    value1 = 24
    rt_var['key1'] = value1
    rt_var['color_sequence'] = [[100, 0, 0],  # red
                                [0, 100, 0],  # green
                                [0, 0, 100],  # blue
                                [47, 80, 38],
                                [30, 66, 29]]
    rt_var['current_color'] = 1
    rt_var['buzzer_freq'] = 50
    rt_var['buzzer_duration'] = 500  # in millisec
    rt_var_json = json.dumps(rt_var)
    file = open(settings_file, 'w')
    file.write(rt_var_json)
    file.close()

# try:
#     while True:
#         print(f"Current count: {rt_var['current_count']}")
#         rt_var['current_count'] += 1
#         time.sleep(2)
# except KeyboardInterrupt:
#     file = open('saved_values.json', 'w')
#     rt_var_json = json.dumps(rt_var)
#     file.write(rt_var_json)
#     file.close()
#     try:
#         sys.exit(0)
#     except SystemExit:
#         os._exit(0)
