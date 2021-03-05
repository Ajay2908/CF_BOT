from datetime import date
import time


t = time.localtime()
today = date.today()
current_time = time.strftime("%H:%M:%S", t)
time_data = str(today)+'T'+str(current_time)


def get_time():
    return time_data
