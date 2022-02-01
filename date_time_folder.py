from email.mime import base
import os
import datetime

today = datetime.datetime.now()
year = today.strftime("%Y")
month=today.strftime("%m")
day=today.strftime("%d")
# output = "/opt/output/"  + year +"/" + month + "/" + day
os.mkdir('D:/shubham/python/date_file/'  + year +"/" + month + "/" + day+'')

