from importlib.resources import path
import os
from datetime import datetime

today = datetime.now()
# path = 'D:/shubham/python/date_file/'
# ti_c = os.path.getctime(today)
os.mkdir('D:/shubham/python/date_file/' + today.strftime("%Y-%m-%d"))
# print(f'the file is create at {ti_c} , {today}')
